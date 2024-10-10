#실습1. 글자를 입력 받습니다
    #   입력받은 글자의 코드값을 출력
    #   합니다

##고려해야할 것
# 한글자의 코드값을 반환하는 코드 짜기
#여러글자인 경우, 숫자인 경우 설명하는 코드 짜기



##코드값 변환 -->ord()
# data=(input("글자를 입력하세요(a~z, A~Z)"))

# if len(data) and ('a'<= data<='z' or 'A'<= data<='Z'):
#     print(f'{data}의 코드값: {ord(data)}')
# else:
#     print("1개의 알파벳 문자만 입력해야 합니다.\n입력된 데이터를 확인하세요")

#if, 여러글자인 경우-> list(map(ord, data))
#                              함수  데이터 ->map클래스 리스트로 변환

#실습 2 점수를 입력 받은 후 학점을 출력합니다
# 학점: A+, A, A-, B+, B, B-, C+, C, C-, D+, D, D-, F
#  + -> 100~96
#  A -> 95
#  - -> 90~94 ....

score= int(input("점수를 입력하세요"))

if 0<score>100: print("잘못된 점수입니다") 
elif score>=96:
    print("A+")
elif score==95:
    print("A")
elif 90<=score:
    print("A-")
elif score>=86:
    print("B+")
elif score==85:         ###실행코드가 한줄일때는 들여쓰기 안하고
    print("B")            # 띄어쓰기만 해도 됨
elif 80<=score:
    print("B-")
if score>=76:
    print("C+")
elif score==75:
    print("C")
elif 70<=score:
    print("C-")
elif score>=66:
    print("D+")
elif score==65:
    print("D")
elif 60<=score:
    print("D-")
else:
    print("F")

#만약 print 안의 내용이 길면 등급을 부여하고
# 마지막에 print(점수, 등급)도 가능

#또는 몫, 나머지 연산자를 사용해서 만들 수 있음
# 10으로 나눈 몫으로 ABC, 나머지로 +-0 구분