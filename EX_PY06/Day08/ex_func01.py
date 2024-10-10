# 사용자 정의 함수
# 함수 기능->이름->매개변수->결과 순으로 정의
# 기능-> 2개의 정수를 덧셈 한 후 결과를 반환하는 함수
# 이름-> add
# 매개변수-> 2개(a,b)   =>변수의 속성을 알 수 있도록 만들기
# 함수 결과-> 덧셈 계산 값 result

def add(num1, num2):
    result=num1+num2
    return result

# 함수 사용하기, 즉 함수호출
value=add(10,20)
print(value)

# value=add(10)     #->함수의 매개변수 개수와 다름
# print(value)            #ERROR
