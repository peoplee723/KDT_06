# 함수의 이해 및 활용
# 
# 
# 함수기능: 3개의 정수를 덧셈한 후 결과를 반환하는 함수
# 함수이름: add3
# 매개변수: num1, num2, num3
# 함수결과: 정수(result) 반환

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

(div(8,4),div(3,0))

# 함수 호출하기
# 덧셈하기
value= (add3(1,2,3))

# 나눗셈하기
value1= div(3,4)
print(value1) #-print- 출력은 기능, 리턴값=None

# 리턴값은 필요에 따라 넣기


#함수기반 계산기 프로그램
# 4칙 연산 기능별 함수 생성 =>덧셈, 뺄셈, 곱셈, 나눗셈
# 2개 정수만 계산

# 함수이름: cal
# 함수기능: 사칙연산
# 매개변수:num1, num2
# 함수결과: none

# 기호, 숫자1,숫자2 입력받음
# 입력받은 기호에 따라 연산 수행
# 기호가 없거나 틀릴때, 나눗셈 0의 경우 오류처리
# add, mius


def cal(sim,num1,num2):
    if sim not in ('+', '-', '*', '/'):
        print('기호를 정확히 입력해 주세요')
    elif sim=='+':
        print(f'({num1} {sim} {num2} = {num1 + num2})')
    elif sim=='-':
        print(f'({num1} {sim} {num2} = {num1 - num2})')
    elif sim=='*':
        print(f'({num1} {sim} {num2} = {num1 * num2})')
    elif sim=='/':
        if not num2: print('0으로 나눌 수 없습니다')
        else: print(f'({num1} {sim} {num2} = {num1 / num2})')    

cal('+', 2, 3)
# 매개변수 비우면 에러 ->>

