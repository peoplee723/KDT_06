#12.1
lux=[490, 334, 550, 18.72]
###뭐가 어떤 능력치(데이터)인지 알기 힘듦

lux={ 'health':490, 'mana':334, 'melee':550, 'amor':18.72}
print(lux)
#SyntaxError: invalid syntax ->문법 오류=='' , () 잘 확인하기!
lux={ 'health':490, 'health':800, 'mana':334, 'melee':550, 'amor':18.72}
print(lux)
##중복될 경우 가장 뒤에 있는 값 사용

x= {100:'hundred', False:0, 3.5:[3.5,3.5]}
print(x)
#key->lsit, dic 사용 불가
#value-> 모두 사용 가능
x={}
print(x,type(x))

lux1=dict(health=490, mana=334, melee=550, amor=18.72)
print(lux1)  #튜플 형태(키=값)의 경우 따옴표x

lux2= dict(zip(['health', 'mana', 'melee','amor'],[ 490, 334, 550, 18.72]))
print(lux2)

lux3= dict([('health', 490), ('mana', 334), ('melee', 550), ('amor', 18.72)])
print(lux3)

lux4=dict({ 'health':490, 'health':800, 'mana':334, 'melee':550, 'amor':18.72})
print(lux4)

#12.2
print(lux['health'])
print(lux['amor'])

#있는 키 값은 교체, 없는 값은 추가
lux['health']= 2037
lux['mana']= 1184
print(lux)

lux['mana_regen']=3.28
print(lux)

print('health' in lux)
#in, not in 으로 키 존재 확인 가능(키:값 형태-->해쉬)

print(len(lux)) #키:값 쌍의 수
print(len({'health':490, 'mana':334, 'melee':550, 'amor':18.72, 'mana_regen':3.28}))

# 12.4
camille={
    'health': 575.6,
    'health_regen': 1.7,
    'mana': 338.8,
    'mana_regen': 1.63,
    'melee': 125,
    'attack_damage': 60,
    'attack_speed': 0.625
    ,'armor': 26,
    'magic_resistance':32.1
   ,'movement_speed': 340
}
print(camille['health'], camille['movement_speed'])

#12.5
"""
data1=input().split
data2=input().split    
data2=list(map(float, data2))  #->값은 실수로 바꾸는 과정 필요
result=list(zip([data1], [data2]))
print(list(data3)[:], type(data3))
"""
# health health_regen mana mana_regen
# 573.6 308.8 600 0.625 35.7 
#[<built-in method split of str object 
# at 0x00000258B94D54F0>] <class 'dict'> ????

#13.1 
x=10
if x==10:                      #=은 할당이므로 수학의 같다는 ==
    print('10입니다.')
    pass   #(미완성일 때 코드 에러 방지 위해 넣음)
x=5
if x==10:
    print('x에 들어있는 숫자는')
print('10입니다.')

#들여쓰기 안하면 조건문과 상관없은 코드가 되어버림
#들여쓰기 권장 4칸 but 일정하기만 하면 상관업음

#13.3
x=15
if x>=10:
    print('10 이상입니다.')
    if x==15:
        print('15입니다.')
    if x==20:
        print('10입니다.')
        # 15, 20조건문이 10조건문에 포함되어 있음
        # 즉 10이상을 만족해야 실행되는 코드들임

# 13.4
# x=int(input())   #인풋으로 입력받은 값은 문자-->수 비교를 위해 변환
# if x>=10:
#     print('10 이상입니다.')
#     if x==20:
#         print('20입니다.')

# 13.6
x=5
if x !=10 :
    print('OK')

13.7
# price=int(input())
# discount=int(input()[4:8])

# if discount:
#     print(price-discount)
# else: 
#     print(price)

# 할인이 존재할 때 가격-할인금액
# 이때, 할인의 형태가Cash0000이므로 숫자만 추출하여 계산

# 14.1
x=5
if x==10:
    print('10입니다.')
else:
    print('10이 아닙니다.')

# 14.2
# if x==10:
#     print('10입니다.')
# else:
#     print('10이 아닙니다.') #-else도 들여쓰기 있어야 함

# 14.3 
if True:
    print('참')
else:
    print('거짓')
if False:
    print('참')
else:
    print('거짓')
if None:
    print('참')
else:
    print('거짓')   #None 도 False로 취급

if 0:
    print('참')       #0만 거짓 나머지 실수는 참
else:
    print('거짓')
if 1:
    print('참')
else:
    print('거짓')
if 0x1F:
    print('참')
else:
    print('거짓')
if 0b1000:
    print('참')
else:
    print('거짓')
if 13.5:
    print('참')
else:
    print('거짓')

if 'Hello':
    print('참')
else:
    print('거짓')
if '':
    print('참')
else:
    print('거짓')    #빈 문자열은 거짓
###거짓 반환--> None, False, 0인 숫자들(n진수 포함), 비어있는 클래스,
#              0, false를 반환하는 bool,len

# 14.4
x=10;y=20

if x== 10 and y==20:
    print('참')
else:
    print('거짓')

if x>0:
    if x<20:
        print('20보다 작은 양수입니다.')
#and 연산자로 if줄일 수 있음
if x>0 and x<20:
    print('20보다 작은 양수입니다.')
#다른 표현
if 0<x<20:
    print('20보다 작은 양수입니다.')

# 14.6
written_test= 75
coding_test= True
if written_test>=80 and coding_test==True:
    print('합격')
else:
    print('불합격')

# 14.7
#점수 입력 받기->점수가 모두0~100점 안에 있는지 검사 
# -> 합격 불합격 검사
# #입력한 점수가 str형태로 저장되기 때문에 map을 통해 int로 변환
# #map 클래스는 계산이 안되기 때문에 list 클래스로 변환

test=list(map(int, input().split()))   
print(type(test),test)
if int(test[0]) in range(101) and int(test[1]) in range(101) and int(test[2]) in range(101) and int(test[3]) in range(101):
    if 100>sum(test)/len(test)>=80:
        print('합격')
    elif sum(test)/len(test)<=80: #else 써도 됨
        print('불합격')
else:
    print('잘못된 점수')


# 15.1
x=20
if x==10:
    print('10입니다.')
elif x==20:
    print('20입니다.')

x=30
if x==10:
    print('10입니다.')
elif x==20:
    print('20입니다.')
else:
    print('10도 20도 아닙니다.')
##elif 앞에 else가 있으면 안됨

# button= int(input())

# if button ==1:
#     print('콜라')
# elif button ==2:
#     print('사이다')
# elif button ==3:
#     print('환타')
# else:
#     print('제공하지 않는 메뉴')    

# #15.3
# x=int(input())
# if 11<=x<=20:
#     print('11~20')
# elif 21<=x<=30:
#     print('21~30')
# else:
#     print('아무것도 해당하지 않음')

# 15.4
age=int(input( ))
balance= 9000

if 7<=age<=12:
    print(balance-650)
elif age<=18:
    print(balance-1050)
elif age>=19:
    print(balance-1250)
    