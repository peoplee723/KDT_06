import csv

f= open('daegu.csv', 'r', encoding='utf-8')
data= csv.reader(f, delimiter=',')
count=0

for row in data:
    if count> 5:
        break
    else:
        print(row)
    count+=1
f.close()

# ufeff 제거
fin= open('daegu.csv', 'r', encoding='utf-8-sig')
data=csv.reader(fin, delimiter=',')

# newline='' 제거
# fout= open('daegu-utf8.csv', 'w', newline='', encoding='utf-8-sig')
# wr= csv.writer(fout)
# for row in data:
#     for i in range(len(row)):
#         row[i]= row[i].replace('\t', '')
#     print(row)
#     wr.writerow(row)
# fin.close()
# fout.close()
# print('파일 저장 완료')

#대구 최저, 최고 기온 날짜와 온도 구하기 예제

# def get_minmax_temp(data):
#     '''
#     최고 기온 및 최고 기온의 날짜 구하기
#     '''
#     header= next(data)

#     min_temp= 100 #최저 기온 값 저장할 변수 초기화
#     min_date= ''  #최저 기온 날짜 변수 초기화

#     max_temp= -999
#     max_date= ''

#     for row in data:     #빈 열 생성, 실수로 변환
#         if row[3]== '':
#             row[3]= 100
#         row[3]= float(row[3])

#         if row[4] =='':
#             row[4] = -999
#         row[4] = float(row[4])

#         #최저 기온 계산 
#         if row[3] < min_temp:
#             min_temp = row[3]
#             min_date = row[0]
#             print(f'최저기온 업데이트: {min_date}, {min_temp}')
#         #최고 기온 계산
#         if row[4] > max_temp:
#             max_temp= row[4]
#             max_date= row[0]
#             print(f'최고기온 업데이트: {max_date}, {max_temp}')
#     print('-'*50)
#     print(f'대구 최저 기온 날짜: {min_date}, 온도: {min_temp}')
#     print(f'대구 최고 기온 날짜: {max_date}, 온도: {max_temp}')

# def main():
#     f= open('daegu-utf8.csv', encoding= 'utf-8-sig')
#     data= csv.reader(f)
#     get_minmax_temp(data)
#     f.close()
    
# main()

import matplotlib.pyplot as plt
import koreanize_matplotlib

# f=open('daegu-utf8.csv', encoding='utf-8-sig')
# data= csv.reader(f)
# next(data)
# result= []

# for row in data:
#     if row[-1] !='':
#         result.append(float(row[-1]))
# f.close()

# plt.figure(figsize=(10,2))
# plt.hist(result, bins=500, color='b')
# plt.rc('font', family='Malgun Gothic')

# plt.rcParams['axes.unicode_minus'] =False
# plt.title('1970년 부터 2024년까지 대구 기온 히스토그램')
# plt.show()


# #월 데이터만 꺼내서 시각화하기
# # 1. 파일 오픈
# f= open('daegu-utf8.csv', encoding='utf-8-sig')
# data= csv.reader(f)
# next(data)
# aug=[]
# # 2. 8월만 검사해서 최고기온 꺼내기(날짜 정보를 잘라서 8월 인덱싱+최고기온 뽑아오기)
# for row in data:
#     if row[0] !='' and row[4] != '':
#         month= row[0].split('-')[1]
#         if month =='08':
#             aug.append(float(row[-1]))
# f.close()
# plt.hist(aug, bins=100, color='tomato')
# plt.title('대구 8월의 최고 기온 히스토그램')
# plt.xlabel('Temperature')
# plt.ylabel('Counts')
# plt.show()

# def draw_graph_on_date(month, day):
#     f=open('daegu-utf8.csv', encoding='utf-8-sig')
#     data= csv.reader(f)
#     next(data)
#     result=[]
#     for row in data:
#         if row[-1] !='':
#             date_string= row[0].split('-')
#             if date_string[1] == month and date_string[2]==day:
#                 result.append(float(row[-1]))
#     f.close()
#     plt.figure(figsize=(15,2))
#     plt.plot(result, 'royalblue')
#     plt.title(f'매년 {month}월 {day}일 최고 기온 변화')
#     plt.show()

# month, date= input('날짜(월 일)를 입력하게요: ').split()
# draw_graph_on_date(month, date)
def file_open(name, encode):
    f=open('daegu-utf8.csv', encoding='utf-8-sig')
    data= csv.reader(f)
    next(data)

