#dict 자료형 살펴보기

#- dict 자료형 전용의 함수 즉, 메서드(method) 사용
# Dict에서 키만 추출하는 메서드 keys() #
#사용법: 변수명.메서드명()

p1= {'name':'홍길동', 'age':20, 'job':'학생'}
result=p1.keys()
print(f'키 추출: {result}, {type(result)}') #class: 'dict_keys'

#list 형변환 =>list(dic_keys타입)
result=list(result)
print(f'키 추출: {result}, {type(result)}') #class: 'list'

#값/데이터만 추출하는 메서드->values()
result=p1.values()
print(f'값 추출: {result}, {type(result)}') #class: 'dict_values'

#키와 값을 묶어서 추출->items
result=p1.items()
print(f'키와 값 추출: {result}, {type(result)}') 
#class: 'dict_items' + (묶음)의 값은 튜플
result=list(result)
print(f'키와 값 추출: {result}, {type(result)}') 
#class: list