#set 자료형 살펴보기
# -여러 가지 종류의 여러 개 데이터를 저장
# 단! 중복 안됨!!!!!!
# -collection타입 데이터 저장시 Tuple
#- 형태: {데1,데2,.....}

#set 생성 
data=[]
data=()
data={}
data=set() #딕션과 형식 같아서 set을 통해 빈 자료 형성 가능
print(f'data의 타입: {type(data)}, data의 수:{len(data)}')

#여러개의 데이터 저장한 set
data={9.34, 'Apple', 10, True, '10'}
print(f'data의 타입: {type(data)}, data의 수:{len(data)}, 데이터:{data}')
#10->int, str이기 떄문에 서로 다른 데이터

data= {1,2,3,(1,)}  #list 사용불가(수정x야함)->tuple사용
#값이 겹칠 경우 하나만 나옴  ---->중복 제거할 때 유용
#tuple 값 하나만 할떄-->(4,)  
print(f'data의 타입: {type(data)}, data의 수:{len(data)}, 데이터:{data}')

#data2= {1,2,3,{1:100}} --->TypeError: unhashable type: 'dict'
#set, dict 또한 변경이 가능하기 때문에 tuple로 감싸서 사용해야함

#set 내장함수
set()   #빈 set
#data={1,2,3} --->set([1,2,3])
data= set({1,2})
print(data, type(data))
##리스트와 같은 자료는 set([리스트데이터]) 와 같이 수동으로 해야함
                    #  ->형변환과 동일한 형태
### 그 외에 일반적은로 data={1,2,3,4...} 으로 사용

data=set('good')
print(data)   #중복된 데이터는 하나만 출력
data=set({'name':'홍길동','age':12})
print(data)   #dic클래스의 경우 키만 출력, 중복된 경우 나중에 입력한
#                  키를 출력
              #dic ===>기본적으로 key우선
data= set((1,2,1,1,2,2))
print(data)    #---->{1, 2}

