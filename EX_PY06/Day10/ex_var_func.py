# 함수와 변수 - 지역/전역 변수
total=100
# 전역변수(Golbal Variable)
# 파일 내에 존재, 모든 곳에 사용 가능
# 프로그램 실행 시 메모리 존재
# 프로그램 종료 시 메모리에서 삭제

name='홍길동'

# 전역변수(Golbal Variable)
# 함수 내에 존재,  함수에서만 사용 가능
# 함수 실행 시 메모리 존재
# 함수 종료 시 메모리에서 삭제


# 함수 기능: 여러개개의 정수를 덧셈한 후 결과를 반환하는 함수
# 함수이름: addInt
# 매개변수: 0~개(가변인자) *nums
# 함수 결과: 정수 result

def addInt(*nums):
    total=0
    for n in nums:
        total+=1
        return total
    

def muitInt(*nums):
    for n in nums:
        total*=n
        return total   

def muitInt2(*nums):
    #전역변수의 값을 변경할 결우 그냥 사용 안됨(변경 안하면 그냥 사용 가능)
    global total        #-> global(전역변수명) 을 통해 값 변경 가능
    for n in nums:
        total *= n
        return total   


# 함수 호출                    
result1=addInt(1)
print(f'result1 : {result1}')

result2=addInt(5)
print(f'result2 : {result2}')

print(f'result2 = {result2}')
print(f'total = {total}')
