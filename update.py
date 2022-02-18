#!python
print("Content-Type: text/html")
print()
import cgi, os, view
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
    {listStr}
  </ol>
  <a href = "create.py">create</a>
  <form action="process_update.py" method="post">
      <input type="hidden" name="pageID" value="{form_default_title}"
      <p><input type="text" name="title" placeholder="title" value="{form_default_title}"></p>
      <p><textarea rows="4" name="description" placeholder="description">{form_default_description}</textarea></p>
      <p><input type="submit"></p>
  </form>
  </form>
</body>
</html>
'''.format(title=pageID, des=description, listStr=view.getList(), form_default_title=pageID, form_default_description=description)) #파일구현및 본문기능
