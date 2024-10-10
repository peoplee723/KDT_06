#조건부 표현식--> 조건이 많은 경우

#실습-> 숫자가 양수, 영, 음수 인지 판별
num=9
if num>0:
    print('양수')
elif num<0:
    print('음수')
else:
    print('영')

result='양수' if num>0 else '음수' if num>0 else '영'
#       참일떄 if 조건 else (앞에껀 거짓이고 뒤어껀
#  00) 참일때 if 조건 else ... else 거짓
#한줄로 쓰긴 편하지만 가독성이 떨어짐
