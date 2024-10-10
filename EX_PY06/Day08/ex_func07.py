# 기능= 입력 데이터가 유효한 데이터인지 검사해주는 기능
# 함수이름= check_data
# 매개 변수= 문자열 데이터, 데이터 갯수, count, sep=' '
# 함수 결과: 유효 여부 True/False

def check_data(data, count, sep=' '):
    # 데이터 여부
    if len(data):
        data2= data.split()
        return True if count==len(data2) else False
    else:
        return False
print(check_data('+, 10 ,3' ,3 ,','))






# 덧셈, 뺄셈, 곱셈, 나눗셈 함수를 각각 만들기
# 변수: 정수 2개
# 결과: 연산 결과 반환

def plus(num1,num2):
    result=num1+num2
    return result

def minus(num1,num2):
    return num1-num2

def div(num1,num2):
    return num1/num2 if not num2==0 else '0으로 나눌 수 없음'
                        #에러가 날 경우를 처리해 줘야 함
def multi(num1,num2):
    return num1*num2

print(plus(3,5), minus(5,9), div(10,2), multi(3,8))
plus(12,4)

# 사용자로부터 연산자, 숫자1, 숫자2를 입력 받아서
# 연산 결과를 출력해주세요
# input('연산자, 숫자1, 숫자2:').split()

x,y,z=input('연산자, 숫자1, 숫자2:').split()
if x not in ['+','-','*','/']:
    print(f'{x}는 잘못된 연산자입니다.')
else:    
    if y.isdecimal() and z.isdecimal:
        y=int(y)
        z=int(z)
        if x=='+':
            print(plus(y,z))
        elif x=='-':
            print(minus(y,z))
        elif x=='/':
            print(div(y,z))
        else:
            print(multi(y,z))
    else:
        print('정수만 입력 가능합니다')

#결과만을 도출하려면 바로 프린트, 결과에 추가해서 도출할거면 result에 담아서 마지막에 print 쓰는게 편할듯
