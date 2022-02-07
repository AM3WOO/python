#!python
print("Content-Type: text/html")
print()
import cgi
form = cgi.FieldStorage()
if 'id' in form:
    pageID = form["id"].value
    description = open('data/'+pageID, 'r').read() #파일구현및 본문기능구현
else:
    pageID = 'Welcome'
    description = 'Hello Web' #본문기능구현
print('''<!doctype html>
<html>
<head>
  <title>WEB1 - Welcome</title>
  <meta charset="utf-8">
  <link rel="stylesheet" href="style.css">
</head>
<body>
<h1><a href="index.py">WEB</a></h1>
<div id="grid">
  <ol>
    <li><a href="index.py?id=HTML">HTML</a></li>
    <li><a href="index.py?id=CSS">CSS</a></li>
    <li><a href="index.py?id=JavaScript">JavaScript</a></li>
  </ol>
  <div id="article">
<h2>{title}</h2>
<p>{des}</p>
</body>
</html>
'''.format(title=pageID, des=description)) #파일구현및 본문기능
