#!python
import cgi
form = cgi.FieldStorage()
title = form["title"].value
description = form["description"].value

#submit 눌렀을때 data폴더에 읽기 파일생성
opened_file = open('data/'+title, 'w')
opened_file.write(description)

#Redirection
print("Location: index.py?id="+title)
print()
