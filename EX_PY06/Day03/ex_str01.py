#문자열 str 데이터 다루기

#여러줄 문자열 ==> ''' '''or""" """
msg='''
오늘은

좋은날
기쁜날

'''
print(f'msg= {msg}')

#인덱싱: 문자열 안에 문자 한개 한개를 식별하는 방법
##- 원소/요소 : 문자열 안에 문자 1개
##- 문법: 변수명[인덱스], 문자열데이터[인덱스]
# - 인덱스 종류
# - 왼>>>오: 0, 1, ...
# - 왼<<<오: ....., -2, -1



msg="Good"
msg2=""           #--->
#문자열 전체 출력
print(msg)

#문자열 내 원소 출력
# print(msg2[0])  #--->IndexError: string index out of range
#--->공백도 원소에 포함
print(msg[-1])

#원소/요소의 갯수를 파악해주는 내장함수 len()
#원소/요소를 가지고 있는 데이터타입에만 사용 가능
print(len(msg))

#슬라이싱: 문자열 내에 연속된 요소/원소 추출 방법
#시작 이상~~끝 미만

#제일 마지막 원소/요소만 출력
print(msg[3], msg[len(msg)-1], msg[-1])

data= "Happy New Year 2025! Good Luck"

print(f'인덱스 범위: 0~{len(data)-1}')
print(data[15],data[16],data[17],data[18],data[19], sep='')
print(data[15:20], sep='')

a= 'Life is too short, You need python'
print(a[:4])  #->(양쪽)끝 인덱스(번호)는 생략 가능
print(a[19:35])
print(a[:17])
print(a[:])


#슬라이싱: 문자열 내에 규칙/패턴을 가진 요소/원소 추출 방법
#문법: 변수명[시작:끝+1:간격](간격=몇칸 이동해야 하는지 등)
#시작 이상~~끝 미만

data='123456789'

#짝수만 추출하기
print(data[1], data[3], data[5], data[7])   #귀찮음

#인덱스가 2칸씩 증가하는 규칙
print(data[1: :2])


data="ABC1DEF2GHI3JKL4MNO5PQR6STU"
#문자열에 숫자 요소만 추출해주세요

print(data[3::4])  #:->콜론, ;->세미 콜론
