#dict 전용 함수 즉, 메서드

person={'name':'홍길동', 'age':10}

#값 읽어오는 메서드
# get(key, default) ->해당하는 값 없으면 default 반환
                    # ->기본=None
print(person['name'])
# print(person['gender'])  -->KeyError: 'gender'
print(person.get('name'))
print(person.get('gender', '없음')) #---> 값 없어도 오류는 안남
# 메서드 쓰기 싫으면 키 검사하고 반환해야 오류 안남

#키와 값 추가하는 메서드
# 원래 -> person['gender']='남'


#수정 및 업데이트 하는 메서드
# update()                   ->키가 같을 경우 수정
person.update(gender='어린이', job='학생')
print(person)

person.update({'phone':'010', 'birth':'240101'})
print(person)

person.update(**{'weight':100, 'height':170})
#  ** -->weight=100, height=170 식으로 알아서 넣어줌

# msg= "Hello Good Luck"
# alpha=set(msg)
# save={}
# print(alpha)
# for m in alpha:
#     print(m, msg.count(m))
#     save[m]=[msg.count(m)]
# print(save)                

