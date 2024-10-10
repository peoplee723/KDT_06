# 중첩조건문
# 조건문에 조건문이 존재하는 제어문
# 형식
#   if조건식
#       실행코드
#       if조건식
#           실행코드 .....

#실습- 숫자가 음이 아닌 정수와 음수 구분하기
#  음이 아닌 정수 중에 0과 양수 구분하기
# 음이 아닌 정수/// 0>=
# 음이 아닌 정수에서 0과 0이 아닌 수 구분
#data=int(input('정수를 입력하시오.'))
num=8
#중첩조건문
if num>=0:
    print(f'{num}은 음이 아닌 정수')
    if num>0:
        print(f'{num}은 양수')
    else:
        print(f'{num}은 영')
else:
    print(f'{num}은 음수')

#다중조건문
if num>0:
    print(f'{num}은 양수')
elif num<0:
    print(f'{num}은 음수')
else:
    print(f'{num}은 영')
#보기에는 elif가 좋음(가독성) but, 중첩조건 써야할 상황이 생김

#동네이름 데이터에서 입력 받은 동네이름 해당 여부
city= ['대구', '부산', '울산']
data='마산'

if data in city:   # ==대구, ==울산, .... 일일이 안적어도 됨
    print(F'{data}는 광역시입니다.')
else:
    print(F'{data}는 광역시가 아닙니다.')
