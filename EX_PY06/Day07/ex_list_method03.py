# 요소 순서 제어 메서드
import random as rad
datas=[]
rad.seed(10)    #동일한 랜덤 숫자 추출을 위한 기준점
for i in range(10):
    datas.append(rad.randint(1,100))

print(f'{len(datas)}개, {datas}')

#0번->-1번, -1->0번으로 위치 변경
# reverse
datas.reverse()
print(datas,len(datas))

#요소 크기를 비교해서 정렬해주는 메서드 
# sort()   기본=오름차순

datas.sort(reverse=True)
print(datas, len(datas))

#리스트에서 요소를 꺼내는 메소드
# pop  ->리스트에서 요소가 삭제됨
#        pop(인덱스)->특정 인덱스의 원소 꺼냄
value=datas.pop()         ##기본=제일 마지박 원소
print(f'vlalue: {value} - {len(datas)}개, {datas}')

#리스트 확장 시켜주는 메서드
# extend()
# list
datas.extend([11,22,33])  #맨 끝에 추가
print(f'{len(datas)}개, {datas}')
# tuple
datas.extend((555,777))
print(f'{len(datas)}개, {datas}')
# str
datas.extend(('Good'))
print(f'{len(datas)}개, {datas}')
# set
datas.extend({555,777, 555, 777})
print(f'{len(datas)}개, {datas}')
# dic(key만 들어감)
datas.extend({555:000,'가나다':'까나따'})
print(f'{len(datas)}개, {datas}')

#모든 원소 삭제 메서드
# clear()
datas.clear()
print(f'{len(datas)}개, {datas}')
