def add3(num1, num2):
    result= num1+num2
    return result


# 함수기능: 3개의 정수를 곱셈한 후 결과를 반환하는 함수
# 함수이름: multi
# 매개변수: num1, num2, num3
# 함수결과: 정수(result) 반환

def multi(num1, num2):
    result= num1*num2
    return result



# 함수기능: 2개의 정수를 나눈 후 결과를 출력하는 함수
# 함수이름: div
# 매개변수: num1, num2
# 함수결과: 실수(result) 반환

def div(num1,num2):
    if not num2:
        result= ('0으로 나눌 수 없습니다.')
    else: result= (num1/num2)
    return result

def minus(num1,num2):
    result= num1-num2
    return result

#연산수행 후 결과를 반환하는 함수
# 이름: cal
# 매개변수: 함수명, str숫자2개
# 함수결과:none(바로 출력)

def cal(func, num1, num2, op):
    num1=int(num1)
    num2=int(num2)
    print(f'결과: {num1} {op} {num2} = {func(num1, num2)}')

# 함수기능: 계산기 메뉴를 출력
# 함수이름: print_menu
# 매개변수: 없음
# 함수결과: 없음

def print_menu():
    print(f'{"*":*^16}')
    print(f'{"   계  산  기":16}')
    print(f'{"*":*^16}')
    print(f'{"*  1 덧    셈  *":16}')
    print(f'{"*":*^16}')
    print(f'{"*  2 뺄    셈  *":16}')
    print(f'{"*":*^16}')
    print(f'{"*  3 곱    셈  *":16}')
    print(f'{"*":*^16}')
    print(f'{"*  4 나 눗 셈  *":16}')
    print(f'{"*":*^16}')
    print(f'{"*  5 종    료  *":16}')
    print(f'{"*":*^16}')

while True:
    print_menu()

    choice= (input("메뉴 선택:"))
    if choice.isdecimal():
        choice=int(choice) 
    else:
        print('0~5사이 숫자만 입력하세요')
        continue

    if choice ==5:
        print("프로그램을 종료합니다.")
        break
    elif choice ==1: 
        print("덧셈")
        num1, num2= input('정수 2개를 입력하세요').split()
        cal(add3, num1, num2, '+')
    elif choice ==2: 
        print("뺄셈")
        num1, num2= input('정수 2개를 입력하세요').split()
        cal(minus, num1, num2, '-')
    elif choice ==3: 
        print("곱셈")
        num1, num2= input('정수 2개를 입력하세요').split()
        cal(multi, num1, num2, '*')
    elif choice ==4: 
        print("나눗셈")
        num1, num2= input('정수 2개를 입력하세요').split()
        cal(div, num1, num2, '/')
    else: print('선택된 메뉴가 없습니다')        

# 계산기 프로그램
# 사용자가 원하는 계산을 선택하는 메뉴 출력
# 종료 메뉴 선택시 프로그램 종료

# 사용자가 번호를 선택해서 연산할 수 있도록
# 예시 1. 덧셈 2. 뺄셈 .... 5. 종료
# 종료 전까지 반복

# 18*18 크기의 판