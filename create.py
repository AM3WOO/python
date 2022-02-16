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
  <ol>
    {listStr}
  </ol>
  <a href = "create.py">create</a>
  <form action="process_create.py" method="post">
      <p><input type="text" name="title" placeholder="title"></p>
      <p><textarea rows="4" name="description" placeholder="description"></textarea></p>
      <p><input type="submit"></p>
  </form>
  </form>
</body>
</html>
'''.format(title=pageID, des=description, listStr=listStr)) #파일구현및 본문기능
