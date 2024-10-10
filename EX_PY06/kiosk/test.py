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

"""
n층->
1     3번쨰칸은 무조건 *   
3     양옆으로 1씩 증가 (층마다 2씩 증가)
5
"""
data=5

data=int(data)
#->j 1,3,5,7,9...
for j in range(1,data+1):
    print(' '*(data-j), end='')
    if data %2:
        print('*'*(2*j-1))
