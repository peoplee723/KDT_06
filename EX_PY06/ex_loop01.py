#1. out 5 in 5
for i in range(5):
    for j in range(5):
        print(f'j:{j}', end=' ')
    print(f'i:{i}\\n')

#19.3 한줄로 나타낼 수도 있음
for j in range(5):
    print('*'*j)

for j in range(5):
    for i in range(i+1):
        print('*'*i)

