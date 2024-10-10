#실습-> 2단~9단까지 모두 출력
data=(range(2,10))
data2=list(range(1,10))

# for n in data:
#     print(f'{n}단')
#     for i in data2:
#         print(f'{n} * {i} = {n*i}')
#n=1, i=1, i=2.... i=9 끝나면 다시 위로
# n=2, i=1, i=2... i=9 .... n=9, i=9가 나오면 끝
#print()와 for문이 같은 줄에 있으니까 순서대로 도출

#몫이 2이고 나머지가 1,2,3,4,5,6,7,8,9
data2=list(map(int, range(20,100)))
####몫이 0이면 20,30,40,50... 단을 구분하는데 사용할 수 있음
####나머지가 존재하면 21,22,23,24,25,26,27,28,29->
#                10으로 나눴을때 몫*나머지로 사용 가능
for i in data2:
    if not i%10:
        print(f'{i//10}단')
    if i%10:
        print(f'{i//10} * {i%10} = {(i//10)*(i%10)}')

data2=list(map(int, range(1,10)))
##후보 1
for j in data2:
    if j:
        for i in list(map(int, range(2,10))):
            if i<=5:
                print(f'{i} * {j} = {(j)*i:<2}', end='   ')
        print()
print()
for j in data2:

    for i in list(map(int, range(2,10))):
        if i>=6:
            print(f'{i} * {j} = {(j)*i:<2}', end='   ')
    print()

##후보2

for j in data2:
    
    for i in list(map(int, range(2,10))):
        if i<=5:
            print(f'{i} * {j} = {(j)*i:<2}', end='   ')

    
            
    print()



#데이터:빈칸채울 문자, 정렬 ,칸수
# num=2
# print( f'{num:>3}입니다.')       # >오른쪽, ^가운데, <왼쪽 정렬
# print( f'{num:0^3}입니다.')      #빈칸 채울 문자 공백->빈 공간 생성 
# print( f'{444:ㅣ<3}입니다.')