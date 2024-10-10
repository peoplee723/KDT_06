#10.1
a=[38,21,53,62,19]
print(a)
person=['james', 17,175.3,True]
print(person)

a=[]
print(a)
b=list()
print(b)
a=range(10)
print(a)
a=list(range(10))
print(a)

b=list(range(5,12))
print(b)
c=list(range(-4,10,2))
print(c)
d=list(range(10,0,-1))
print(d)

#10.2
a=(38,21,53,62,19)
print(a)
a=38,21,53,62,19
print(a)
person='james', 17, 175.3, True
print(person)

type(38)
a=38,
print(type(a))

a=tuple(range(10))
print(a)
b=tuple(range(5,12))
print(b)
c= tuple(range(-4,10,2))
print(c)

a=[1,2,3]
print(tuple(a))
b= 4,5,6
print(list(b))

y=4,5,6
d,e,f=y   #=1.d,e,f = 4,5,6 ->양변순서 바뀌면 안됨
print(d,e,f)
"""
a=input().split() # -> 나눗 데이터를 리스트 형태로 저장
print(a, type(a))  #-><class 'list'>
"""

#10.4
a=list(range(5,-10,-2))
print(a)
print(list(range(5,-10,-2)))

#10.5
print(tuple(range(-10,10,2)))
print(tuple(range(-10,10,3)))

#11.1

a=[1,2,3,4,5,6,7,8,9]
print(3 in a)
print(10 in a)
print(100 not in a)
print(3 not in a)
print(43 in (38,76,43,62,19))
print( 1 in range(10))
print('p' in 'Hello, python')

a=[0,10,20,30]
b=[9,8,7,6]
print(a+b)
#print(range(10)+range(10,21))
#->TypeError: unsupported operand 
#             type(s) for +: 'range' and 'range'
print(list(range(10))+list(range(10,21)))
print(tuple(range(10))+tuple(range(10,21)))
#연산 가능한 형으로 변환 후 사용

print('hello, '+'world!')

#print('hello, '+30)
# ->TypeError: can only concatenate str (not "int") to str
#str-int끼리 연산 안됨
print('hello, '+'30')
#int를 str로 변환후 연산 가능

print([1,2,3,4]*3)
#print(range(10)*3)
#TypeError: unsupported operand type(s) for 
#            *: 'range' and 'int'
#미지원 ->지원되는 형태로 변환 후 사용
print(list(range(10))*3)
print(tuple(range(10))*3)

print('hello, '*3)
a='hello, '
a=range(10)
print(len(a), len(b))
print(len(range(10)))

hello='Hello, world!'
print(len(hello))
hello='안녕하세요'
print(len(hello))
print(len(hello.encode('utf-8')))#->실제 바이트 수 표현

#11.3
a= [38,21,53,62,19]
print(a[0], a[2], a[0],sep='-')

b=tuple(a)
print(b[0])
r= range(0,10,2)
print(r[2])

hello='Hello, world!'
print(hello[7])
print(hello[:])#대괄호 안이 비어있으면 안됨
                #invalid syntax

#11.3
a=[38,21,53,62,19]
print(a[-1], a[-5])

b=(38,21,53,62,19)
print(b[-1])
print(r[-3])
print(hello[-4])
#print(a[5]) ->범위 벗어남
              #IndexError: list index out of range
print(a[-1], a[len(a)-1]) #인덱싱은 0부터 시작이므로
                        #끝위치는 개수-1
a=[0,0,0,0,0]
a[0]=38
a[1]=21
a[2]=53
a[3]=62
a[4]=19
print(a[0],a[4])
b=(0,0,0,0,0)
#b[0]=38 #튜플을 값 교체가 안됨
        #TypeError: 'tuple' object does not support 
        #            item assignment
r=range(10)
#r[0]=4  #range도 안됨
#        #TypeError: 'range' object does not support 
#                     item assignment
del a[2]
print(a)
#del b[2] #삭제 또한 지원 안함
#del r[2]
#del hello[2]
#TypeError: 'tuple' object doesn't support item deletion

#11.4
a=[0,1,2,3,4,5,6,7,8,9]
print(a[:4])

print(a[:10]) #범위를 지정할 때 끝은 인덱스 범위 벗어나도 됨
print(a[1:1])

#11.4
print(a[4:7])
print(a[4:-2])  #-2-> 끝에서 2번째
print(a[2:8:3])
print(a[2:9:3])
print(a[:7])
print(a[7:])
print(a[:])
print(a[:7:2])
print(a[7::2])
print(a[::2])
print(a[::])
print(a[5:1:-1])
print(a[::-1]) #폭을 음수로 지정하면 자동으로 뒤에서부터 가져옴
print(a[:len(a)])

b=(0,1,2,3,4,5,6,7,8,9)
print(b[4:7])
print(b[4:])
print(b[:7:2])

r=range(10)
print(r[4:7])
print(r[4:])
print(list(r[:7:2]))
hello="Hello, world!"
print(hello[2:9])
print(hello[2:])
print(hello[:9:2])
#[ : : ]=slice( , , )

a[2:5]=['a','b','c']
print(a)
#연속된 경우 개수를 맞추지 않아도 됨
#단, 요소 개수는 안 맞춤 만큼 변함
a=[1,2,3,4,5,6,7,8,9]
a[2:5]='a'
print(a,len(a)) #->7개로 요소 수 변함
a=[1,2,3,4,5,6,7,8,9]
a[2:5]=['a','b','c','d','e']
print(a,len(a)) #->11개로 요소 수 변함

a=[1,2,3,4,5,6,7,8,9]
a[2:8:2]=['a', 'b', 'c']
print(a)
#증가폭이 1초과일때 교체되는 수와 일치해야함
"""
a=[1,2,3,4,5,6,7,8,9]
a[2:8:2]=['a', 'b', 'c','d']
print(a)
""" #ValueError: attempt to assign 
     #sequence of size 4 to extended slice of size 3
      #교체 수 초과
#b[2:5]=['a','b','c']
#r[2:5]=['a','b','c']
#hello[2:5]=['a','b','c']
#tuple, range, str-> 교체 지원 안함

del a[2:5]
print(a)
del a[2:5:2]
print(a)
"""
del b[2:5]
del r[2:5]
del hello[2:5]
""" #삭제또한 지원 안함

#11.6
year=[2011,2012,2013,2014,2015,2016,2018]
population= [10249679, 10195318, 10143645, 10103233, 10022181, 9930616, 9857426, 9838892]
print( year[-1:-4:-1], population[-1:-4:-1])

print( year[-3:], population[-3:]) #좀 더 짧음

#11.7  --->인덱스가 홀수인 (실제 값이 홀수x)
n=-32,75,97,-10,9,32,4,-15,0,76,14,2
print(n[::2])

#11.8
#x=input().split()
#del x[-5:]
#print(tuple(x)) 
#입력받은 값은 띄어쓰기 기준으로 입력, 뒤 5요소 삭제 후 튜플로 변환

#11.9???? 왜 str로 변환할때 [""]->도 포함되는가?
x=input().split()
y=input().split()
print(type(x),x)
x=str(x)
y=str(y)
print(x,y)

print(x[3:-2:2],y[4:-2:2],sep='')