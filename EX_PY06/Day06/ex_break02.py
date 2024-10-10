# 반복문과 break
# 중첩 반복문일 경우의 break는 가장 가까이 있는 반복문만 종료

#중첩 반복문 -> 내부 반복문 종료 시 외부 반복문 종료
#내부 반복문 종료 여부를 변수에 저장->내부 종료시 외부 종료되도록
#dan=int(input('원하는 단 입력: '))
isbreak=False
for d in range(2,10):
    print(f'\n[{d}단],', end=' ')
    for n in range(1,10):
        print(f'{d} * {n} = {d*n:<2}',end=' ')
        if n==d:
            isbreak=True 
            break
    if isbreak: break            #if n ==d: break 도 가능-->
                                 #하지만 조건이 길어지면 변수선언하는게 편함