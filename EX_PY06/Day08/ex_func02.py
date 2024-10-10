# 기능-> 2개의 정수를 덧셈 한 후 결과를 출력하는 함수
# 이름-> add
# 매개변수-> 2개(a,b)   
# 함수 결과-> 없음
def add(num1, num2):
    result=num1+num2
    print(f'{num1}+{num2}={result}')

# 함수사용하기
add(5,8)

# 기능-> 인사 메시지를 출력하는 함수
# 이름-> hello
# 매개변수-> 없음
# 함수 결과-> 없음

def hello():   #->괄호는 필수
    print("Hello~^^")   #리턴, 매개변수는 선택

hello()    #-> 함수기 때문에 () 잊지 말기!
