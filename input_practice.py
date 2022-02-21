#input
string = input("인사말을 입력하세요>")  #명령프롬프트로부터 데이터를 받아오는 input함수
print(string) #-->리턴값
print(type(string)) #자료형=str(문자열)
number = input("숫자를 입력하세요")
print(number)
print(type(number)) #자료형=str(문자열)

#int (#float)
int_number = int(number) #int()함수를 통해 문자열을 숫자열로 바꾸기
print(type(int_number)) #int

#str
str_a = str(321.1221)
print(type(str_a))

#활용
input_a = float(input("숫자를 입력하시오"))
input_b = float(input("숫자를 입력하시오"))
print("덧셈:", input_a + input_b)
print("뺄셈:", input_a - input_b)
print("곱셉:", input_a * input_b)
print("나눗셈:", input_a / input_b)