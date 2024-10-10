#제어문-> 반복문 중단 break
# - 반복을 중단 시키는 조건문과 함께 사용됨

# 실습-> 숫자 데이터의 합계가 30이상이되면 더 이상 합계를 하지 마세요
# 숫자 데이터는 1~50으로 구성됨

nums=range(1,51)
total=0

for n in nums:
    if total>30:
        break           #즉시 반복 종료
    total=total+n
print(f'total = {total}, {1}~{n-1}까지의 합계')

#4개 과목점수가 있습니다.
# 과목점수가 1과목이라도 40이하면 불합격입니다. 
# 4개 과목 평균이 60점 이상이면 합격입니다.
jumsu= [89, 39, 80, 77]
ispass=True
#과목별 40미만 구별
for jum in jumsu:
    if jum<40: 
        print('당신은 과락입니다.')
        ispass=False
        break
    else: 
        print('모든 과목이 40점 이상입니다.')
#평균 구별 ->합격 불합격 처리
if ispass:
    avg=sum(jumsu)/len(jumsu)
    if avg>=60:
        print(f'당신은 {avg}점으로 합격입니다.')
    else:
        print(f'당신은 {avg}점으로 불합격입니다.')
else:
    print(f'당신은 40미만인 과목으로 불합격입니다.')

##For문 한개로 합칠 수 있음... HOW?