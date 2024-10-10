##실습 숫자를 입력 받아서 음이 아닌 정수와 음수 구분하기

data= int(input("정수를 입력하시오:"))
nums=['음이 아닌 정수', '음수']

if data>=0:
    print(f' 숫자 {data}는 {nums[0]} 입니다.')
else:
    print(f' 숫자 {data}는 {nums[1]} 입니다.')


#실습- 점수를 입력 받아서 합격과 불합격 출력
# - 합격: 60점 이상
test= int(input("점수를 입력하세요"))

if test>=60:
    print(f'당신은 합격입니다.')
else:
    print(f'당신은 불합격입니다.')


#실습 점수를 입력 받아서 학점 출력
# 학점: A,B,C,D,F
score= int(input('점수를 입력하세요'))
grade=('A','B','C','D','F')

if score>=90:
    print(f'당신의 학점은 {grade[0]}입니다.')
elif score>=80:
    print(f'당신의 학점은 {grade[1]}입니다.')
elif score>=70:
    print(f'당신의 학점은 {grade[2]}입니다.')
elif score>=60:
    print(f'당신의 학점은 {grade[3]}입니다.')
else: 
    print(f'당신의 학점은 {grade[4]}입니다.')


