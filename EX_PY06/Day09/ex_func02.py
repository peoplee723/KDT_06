def add3(num1, num2, num3):
    result= num1+num2+num3
    return result


# 함수기능: 3개의 정수를 곱셈한 후 결과를 반환하는 함수
# 함수이름: multi
# 매개변수: num1, num2, num3
# 함수결과: 정수(result) 반환

def multi(num1, num2, num3):
    result= num1*num2*num3
    return result

print(add3(3,5,7), multi(3,5,7))

# 함수기능: 2개의 정수를 나눈 후 결과를 출력하는 함수
# 함수이름: div
# 매개변수: num1, num2
# 함수결과: 실수(result) 반환

def div(num1,num2):
    if not num2:
        result= print('0으로 나눌 수 없습니다.')
    else: result= print(num1/num2)
    return result


# 계산기 프로그램
# 사용자가 종료를 원할때 종료 ->'x'(대소문자 둘다) 입력시
# 연산방식과 숫자 데이터 입력 받기

while True:
    # 1. 입력받기
    req=input("연산(+,-,*,/)방식과 정수 2개 입력(예:+ 10 2)")
    # 2. 종료조건 검사
    if req=='x' or 'X':
        print('계산기를 종료합니다')
        break
    # 3. 입력에 대한 연산방식과 데이터 추출
    op,num1,num2= req.split()
    # str정수를 int로 변환
    num1=int(num1);num2=int(num2)
    # 입력받은 값을 바탕으로 연산 실행
    if op=='+':
        print(f'{num1} {op} {num2} = {add3(num1, num2)}')
    elif op=='-':
        print(f'{num1} {op} {num2} = {num1 - num2}')
    elif op=='*':
        print(f'{num1} {op} {num2} = {multi(num1, num2)}')
    elif op=='/':
        print(f'{num1} {op} {num2} = {div(num1, num2)}')
    else:
        print('지원되지 않는 연산방식입니다.')