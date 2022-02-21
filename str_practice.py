#index
print("안녕하세요"[0]) #안 (indexing)
print("안녕하세요"[-5]) #안 (indexing)
print("안녕하세요"[0:3]) #안녕하 (slicing)
print("안녕하세요"[:3]) #안녕하 (slicing)
print("안녕하세요"[3:]) #세요 (slicing)

#slicing 처리를 해도 원본은 변하지 않음
hello = "안녕하세요"
print(hello[0:2]) #안녕
print(hello) #안녕하세요

#len (문자열의 길이)
print(len("안녕하세요"))

#복합대입연산자
number = 100
number *= 10 #number = number * 10
print(number)
string = "안녕하세요"
string +="!" #string = sting + "!""
print(string)
