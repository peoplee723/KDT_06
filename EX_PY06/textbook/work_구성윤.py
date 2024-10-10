#3.1
print('hello world')
print("hello python")
#3.7 연습문제
print('hello world')
print('python programming')
#3.8
print('Hello, world!')
print('Hello, world!')

# 4.1
print('Hello, world!')
print('Hello'); print('1234')

# 4.2
#Hello, world! 출력
print('Hello, world!')
# print('Hello, world!')
a=1+2 #더하기
print(a)
print('Hello, world!')
#print('Hello, world!')
#print('1234567890')
# 더하기
# a = 1 + 2
#  print('Hello, world!')
# 4.3
# if a ==10:
# print('10입니다.')
if a == 10:
    print('10입니다.')

if a ==10:
    print('10')
    print('입니다.')

# 5.5
#0.2467*도로와의 거리(m)+4.159
#도로와의 거리=12m
road=12
x=0.2467
u=4.159

print(int(12*0.2467+4.159))  #7층
# 5.6
# AP * 0.6 +225
# AP= 102
print(102*0.6+225)  #286.2

#6.1
x, y, z = 10, 20, 30
print(x)
print(y)
print(z)

# x, y, z= 10,20
# Traceback (most recent call last):
#   File "c:\Users\KDP-25\Desktop\EX_PY06\textbook\unit3.py", line 55, in <module>
 # x, y, z= 10,20
# ValueError: not enough values to unpack (expected 3, got 2)
#값 부족 에러

y='Hello, world!'
print(y)
print(type(y))
a=10;b=20;c=a+b
print(c)

# 6.2
a=10;a+20
print(a)

a=10;a=a+20
print(a)
a=10;a+=20
a+=20
print(a)
#d+=10
# NameError: name 'd' is not defined (정의 오류)
# 6.3
#input()
# x= input()
# print(x)
# x= input('문자열을 입력하세요:')
#print(x)

# a= input('첫 번쨰 숫자를 입력하세요: ')#class->'str'
# b= input('두 번째 숫자를 입력하세요: ')
# print(a+b)

# a= int(input('첫 번쨰 숫자를 입력하세요: ')# -> 정수로 변환
# b= int(input('두 번째 숫자를 입력하세요: '))
# print(a+b)

#6.4
#a, b= input('문자열 두 개를 입력하세요: ').split('-')
#입력받은 값을 (공백) 기준으로 분리
#print(a+b)#->class:str

# a, b= input('문자열 두 개를 입력하세요: ').split()
# a= int(a)
# b= int(b) #or
# print(int(a)+int(b))

# a, b= map(int, input('숫자 두 개를 입력하세요: ').split())
# 입력받은 값은 (int)로, (공백)을 기준으로 분리
# print(a+b)

#6.6
#a, b, c=map(int, input("정수 세 개를 입력하시오: ").split())
#print(a+b+c)

# 6.7
a=50; b=100; c=None
print(c)

# 6.8
#안내문자 X + 네과목 평균 정수로 출력
# a, b, c, d= map(int, input().split())
# print(int((a+b+c+d)/4))

#7.1
# print(1,2,3)
# print('Hello', 'python')

print(1, 2, 3, sep=", ")
print(4,5,6, sep=',')
print('Hello', 'python', sep='')
print(1920, 1080, sep='*')

#7.2
print(1, 2, 3)
print(1, 2, 3, sep='\n')#\n->제어(개행) 문자(화면에 출력x)
print('1\n2\n3')
# print(1,'\n'2'\n',3) ->문법 오류 ???

print(1)
print(2)
print(3)
print(1, end='')
print(2, end='')
print(3)
print(1, end=' ')
print(2, end=' ')
print(3)

print('1','\n''2''\n','3')

#7.4
year=2000;month=10;day=27;hour=11;minute=43;second=59
print(year, month, day, sep='/',end=' ')
print(hour, minute, second, sep=':')

# 7.5
#year, month, day, hour, minute, second=input().split()

print(year,month,day, sep='-',end='t')
print(hour,minute,second, sep=':')


#8.1
print(3>1)
print(10== 10)
print(10!= 5)
print('python'== 'python')
print('Python'== 'python')
print('Python'!= 'python')
print(10>20, 10<20, 10>=10, 10<=10)
print(1== 1.0, 1 is 1.0, 1 is not 1.0)
#is와 is not은 객체를 비교

#8.2
print(True and True, True and False, False and True, False and False)
print(True or True, True or False, False or True, False or False)
print(not True, not False)
print(not True and False or not False)

#논리 연산 순서=> not-> and-> or 순서(순서 헷갈리면 괄호 사용)
#false and false or true-> false or true => true

print(10== 10 and 10!= 5, 
      10> 5 or 10< 3, not 10>5, not 1 is 1.0)
#비교 연산하고 논리 연산 판단

#8.4
korean =92;english=47;mathmatics=86;science=81
#50점 미만이면 불합격
print(korean>=50 and english>=50 and mathmatics>=50 and science>=50)

#8.5 정수로 변환해야함!
#korean, english, math, science=map(int, input().split())
print(korean>=90 and english>80 and math>85 and science>=80)

# 9.1 
hello= '''Hello, world!
안녕하세요.
python입니다.'''
print(hello)

s= "python isn't difficult"
print(s)
s= 'He said "python is easy"'
print(s)

#s= 'python isn't difficult'-> 문법오류

#s= "He said "python is easy""-> 문법오류
#\',\"를 통해 사용할 수 있음
print('python isn\'t difficult')

print("""'python' is a "programming language"
      that let you work quickly
      and
      integrate sysyems more effectively""")
#""""""->'," 둘다 사용 가능

