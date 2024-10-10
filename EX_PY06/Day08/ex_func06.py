# 디폴트 매개변수 함수
# 함수 호출시 데이터가 전달되지 않는 경우 미리 지정된 값으로 처리합니다
# 형식 def함수명(변수1, 2, 3... 매개변수=0)

def add(num1=0,num2=0):
    return num1+num2

print(add())
print(add(5))
print(add(4,5))


# 기능: 회원가입 기능 함수
# 이름: register
# 변수: id,pw,gender
        # 성별 기본값=남
# 결과:'ooo님 가입을 환영합니다' (str)

# def register(gender='남',id , pw):  ->순서가 중요!
def register(id , pw, gender='남'): 
      return f'{id}-{gender}님 가입을 환영합니다'
#-->기본적으로 왼쪽에서 오른쪽으로 읽음, 하지만, 기본값을 왼쪽에 넣으면 입력받은 값이 기본값인지, 새 값을 할당받는지 알 수 없음
# ex-> sorted([11,22], reverse=True)
print( register('kk', 'k123','여'))

def test(n1,n2, *nums):   #->어디서 어디까지가 nums인지 모르기 때문에 맨오른쪽에 배치
     print(n1, n2, nums)

print(1,2,3,4,5,6,7,8,9)
     