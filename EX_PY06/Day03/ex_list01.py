#list 데이터 자료형 살펴보기
#- 여러 개의 데이터를 저장하는 타입
# -다른 종류의 데이터도 함께 저장 가능
# - 형식: [데1,데2,.....]

#나이, 키, 몸무게를 저장
age=16;height=170;weight=70 #-->일일이 저장 귀찮

#여러개의 데이터를 하나의 변수명으로 저장
#리스트
my= [16, 170, 70]
#리스트 내의 원소/요소 접근=>인덱싱
#0번 원소 출력
print(my[0])

#마지막 원소 출력
print(my[2], my[-1])

#리스트 내의 원소/요소 여러개 접근 ==> 슬라이싱
#0,1번 원소 출력
print(my[0:2],my[:2],my[:-1])

#문자열 슬라이싱과 차이점
# 0,1 번 원소 출력
print(f'인덱싱: {my[0], my[1], type(my[0])}')
print(f'슬라이싱: {my[:2], type(my[:2])}')
## 둘다 문자이지만, 리스트는 여러개 뽑을때 
# 리스트에 담겨져 나옴
"""인덱싱: (16, 170, <class 'int'>)
슬라이싱: ([16, 170], <class 'list'>)"""

