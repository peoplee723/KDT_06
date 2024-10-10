#조건부 표현식
# - 조건문을 1줄로 축약해주는 문법
# 다중조건문을 축약할 때 사용
# 다른 프로그래밍 언어에서 상항연산자와 유사
# 형식: 참실행코드 if조건식 else 거짓실행코드

#실습 -> 임의의 숫자 데이터를 정하기
#   해당 숫자 데이터가 짝수인지 홀수 인지 판별 하는 코드

#어떤 방식으로 판별할까 -> 짝수로 나눠서 나머지로 판별
#어떤 숫자로 할까 -> 4=>나머지 0,1,2,3 (경우의 수가 너무 많다)
#                  2=> 나머지 0,1  

num=7
print(num%2)
#비교연산
if num%2 ==0:
    pirnt('짝수')
else: print("홀수")

#or 값으로 판별
if num%2: print('홀수')   #나머지가 있을때 참으로 인식
else: print('짝수')

#not 연산자
if not num%2: print('짝수')   #not참= False
else: print('홀수')

##1줄로 조건식을 축약 --> 조건부 표현식
num=2
print("짝수") if num%2 ==0 else print("홀수")
print("홀수") if num%2 else print('짝수')
print("짝수") if not num%2 else print("홀수")