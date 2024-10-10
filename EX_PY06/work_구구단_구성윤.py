
#구구단 for문 하나

data2=list(map(int, range(20,100)))

for i in data2:
    if not i%10:
        print(f'{i//10}단')
    if i%10:
        print(f'{i//10} * {i%10} = {(i//10)*(i%10)}')




#구구단 옆으로
data2=list(map(int, range(1,10)))
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