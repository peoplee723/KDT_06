#리스트 전용의 함수, 즉 메서드(Method)
# 리스트의 원소/요소를 제어하기 위한 함수들

import random as rad

#요소 인덱스를 반환하는 메서드 
# index(데이터, 찾기시작하는인덱스)
#                                  
datas=[1,2,3,4,5,3,7,8,3]
idx=datas.index(8)
print(idx)
#존재하지 않는 데이터의 경우 ERROR
if 0 in datas:
    idx=datas.index(3)   
    print(f'0의 인덱스: {idx}')
else:
    print('0은 존재하지 않는 데이터입니다.')

if 3 in datas:
    idx=datas.index(3)
    print(f'첫번째 3의 인덱스: {idx}')
    idx=datas.index(3,idx+1)
    print(f'두번째 3의 인덱스: {idx}')
    idx=datas.index(3,idx+1)
    print(f'세번째 3의 인덱스: {idx}')

#데이터가 몇개 존재하는지 갯수 파악하는 메서드: 
# count(data)
cnt=datas.count(3)  #--> 3이 몇개있는지
print(f'3의 개수: {cnt}개')
idx=0
for i in range(cnt):
    idx=datas.index(3,idx if not i else idx+1)
    print(f'{i+1}번째 3의 인덱스: {idx}')

# 메서드 - 요소 추가 메서드 
# append(데이터)
datas=[1,3,5]
datas.append(100)   #제일 마지막에 원소 추가
datas.append(100)
print(f'datas 개수: {len(datas)}, {datas}')

#요소 추가 메서드
# insert(인덱스, 데이터)   #원하는 위치에 추가
datas.insert(0,300)       #다른 데이터는 뒤로 밀림
print(f'datas 개수: {len(datas)}, {datas}')

# 실습 데이터 ->임의의 정수 10개로 구성된 리스트
data=[]

for i in range(10):
    data.append(rad.randint(1,100))

print(data)

#요소 삭제 메서드
# remove(데이터)
# [300, 1, 3, 5, 100, 100]
datas.remove(100)   #가장 앞에 있는거 하나 지움
print(datas,len(datas))# 존재하지 않는 데이터 삭제->ERROR   
for cnt in range(datas.count(300)):
    datas.remove(300)
    print(datas,len(datas))   

