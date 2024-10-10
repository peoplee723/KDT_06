#16.1
for i in range(100):
    print('hello, world')

for i in range(100):
    print('Hello, world!', i)

for i in range(5,12):
    print('Hello, world!', i)

for i in range(0, 10, 2):
    print('Hello, world!', i)

for i in range(10,0,-1):
    print('Hello, world!', i)

for i in reversed(range(10)):     #0~9까지를 뒤짐음-->9부터 0까지
    print('Hello, world!', i)

# 16.2
# count= int(input('반복할 횟수를 입력하세요'))
# for i in range(count):
#     print('Hello, world!', i)

# 16.3
a=[10,20,30,40,50]
for i in a:                       #요소를 꺼내면서 반복
    print(i)

fruits=('apple', 'orange', 'grape')
for fruit in fruits:
    print(fruit)

for letter in 'python':
    print(letter, end='')


for letter in reversed('python'):
    print(letter, end='')

#16.5
x=[49,-17,25,102,8,62,21]
for i in x:
    print(i*10, end=' ')

#16.6
dan=int(input())
x=range(1,10)
for i in x:
    print(f'{dan} * {i} = {dan*i}')