#!python
print("Content-Type: text/html")
print()
import cgi, os, view, html_sanitizer
sanitizer = html_sanitizer.Sanitizer()

form = cgi.FieldStorage()
if 'id' in form:
    title = pageID = form["id"].value
    description = open('data/'+pageID, 'r').read() #파일구현및 본문기능구현
    #description = description.replace('<', '&lt;') #xss(보안)
    #description = description.replace('>', '&gt;') #xss(보안)
    description = sanitizer.sanitize(description) #Pypi pip패키지매니저 (html_sanitizer)
    title = sanitizer.sanitize(title)
    updatelink = '<a href = "update.py?id={}">update</a>'.format(pageID)
    deleteaction = '''
        <form action="process_delete.py" method="post">
            <input type="hidden" name="pageID" value="{}">
            <input type="submit" value="delete">
        </form>
    '''.format(pageID)
else:
    title = pageID = 'Welcome'
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
'''.format(title=title,
           des=description,
           listStr=view.getList(), #moduel
           updatelink=updatelink,
           deleteaction=deleteaction)) #파일구현및 본문기능
