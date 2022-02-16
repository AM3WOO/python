#!python
import cgi, os
form = cgi.FieldStorage()
pageID = form["pageID"].value #pageID만 받아옴

os.remove('data/'+pageID)

#Redirection
print("Location: index.py")
print()
