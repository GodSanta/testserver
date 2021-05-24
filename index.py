#!C:\Users\82109\AppData\Local\Programs\Python\Python38-32\python.exe
# -*- coding:UTF-8 -*- 
print('content-type: text/html; charset=utf-8\n')
import cgi, os, urllib
form = cgi.FieldStorage()
if 'id' in form:
    pageID = form["id"].value
    f=open('webs/'+pageID+".txt",'r')
    print(f.read())
else:
    pageID = "KSW's World"
    files = ''
    if 'Search' in form:
        Search=form["Search"].value
        for i in os.listdir('webs'):
            i=i.replace('.txt','')
            if Search in i:
                files += '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=i)
        if files == '':
            files = '<h1>None</h3>'
    else:
        for i in os.listdir('webs'):
            i=i.replace('.txt','')
            files += '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=i)
    if 'comment' in form:
        comment = form["comment"].value
        cf=open('comment.txt','a')
        cf.write('<p><h3>{comment}</h3></p>'.format(comment=comment))
        cf.close()
        print('<script>location.href="http://localhost/index.py";</script>')
        
    comment = open('comment.txt','r')
    print('''<!doctype html>
    <html>
        <head>
            <title>{title}</title>
            <meta charset="UTF-8" />
        </head>
        <body>
            <h1><a href="index.py">{title}</a></h1>
            <ol>
                <h2>
                    <form action="index.py" method="post">
                        <input type="text" name="Search" placeholder="Search" value="">
                        <input type="submit">
                    </form>
                    {files}
                    <li>Search images</li>
                    <form action="imgs.py" method="post">
                        <input type="text" name="imgsearch" placeholder="Search img">
                        <input type="submit">
                    </form>
                    <li>Comment</li>
                    <form action="index.py" method="post">
                        <input type="text" name="comment" placeholder="Write Comment">
                        <input type="submit">
                    </form>
                    {comment}
                </h2>
            </ol>
        </body>
    </html>'''.format(title=pageID,files=files,comment=comment.read()))