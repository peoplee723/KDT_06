# 매개변수의 개수를 유동적으로
# 0~N개까지 가능 하도록
# 형태: def 함수명(*변수명)  -->0~N개 데이터(가변인자)

# 함수 기능 : 정수 덧셈후 결과 반환
# 이름:add
# 매개 변수:0~N개
# 결과:덧셈 값 result

def add(*nums):
    total=0
    for n in nums:
        total+= n
    return total

# 함수 호출
print(add())    #----> 튜플의 형태로 도출됨
print(add(1,2,3))
print(add(5,6,7,8,9,1,5,6,2))