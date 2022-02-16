#!python
print("Content-Type: text/html")
print()
import cgi, os
files = os.listdir('data')
listStr = ''
for item in files:
        listStr = listStr + '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=item) #listStr = listStr(기존의값) + ~
form = cgi.FieldStorage()
if 'id' in form:
    pageID = form["id"].value
    description = open('data/'+pageID, 'r').read() #파일구현및 본문기능구현
    updatelink = '<a href = "update.py?id={}">update</a>'.format(pageID)
    deleteaction = '''
        <form action="process_delete.py" method="post">
            <input type="hidden" name="pageID" value="{}">
            <input type="submit" value="delete">
        </form>
    '''.format(pageID)
else:
    pageID = 'Welcome'
    description = 'Hello Web' #본문기능구현
    updatelink = ''
    deleteaction = ''
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
    {listStr}
  </ol>
  <a href = "create.py">create</a>
  {updatelink}
  {deleteaction}
<h2>{title}</h2>
<p>{des}</p>
</body>
</html>
'''.format(title=pageID, des=description, listStr=listStr, updatelink=updatelink, deleteaction=deleteaction)) #파일구현및 본문기능
