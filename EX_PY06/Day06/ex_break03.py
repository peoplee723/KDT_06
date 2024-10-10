# 반복문과 break
# 중첩 반복문일 경우의 break는 가장 가까이 있는 반복문만 종료

# 실습-> 단의 숫자만큼만 구구단 출력
# 2단 -> 21, 22/ 3단-> 31,32,33

dan=int(input('원하는 단 입력: '))
for d in range(2,10):                             
    print(f'\n[{d}단],', end=' ')
    for n in range(1,10):
        print(f'{d} * {n} = {d*n:<2}',end=' ')
        if n==d: 
            break
    if d == dan: 
        print()
        break
 #break 없이 만들기
for d in range(2, dan+1):
    for n in range(1,d+1):
        print(f'{d} * {n} = {d*n:<2}',end=' ')