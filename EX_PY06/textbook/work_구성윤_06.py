#17.1 
i= 0
while i<100:
    print('hello, world')
    i+=1

i= 1
while i<100:
    print('hello, world')
    i+=1

i= 100
while i>1:
    print('hello, world')
    i-=1

#count=int(input('반복할 횟수를 입력하세요: '))

# i=0
# while i<count:
#     print('Hello, world!', i)
#     i+=1

import random
random.random()
random.randint(1, 6)

i=0
while i !=3:
    i = random.randint(1,6)
    print(i)

#17.5
i=2; j=5
while i<=32 or j>=1:
    print(i, j)
    i *= 2; j -= 1

#17.6
money=10000
while money>=1350:
    money-=1350
    print(money)

#18.1

i=0
while True:
    print(i)
    i +=1
    if i==100:
        break         #100일때 종료

for i in range(10000):
    print(i)
    if i==100:
        break

#18.2
for i in range(100):
    if i % 2 == 0:   #조건: 컨티뉴-> 거짓일때 출력, 참일때 건너뜀
        continue                   #참일때 continue가 실행됨
    print(i)

i=0
while i<100:
    i+= 1
    if i%2 ==0:
        continue
    print(i)

#18.3
# count = int(input('반복할 횟수를 입력하세요'))
# i=0
# while True:
#     print(i)
#     i+=1
#     if i==count:
#         break
# count =int(input('반복할 횟수를 입력하세요: '))

# for i in range(count +1):
#     if i % 2 == 0:
#         continue
#     print(i)

#18.5
i=0
while True:
    if i%10 !=3:      #3으로 끝나는 숫자= /10 나머지가 3
        i+=1          #나머지가 3이 아닌 숫자는 continue +1
        continue      #나머지가 3인 숫자는 출력 +1
    if i>73:
        break
    print( i, end=' ')
    i +=1
#출력이 안되는 경우도 i를 증가시켜 무한반복 피해야함
#3으로 끝나는 숫자가 10씩 커짐 -> 순서를 사용해서 추출하는 것도 가능
#18.6
# start,stop = map(int, input().split())

# i=start
# while True:
#     if i%10==3 and start<=i<=stop:
#         i+=1
#         continue
#     if i>stop: break
#     print(i,end=' ')
#     i+=1
#중복을 줄이기 위해 +1을 시작하고 코드 시작할 수 있음
# +무한반복 되는 오류 줄일 수 있음
#3으로 끝나는 수 추출, 끝나는 수까지 가면 반복종료, 그전까진 출력

# 19.1
for i in range(5):
    for j in range(5):
        print('j', j, sep='', end=' ')
    print('i:', i, '\\n',sep='')
#j 1,2,3,4 출력하고 i1, 다시 j 1,2,3,4출력하고 i2...
#출력은 위에서 아래로, for문은 한번 출력하면 for문으로 올라가서 출력

#19.2
for i in range(5):
    for j in range(5):       #아래 포문(별5개생성)을 5번 반복
        print('*',end='')
    print()                  #print는 다 출력하고\n자동이므로
                             #여기서는 줄바꿈 용도로 사용함
                            #  여기서 i범위가 세로, j가 가로 역할

for i in range(3):             #3줄 형태면 가로 x, 세로j인 사각형을
    for j in range(7):         #반복하는 형태로 출력
        for x in range(5):
            print('*', end='')
        print()
    print()
#19.3
for i in range(5):
    for j in range(5):
        if j <= i:
            print('*', end='')
    print()

for i in range(5):
    for j in range(5):
        if j == i:
            print('*', end='')
        else:
            print('', end=' ')
    print()

# 19.5 
for i in range(5):
    for j in range(5):
        if int(j)>=int(i):
            print('*', end='')
        else:
            print('', end=' ')
    print()        

# 19.6     ????
                           #층수니까 홀수번만 출력
# height=int(input())                       #3-> 1, 3, 5

# for h in range(1,height+1):
#     space=' '*(height-h)
#     star='*'*(2*h-1)
#     print(space+star)

#변수를 기준으로 생각하기
#변수는 층수
##층수의 위치가 바로 중앙 ex)5층이면 5칸이 중앙
#별의 갯수는 항상 홀수
#층당 별의 개수->층*2-1
#공백 ->    5층일때 1층의 공백은 층수-1
#문자에서 곱하기는 반복하는 수

#20.1
for i in range(1, 101):
    if i%3==0 and i%5==0:
        print('Fizz', 'Buzz')
    elif i%3==0:
        print('Fizz')
    elif i%5==0:
        print('Buzz')
    else:
        print(i)
#순서주의! 공배수가 먼저가야지 인식함
#15의 배수일때 ->15배수 아닌 수 중에서 3 또는 5의 배수일때
#반대일 경우 15배수 코드 인식 안함
#20.4
for i in range(1, 101):
    if i%15:                 #3과 5의 최소공배수=15
        print('Fizz', 'Buzz')
    elif i%3==0:
        print('Fizz')
    elif i%5==0:
        print('Buzz')
    else:
        print(i)
#20.5
for i in range(1, 101):
    print('Fizz'*(i%3==0)+ 'Buzz'* (i%5==0) or i)
#문자의 곱=반복, 문자의 합->이어쓰기, True=1,False=0
# or연산자를 통해 FizzBuzz에 해당하지 않는 수 처리

#20.7
for i in range(1, 101):
    if i%22==0:
        print('FizzBuzz')
    elif i%2==0:
        print('Fizz')
    elif i%11==0:
        print('Buzz')
    else:
        print(i)

#20.8
x, y=map(int, input().split())

for i in range(x,y+1):
    print('Fizz'*(i%7==0)+'Buzz'*(i%5==0) or i)
