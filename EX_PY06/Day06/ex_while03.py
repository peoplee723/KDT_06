#while문으로 3단 출력
# 
x=1
while x<10:
    print(f'{3} * {x} = {3*x}')
    x= x+1   

# 실습 1~30 범위의 수 중에서 홀수만 출력

x=1
while x<=30:                    #홀수 제한을 while로 넣으면 짝수 
    if x%2:                     #짝수 되자마자 종료됨 ->if사용
        print(x)
    x=x+1


while x<=30:                   #추가되는 숫자를 2로 해서 홀수만 출력
    print(x)
    x=x+2

