# 형변환 / 타입캐스팅#
#- 자료형을 다른 종류의 자료형으로 변경
"""-종류
     -자동/묵시적 형변환 : 컴퓨터가 진행
     -수동/명시적 형변환 : 개발자가 진행"""


age=20.7
print(int(age))#다시 저장하지 않으면 변환 결과 적용 안됨
print(age)
age=int(age)
print(age)
print(type(age))
#정수를 실수로 변환
age=float(age)
print(age)
print(type(age))
#실수를 문자열로 변환
age=str(age)
print(age)
print(type(age))

p=1
print(type(p))
o=3
print(type(p/o))
m=p/o
print(type(m*3))
print(m*3)
