#조건부표현식으로 나타내기
# 임의의 숫자가 5의 배수인지 아닌지 결과를 출력하세요
# 단, 2와 5를 제외한 나머지는 고려하지 x

num=5
print('5의 배수') if not num%5 else print('5의 배수가 아님')

#문자열을 입력 받아서 문자열의 원소 개수를 저장
# 단, 원소 개수가 0이면 None 저장
# 1. 입력받기
# 2. 길이 재기
# 3. 잰 길이 저장, 단 0인 경우 None저장하기

# data=input()
# print(data)

# result=len(data) if len(data) else None     #result=None 왜 안되지??
# print(f'{result}의 원소개수: {len(result)}') 


#실습 ->연산자(사칙연산자:+-*/) 와 숫자 2개 입력 받기
# 입력된 연산자에 따라 계산 결과 저장

data=(input().split())
data=list(data)
num=list(map(int, data[1:]))
x =data[0]

if x=='+':
    rusult = num[0]+num[1]
elif x== '-':
    result = num[0]-num[1]
elif x== '*':
    result = num[0]*num[1]
elif x== '/':
    result = num[0]/num[1]
else:
    print('사칙 연산자가 아님니다')



if x=='+':
    print(f'{data[1]} {data[0]} {data[2]} = {num[0]+num[1]}')
elif x== '-':
    print(f'{data[1]} {data[0]} {data[2]} = {num[0]-num[1]}')
elif x== '*':
    print(f'{data[1]} {data[0]} {data[2]} = {num[0]*num[1]}')
elif x== '/':
    print(f'{data[1]} {data[0]} {data[2]} = {num[0]/num[1]}')
else:
    None


print(data, type(data[1]), len(data))
print(f'{data[1]} {data[0]} {data[2]} = {int(data[1]),data[0],int(data[2])}')

