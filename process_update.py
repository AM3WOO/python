#!python
import cgi, os
form = cgi.FieldStorage()
pageID = form["pageID"].value #hidden으로 가린 pageID 값 받아옴
title = form["title"].value
description = form["description"].value

#submit 눌렀을때 data폴더에 읽기 파일생성
opened_file = open('data/'+pageID, 'w') #파일을 title값이아닌 고정된 pageID값으로 열기
opened_file.write(description)
opened_file.close()

os.rename('data/'+pageID, 'data/'+title) #기존네임 pageID -> 바꿀네임 tile 로 바꿈

#Redirection
print("Location: index.py?id="+title)
print()
