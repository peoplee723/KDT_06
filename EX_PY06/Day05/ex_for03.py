##실습-> 출력하고 싶은 단을 입력받아서
#       해당 단의 구구단을 출력하세요
# 예시-> 2*1=2~~~2*9=18
#2-9단 1-9
#data=int(input('계산할 단을 입력하세요: '))
data2=[1,2,3,4,5,6,7,8,9]  ##range(1,10)써도 됨
for i in data2:
    print(f'{data}*{(i)}= {i*(data)}')
