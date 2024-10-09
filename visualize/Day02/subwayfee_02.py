import csv

f= open('subwayfee.csv', encoding='utf-8-sig')
data= csv.reader(f)
header= next(data)  #한 줄을 읽고 다음 줄로 이동
print(header)
max_rate=0
rate=0

for row in data:
    for i in range(4,8):
        row[i]= int(row[i])
    rate=row[4]/row[6]
    if rate>max_rate:
        max_rate=rate    #최댓값 뽑기 위한 조건
print(max_rate)
f.close()
