#22.1 
a=[10,20,30]
a.append(500)
print(a)
a=[]
a.append(10)
print(a)

a.append([500,600])
print(a)

#insert(인덱스, 요소)
a=[10,20,30]
a.insert(2,500)
print(a,len(a))

a=[10,20,30]
a.insert(1,[500,600])
print(a)


#삭제
# pop,del->인덱스, remove 값을 통해 삭제
a=[10,20,30]
a.pop()
print(a)
a=[10,20,30,20]
a.pop(1)
print(a)
a=[10,20,30,20]
del a[0]
print(a)

a=[10,20,30]
a.remove(20)
a=[10,20,30,20]
a.remove(20)
print(a)
# index, count->>값을 넣어서 사용
a=[10,20,30,15,20,40]
print(a.index(20))

a=[10,20,30,15,20,40]
print(a.count(20))
a=[10,20,30,15,20,40]
a.reverse()
print(a)
a=[10,20,30,15,20,40] 
a.sort        #->none이므로 a를 도출하여 결과 확인 가능
print(a)
a.clear()
print(a, len(a))
# = del a[:]
# 매서드가 아닌 슬라이싱으로도 추가 가능
a=[10,20,30,15,20,40]
a[len(a):]=[500]
print(a)

#22.2
a=[0,0,0,0,0,0,0]
b=a
print(a is b)                     #주소 공유
b[2]=99
print(a, b, sep='\n')

a=[0,0,0,0,0,0,0]
b=a.copy
print(a is b)  # ->복사해서 새로운 곳에 저장
print( b, type(b))
b  = '99'
print(a, b, sep='\n')

#22.3
a=[38,21,53,62,19]
for i in a:
    print(i)

for i in [38,21,53,62,19]:
    print(i)

for index, value in enumerate(a): #a의 인덱스 값과 데이터 값을 쌍으로 추출
    print(index+1,value)

a=[38,21,53,62,19]
i=0
while i<len(a):
    print(a[i])
    i+=1

#22.4
a=[38,21,53,62,19]
smallest=a[0]
for i in a:
    if i< smallest:       #38보다 작으면 그 수로 바꿈
        smallest=i            #-->리스트 끝까지 반복

a=[38,21,53,62,19]
largest=a[0]
for i in a:
    if i< largest:       #38보다 크면 그 수로 바꿈
        largest=i            #-->리스트 끝까지 반복

a=[10,10,10,10,10]
x=0
for i in a:
    x+=i
print(x)

#22.5 list comprehension

a=[i for i in range(10)]
print(i)     #0~10까지 반복하는 i를 a에 집어넣음

c=[i+5 for i in range(10)] #연산자도 삽입 가능
print(c)

a=[i for i in range(10) if i%2==0] #조건식도 삽입 가능
print(a)     #2로 나눴을때 나머지가 0인 수만 삽입

b=[i +5 for i in range(10) if i%2==0]  #복합적 사용
print(b)

a=[i*j for j in range(2,10)         #들여쓰기 권장(가독성)
        for i in range(1,10)]

#22.6  map->ilterable한 객체만 사용가능! 
a=[1.2,2.5,3.7,4.6]
for i in range(len(a)):
    a[i]= int(a[i])
print(a)

a=[1.2,2.5,3.7,4.6]
a=list(map(int, a))
print( a, type(a[0]))

a=list(map(str,range(10)))
print(a,type(a[4]))

# a=map(int, input().split())   #괄호 넣는거 잊지 말기!!
# print(a)

#22.7
a=(10,20,30,15,20,40)
print(a.count(20))

a=tuple(i for i in range(10) if i%2==0)
print(a)

a=[1.2,2.5,3.7,4.6]
a=tuple(map(int, a))
print( a, type(a[0]))


a=[1,2,3,4,5,6,7,9,9]

print(a)

#22.9
a=['alpha','bravo','charlie', 'delta', 'echo', 'foxtrot', 'golf'
   , 'hotel', 'india']
b=[i for i in a if len(i)==5]
print(b)

#22.10
# a,b= map(int, input().split())
# print(a, type(a))
# print(b, type(b))
# x=[2**i for i in range(a,b+1) ]
# del x[1]; del x[-2]
# print(x)

#25.1
x={'a':10, 'b':20, 'c':30, 'd':40}
x.setdefault('e') #value가 none인 키 생성
print(x)

x={'a':10, 'b':20, 'c':30, 'd':40}
x.update(a=90)   #따옴표 있으면 안됨, 키가 문자일 때만 사용 가능!
print(x)         #숫자일 때는 {1:'one'} 으로 가능

x.update(a=900, f=60) #없으면 삽임, 여러개 수정 가능
print(x)

x={'a':10, 'b':20, 'c':30, 'd':40}
x.pop('a')      #삭제할 쌍의 키 넣기

print(x)             
x={'a':10, 'b':20, 'c':30, 'd':40}
del x['a']    #del 사용해도 삭제 가능

x={'a':10, 'b':20, 'c':30, 'd':40}
x.clear()          #모든 쌍 삭제
print(x)

x={'a':10, 'b':20, 'c':30, 'd':40}
x.get('a')  #특정 키의 값 반환(키가 없을 경우 none)

print((x.items()))  #키-값 쌍
print((x.keys()))    #키만
print((x.values()))  #밸류만

keys=['a','b','c','d']
x=dict.fromkeys(keys) #keys를 키로 해서 dict생성
y=dict.fromkeys(keys, 100) #임의의 값 할당 가능
print(x,y, sep='\n')

#25.2
x={'a':10, 'b':20, 'c':30, 'd':40}
for i in x:               #키만 추출
    print(i,end='')

x={'a':10, 'b':20, 'c':30, 'd':40}
for key, value in x.items():
    print(key, value)


