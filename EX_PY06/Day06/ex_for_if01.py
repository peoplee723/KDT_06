#제어문 -> 반복문과 조건문 혼합

#실습
# 숫자 1~50까지의 데이터가 있습니다.
# 해당 데이터에서 3의 배수는 제곱을 하고, ->%3==0인 수
# 나머지 숫자는 그대로 해서 모두 더해서 합계를 출력하세요

nums=range(51)
total=0
for i in nums:
    if i%3:
        total=total+i                #각각의 수가 int이므로 합연산자로 합계 만들 수 있음
    else:
        total=total+i*i              #3의 배수 여부 검사
print(total)

#실습
# 메시지에서 알파벳과 숫자를 구분해서 처리합니다.
# 알파벳은 ★, 숫자는 ♡로 변경해서 출력해주세요.

msg="Good 2024"  #원소 가져오기++ 구분하기 ++ 저장
msg2=''
for m in msg:
    if ('a'<=m<='z') or ('A'<=m<='Z'):
        print('★', end='')
        msg2=msg2+'★'
    elif '0'<=m<='9':
        print('♡', end='')
        msg2=msg2+'♡'
    else:
        print(m,end='')
        msg2=msg2+m
print(msg2)            #변경된 것을 저장하고 싶으면 새로운 변수에 추가