# Dict 자료형 살펴보기
# - 데이터의 의미를 함께 저장하는 자료형
# 형태: {키1:값, 키2:값....키n:값}
# 키는 중복 안됨, 값은 가능
# 데이터 분석 시 파일 데이터 가져올 때 많이 사용

# [Dict 생성]
data={}   #빈 딕트 생성

#사람정보 저장 :이름, 나이, 성별
data={'name':'마징가', 'age':100, 'gender':'남'}
print(f'data => {len(data)}, {type(data)}, {data}')
# 키:값 한쌍이 1개의 데이터

#강아지에 대한 정보-> 품종, 무게, 색상, 성별, 나이....
data={'name':'우유', 'age':3, 'gender': '수', 'kind':'말티즈',
       'color': 'white'}
print(f'data => {len(data)}, {type(data)}, {data}')

#Dict 원소/요소 읽기
# 키를 가지고 값/데이터 읽기
# 형식: 변수명[키]
data={'name':'우유', 'age':3, 'weight':4, 'gender': '수', 'kind':'말티즈', 'color':'white'}

#색상 출력
print(f"색상: {data['color']}")  #따옴표 겹치는거 주의!

#성별, 품좀 출력

print(f'성별: {data["gender"]}, 품종: {data["kind"]}')

#나이 변경

data['age']=6
print(data)

#데이터 삭제
del data["gender"]
print(data)

#새로운 값 추가
data["gender"]="암" 
print(data)  #이미 있는 키의 경우 변경, 없으면 추가하는 형태

