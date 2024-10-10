# collect 자료형에 공통적인 부분 살펴보기
# 여러개의 변수에 데이터 저장
name=['홍길동']
age=12
job='의적'
gender='남'
#  -->패킹 방식

#변수명= tuple타입 --->언패킹 방식
name, age, job, gender= '홍길동', 12, '의적', '남'
print(name, age, job, gender)

# name, age= '홍길동', 12, '의적', '남'
# print(name, age, job, gender)
# -->ValueError: too many values to unpack (expected 2)
#변수명 수와 데이터 수가 서로 매치되야함
# 그럼에도 해야할 때
name, age, _, _= '홍길동', 12, '의적', '남'
print(name, age, _)
# 의미없는 변수 --> _(underscore)로 표현 ->출력시 마지막 값 출력

#리스트도 언패킹 가능
jumsu=[100,99]
kor, math= [100, 99]
print(jumsu, kor, math)

#dic도 가능 (언패킹할 경우 key값 도출)
person={'name':'박', 'age':11}
k1, k2= {'name':'박', 'age':11}
print(person, k1, k2)

#생성자(constructor) 함수: 타입명과 동일한 이름의 함수
#int, float, str, bool, list, tuple, dict, set
#map, range

# 기본 데이터 타입
num=int(10)            #-> num=10
fnum=float(10.2)        #-> fnum=10.2
msg=str('Good')         #msg='Good'
isok=bool(False)         #isok=False

#collection 데이터 타입
lnums= list([1,2,3,4])   #->lnums=[1,2,3,4]
tnums= tuple((3,6,9))    #->tnums=(3,6,9)
ds= dict({'d1':10, 'd2':30})   #ds={'d1':10, 'd2'=30}          
s=set({1,1,3,3,5})        #s={1,1,3,3,5}
##오른쪽으로 적어도 파이썬이 왼쪽으로 적은 것 처럼 처리해줌

#타입 변경 => 형변환
# dict 자료형은 다른 자료형과 달리 데이터 형태가 다름
# dict-> 키:값
#ds=dict([1,2,3])
# TypeError: cannot convert dictionary update sequence element
 #           0 to a sequence

#때문에 키1=값, 키2=값.... 의 형태로 만들어 줘야 함
ds= dict(n1=1, n2=2, n3=3)   #이때 ''또는""넣으면 안됨
print(ds)                    #  (값은 문자일 때 넣기)
                             #또한, key는 str만 가능
ds=dict([('name', '마징가'), ('age', 12)])
print(ds)
#  리스트지만 리스트 안이 튜플(키와 값의 형태)로 되있기 때문에 가능

# 내장함수 : zip() 같은 인덱스의 요소끼리 묶어줌
l1= ['name', 'age', 'gender']
l2= ['마징가', 12, '남']
l3= [False, True, True]
print(list(zip(l1,l2,l3)))   ##class =zip

ds=dict(zip(l1,l2))
print(ds)

