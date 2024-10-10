#모듈: 변수, 함수, 클래스가 들어있는 파이썬 파일
#패키지: 동일한 목적의 모듈들을 모은 것
#        여러개의 모듈 파일들 존재
# 모듈 사용법: import 모듈파일명 (확장자제외)
import random as rad #줄이는 건 알아볼 수 있도록 

#임의의 숫자를 생성 추출하기
#10개 생성
for i in range(10):             
    print(int(rad.random()*10),end=" ")
print()
#randint(a,b)   #a<=~<=b
for i in range(10):             
    print(rad.randint(0,1), end="  ")


#실습 로또 프로그램을 만들어주세요
# 1~45 범위에서 중복되지 않는 6개 추출
data=set()


# while len(data)<6:
#     num= rad.randint(1,45)
#     num_set=set([num])
#     data= data.union(num_set)
# print(data)

#rand를 통해 생성한 데이터:int
# set으로 바꾸기 위해서는 iterable해야함 ->
# 생성한 원소를 리스트 또는 str로 변경해면
# set으로 변경 가능해짐
data=rad.randint(1,45)
data=set(str(data))
print(type(data))

while len(data)<6:
    data= data.union([rad.randint(1,45)])
#예시
# lotto=[0,0,0,0,0,0]
# idx=0
# while True:
#     num= rad.randint(1,45)
#     if num not in lotto:
#         lotto[idx]= num
#         idx= idx+1
#     if idx==6:
#         break
# print(lotto)


#set타입의 add()메서드
# lotto=set()
# while len(lotto)<6:
#     num= rad.randint(1,45)
#     lotto.add(num)
# print(lotto)