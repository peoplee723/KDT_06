#10번 입력(숫자데이터)을 받습니다.
#  - 숫자 데이터를 모두 더해서 합계가 30이상이 되면
#  - 10번 입력 안 받았더라도 종료해주세요.
# 30 이상이 되면 종료->10번 입력 받으면 종료 -> 합계 계산

#data=list(map(int,input().split()))

total=0
for d in range(10):
    data=int(input('숫자를 입력하세요'))
    total=total+data
    if total>=30:break
print(f'{total}, 마지막 숫자: {data}')

