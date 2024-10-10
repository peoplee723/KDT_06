#tuple 데이터 자료형 살펴보기
# 다양한 종류의 여러 개 데이터를 저장하는 타입
#list와 비슷하지만 추정, 삭제 안됨
#형식: (데1,데2,...)or 데1,데2,...
#데이터 하나일 때는 끝에, 붙이기!!
a='h'
b='h','l'
print(type(a), type(b))
print(b, len(b))

datas=(1,5,7)
print(type(datas), datas)
datas=(1, )
print(datas, type(datas))
print(len(datas))

datas=1, 
print(datas, type(datas))
print(len(datas))

#tuple 데이터의 원소/요소 읽기 
datas=11,22,33,44,55,

#2번 요소 읽기
print(datas[2], datas[-3])

#1,2,3번 요소 읽기(슬라이싱)
print(datas[:3])

#요소/원소 수정 및 삭제(변경) 불가!
#마지막 원소를 'a'로 변경
#datas[-1]='a'
# ->TypeError: 'tuple' object does not 
#               support item assignment

#마지막 원소를 삭제해줘
#del datas[-1]
#->TypeError: 'tuple' object doesn't support item deletion

#국가코드, 지역번호 등은 시간이 지나도 변경되지 않음

#튜플 데이터의 원소/요소 변경 ->형변환
birthday=(2024,1,1)
#1월 ->3월로 변경하기
birthday=list(birthday)  #형변환
birthday[1]=3            #값 수정
birthday=tuple(birthday) #형변환
print(birthday)
