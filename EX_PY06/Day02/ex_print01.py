""""내장함수 print() 사용법
- 모니터 즉, 콘솔/터미널에 출력하는 함수
- 문법 : print(아규먼트1,아규먼트2 ...)"""
 

#나이, 이름, 성별을 저장하기
age=100
name='마징가'
gender='남자'
#모니터에 출력하기
print(age)
print(name)
print(gender)

#한줄에 모두 출력하기
print(age,name,gender)
print(99,'홍길동','여자')

#2개의 정수 덧셈 결과 출력하기
num1=2
num2=9
print(num1+num2)

#출력결과 => 2+9=11 화면에 출력
print(num1, '+', num2, '=', num2+num1)
#하지만 일일이 적기 힘듦=> 서식 지정자 사용

#화면 출력 글자를 만들고 그 글자안에 특정결과 출력하는 형식
# -> 글자 내부에 정수결과 넣기 :'%d' %변수명 또는 %수실
# -> 글자 내부에 실수결과 넣기 :'%f' %변수명 또는 %수실
# -> 글자 내부에 글자결과 넣기 :'%f' %변수명 또는 %수실
print('%d + %d = %d' %(num1, num2, num1+num2))

# 9 / 2 = 4.5 화면에 출력
print('%d / %d = %f' %(num2, num1, num2/num1))
print('%s / %s = %s' %(num2, num1, num2/num1))
#구분이 어려운 경우 s로 하면 알아서 변환해줌

# F-string 방식
#=> 형식 : f'  {변수명or수식or데이터}    '
#=> 형식 : F"  {변수명or수식or데이터}    "
print(F'{num1}+{num2} = {num1+num2}')
print(F'{num2}/{num1} = {num2/num1}')