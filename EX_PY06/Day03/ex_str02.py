#문자열 str데이터 다루기
# -문자요소 연산 : 산술,비교, 멤버 연산

#(1) 산술 연산
data1='Happy'
data2='Year'

#덧셈(+)연산: str+str= str연결
print(f'{data1}+{data2} =>{data1+data2}')
# print(f'{data1}+{10} => {data1+10}')
#TypeError: can only concatenate str (not "int") to str
#문자열 끼리만 연산이 가능함
print(f'{data1}+{10} => {data1+str(10)}')

#뺄셈(-) 연산
# print(f'{data1}-{data2} => {data1-data2}')
# TypeError: unsupported operand type(s) for -: 'str' and 'str'
#지원하지 않는 연산 ->미지원

#곱셈(*) 연산 ->숫자만큼 str 반복연결
#print(f'{data1}*{data2} => {data1*data2}')
#TypeError: can't multiply sequence by non-int of type 'str'

print(f'{data1}*{3} => {data1*3}')
print(f'{data1}*{3} => {3*data1}')
#나눗셈 안됨

#2. 멤버 연산
# 요소/원소 in 문자열     =>존재하면 True, 아니면 False
# 요소/원소 not in 문자열 =>존재한하면 True, 아니면 False

print(f'h in {data1} : {"h" in data1}')
print(f'h not in {data1} : {"h" not in data1}')

#print(3 in 123)
#TypeError: argument of type 'int' is not iterable
#원소/요소를 가진 데이터타입에만 사용 가능!
print(str(3) in str(123))


