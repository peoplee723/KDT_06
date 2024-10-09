import csv
 
reusult= []
total_number= 0
with open('subwaytime.csv', encoding='utf-8-sig') as f:
    data= csv.reader(f)
    next(data)
    next(data)
    for row in data:
        row[4:]= map(int, row[4:])
        total_number+=row[4]
        reusult.append(row[4])

print(f'총 지하철 역의 수: {len(reusult)}')
print(f'새벽 4시 승차인원: {total_number:,}')