#연산자와 내장함수

person= {'name':'홍길동', 'age':20, 'job':'학생'}
dog= {'name':'우유', 'age':3, 'gender': '수', 
      'kind':'말티즈', 'color': 'white'}

#연산자
#산술 연산 안됨
#person+dog (X)

#멤버 연산자 : in, not in
#key
print('name' in dog)

#value   dict타입에서는 key만 멤버 연산자로 확인
print('말티즈' in dog)
print( 20 in person)

#value 추출
print('말티즈' in dog.values())
print( 20 in person.values())

#내장함수
#원소/요소 개수 확인: len()
print(f'dog의 요소 개수: {len(dog)}개')
print(f'person의 요소 개수: {len(person)}개')

#원소/요소 정렬 
#키만 정렬#
print(f'dog의 오름차순 정렬: {sorted(dog)}개')
print(f'person의 내림차순 정렬: {sorted(person, reverse=True)}개')

#print(f'dog의 오름차순 정렬: {sorted(dog.values())}개')
#TypeError:'<' not supported between instances of 'int' and 'str'
#타입이 다르면 정렬이 안됨
jumsu={'국어':90, '수학':178, '체육':100}

#동일한 타입에서 정렬 가능함
print(f'jumsu값의 오름차순 정렬: {sorted(jumsu.values())}')
print(f'jumsu값의 오름차순 정렬: {sorted(jumsu)}')
"""jumsu값의 오름차순 정렬: [90, 100, 178]
jumsu값의 오름차순 정렬: ['국어', '수학', '체육']"""
#==>각자 정렬됨, 매칭x

print(f'jumsu값의 오름차순 정렬: {sorted(jumsu.items())}')
"""jumsu값의 오름차순 정렬: [('국어', 90), 
                           ('수학', 178), ('체육', 100)]"""
#==>매칭은 됬지만 점수(값)이 아닌 키 기준으로 정렬됨

print(f'jumsu값의 오름차순 정렬: {sorted(jumsu.items(), 
                                 key=lambda x:x[1])}')
#==>  기존 국어[0]가 아닌 90[1]을 기준으로 정렬

print(type(jumsu.items()))
 
