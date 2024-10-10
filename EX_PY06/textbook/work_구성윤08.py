#24.1    -->str 메서드 
# replace
a='Hello, world!'  
print(a.replace('world', 'python'))

# maketrans, translate
table= str.maketrans('aeiou', '12345')
print('apple'.translate(table))
##변환 테이블을 만들어서 문자 일부만 변환

#split 
a=('apple pear grape pineapple orange')
print(type(a))
a=a.split()
print(a)

# join  리스트를 str(하나의 문자열)로 변환
a='-'.join(a)
print(a)

a='   pyThon  '
print(a.upper())           #괄호 빼먹지 않기!
print(a.lower())         #삭제의 개념이라 괄호안에 문자 넣으면 삭제 가능
print(a.lstrip())
print(a.rstrip())
print(a.strip())

a=' "python" '
print(a.ljust(10))  
print(a.rjust(10))
print(a.center(10))    ##남는 공간 이용하여가운데 정렬

print(a.rjust(10).upper())
print('35'.zfill(4))  #->str메서드 남는 공간0으로 채움

a='apple pineapple'
print(a.find('pl')) #처음찾은 인덱스, 없으면 -1
print(a.find('xy'))
print(a.index('pl')) #find와 동일,but 없으면 ERROR
a= 'I am %s' %'james'
print(a)

#24.2 서식 지장자(format)
print('I am %s.' %'james')
name='maria'
print('I am %s.' %name)
print('I am %d years old' %20)
print('%f' %2.3)
print('%.2f' %2.3)    #-> .2 -->소수 자리수
print('%.3f' %2.3)
print('%10s' %'python') #->오른쪽 정렬 + 나머지 여백
print('%-10s' %'python') #->(-) 왼쪽 정렬 + 나머지 여백

print('Today is %d %s.' %(3, 'April'))
print('Today is %d%s.' %(3, 'April'))   #서식 지정자 공백도 인식함

print('Hello, {0}'.format('world!'))
print('Hello, {0}'.format(100))

print('Hello, {0} {2} {1}'.format('python', 'Script', 3.6)) 
#인덱스 지정해서 순서에 따라 도출, 또한 공백 인식함

print('{0} {0} {1} {1}'.format('python', 'script'))
#같은 값 여러번 사용 가능
print('Hello, {} {} {}'.format('python', 'Script', 3.6)) 
#공백시 순서대로 도출

print('Hello, {language} {version}'.format(language='python', version=3.6))

language='python'; version=3.6
print(f'Hello, {language} {version}')
#얘가 젤 편한듯

print('{0:<10}'.format('python')) #정렬도 가능
print('{0:>10}'.format('python')) #남는 칸은 공백으로

print('%03d' %1)
print('{0:03d}'.format(35))  #숫자 개수 맞추기

print('%08.2f'%3.6) #실수도 가능
print('{0:08.2f}'.format(150.37))

print('{0:0<10}'.format('python'))  #값을 넣어서 채울 수 있음
print('{0:0>10}'.format('python')) 

#24.4
path = 'c:\\wrwefwefwef\\wqefqwefasdfgatdh\\qwefwqf\\python.exe'
a= path.rfind('\\')
filename=path[a+1:] 
print(filename)

#24.5
data='they their the the the the the the se sg n i isrg nse i'
data2= data.split()
print(data2)
num= data.count('the')
x=-1
result=0
for d in data2:
    if d=='the':
        result+=1

print(result)
    



#24.6
x=[]
data='51900;83000;158000;367500;250000;59200;128500;1304000'
data2= data.split(';')
data2=list(map(int, data2))
print(data2)
data2.sort(reverse=True)
for d in data2:
    print(f'{d:>,}')


"""
# 29.1
def hello():
    print('Hello, world!')

hello()

# 29.2
def add(a,b):
    '''이 함수를 a와 b를 더한 뒤 결과를 반환하는 함수입니다.''' #->독스트링= 설명
    print(a+b)

add(10,2)

#29.3
def add(a,b):
    return a+b
x= add(12,3)
print(x)
print(add(12,3))

#29.4
def add_sub(a,b):
    return a+b, a-b
x, y= add_sub(10,20)
print(x,y)

#29.5
#함수를 사용될때만 불러와서 사용됨 
# ->함수의 변수들은 함수 종료시 사라짐

#29.7
x=10
y=3
def get_quotient_reminder(a,b):
    return a//b, a%b
quotient, remainder= get_quotient_reminder(x,y)
print('몫: {0}, 나머지:{1}'.format(quotient,remainder))

# 29.8
x,y= map(int,input().split())
def calc(a,b):
    return a+b, a-b, a*b, a/b
a,s,m,d= calc(x,y)
print('덧셈: {0}, 뺄셈: {1}, 곱셈: {2}, 나눗셈: {3}'.format(a,s,m,d))


#30.1
def print_numbers(a, b, c):
    print(a)
    print(b)
    print(c)

x=[10,20,30]
print_numbers(*x)
print_numbers(*[10,20,30])

def print_numbers(*args):
    for arg in args:
        print(arg)
print_numbers(10,20,30,40)


#30.2
def personal_info(name, age, address):
    print(f'이름: {name}')
    print(f'나이: {age}')
    print(f'주소: {address}')
personal_info(name='홍길동', age=30, address='서울시')
#키워드 =값으로 순서 상관없이 원하는 값 넣을 수 있음

x={'name':'홍길동','age':30, 'address':'서울시'}
personal_info(**x)
#dict 언패킹 ->키 값 한쌍이기 때문에 *두번 씀

#30.6
korean, english, mathmatics, science= 100,86,81,91
def get_max_score(*subs):
    return max(subs)
max_score= get_max_score(korean, english, mathmatics, science)
print(f'높은 점수: {max_score}')

#30.7
# get_min_max_score -> 최대, 최소 도출되도록
# 입력받는 값은 정수
# korean, english, mathmatics, science= map(int,input().split())
# def get_min_max_score(korean, english, mathmatics, science):
    
#     result= (max(korean, english, mathmatics, science),
#            min(korean, english, mathmatics, science))
#     return result
# def get_average(**sub):
#     result= sum(sub.values)/len(sub)

# min_score, max_score= get_min_max_score(korean, english, mathmatics, science)
# average_score= get_average(korean=korean, english=english, mathmatics=mathmatics, science=science)
# print('낮은 점수: {0:.2f}, 높은점수: {1:.2f}, 평균점수: {2:2.f}'.format(min_score, max_score, average_score))
# min_score, max_score= get_min_max_score(english, science)
# average_score= get_average(english=english, science=science)
# print('낮은 점수: {0:.2f}, 높은점수: {1:.2f}, 평균점수: {2:2.f}'.format(min_score, max_score, average_score))
"""