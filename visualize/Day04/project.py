import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate
import koreanize_matplotlib
import seaborn as sns

import pandas as pd
import numpy as np


def show_data(Dname):
    print(tabulate(Dname, headers='key', tablefmt='pretty'))

cuttle_fish= pd.read_excel('갑오징어.xlsx')

wt_2014 = pd.read_csv('water_temp_2014.csv', encoding='euc_kr')
wt_2015 = pd.read_csv('water_temp_2015.csv', encoding='euc_kr')
wt_2016 = pd.read_csv('water_temp_2016.csv', encoding='euc_kr')
wt_2017 = pd.read_csv('water_temp_2017.csv', encoding='euc_kr')
wt_2018 = pd.read_csv('water_temp_2018.csv', encoding='euc_kr')
wt_2019 = pd.read_csv('water_temp_2019.csv', encoding='euc_kr')
wt_2020 = pd.read_csv('water_temp_2020.csv', encoding='euc_kr')
wt_2021 = pd.read_csv('water_temp_2021.csv', encoding='euc_kr')
wt_2022 = pd.read_csv('water_temp_2022.csv', encoding='euc_kr')
wt_2023 = pd.read_csv('water_temp_2023.csv', encoding='euc_kr')

show_data(cuttle_fish)
print(cuttle_fish.columns)


print(cuttle_fish.dtypes)   #열 제거를 위해 컬럼 제목 수정
cuttle_fish.columns=['시점', '갑오징어류_1_수', '갑오징어류_1_금액', '살오징어_수', '살오징어_금액', '갑오징어류_2_수', 
                     '갑오징어류_2_금액', '오징어류_수', '오징어류_금액', '합계_수', '합계_금액' ]
show_data(cuttle_fish)
cuttle_fish.drop(index=0 ,inplace=True)  #행 제거
show_data(cuttle_fish)
change_list= [10, 22, 34, 46, 58, 70, 82, 94, 106, 118]
change_year= ['2014.01','2015.01','2016.01','2017.01','2018.01','2019.01','2020.01','2021.01','2022.01','2023.01']




print(cuttle_fish)

# plt.plot(cuttle_fish['합계_수'])
# plt.ylabel('어획량(톤)')
# plt.xlabel('연도')
# plt.xticks()
# plt.show()


temp_list = [wt_2014, wt_2015, wt_2016, wt_2017, wt_2018,
             wt_2019, wt_2020, wt_2021, wt_2022, wt_2023]

def make_month_temp(data):
    list_data = []
    for i in range(len(data)):
        list_data.append(data['일시'][i][:7])
    data['일시'] = list_data
    data

    month_temp = []
    for i in sorted(data['일시'].value_counts().index):
        if data.columns[8] == '수온(°C)':
            month_temp.append(data[data['일시'] == i]['수온(°C)'].mean())
        else:
            month_temp.append(data[data['일시'] == i]['평균 수온(°C)'].mean())
    return month_temp

temp=[]
temp_2014= make_month_temp(wt_2014)
temp_2015= make_month_temp(wt_2015)
temp_2016= make_month_temp(wt_2016)
temp_2017= make_month_temp(wt_2017)
temp_2018= make_month_temp(wt_2018)
temp_2019= make_month_temp(wt_2019)
temp_2020= make_month_temp(wt_2020)
temp_2021= make_month_temp(wt_2021)
temp_2022= make_month_temp(wt_2022)
temp_2023= make_month_temp(wt_2023)
temp_list=[temp_2014, temp_2015, temp_2016, temp_2017, temp_2018, temp_2019, temp_2020, temp_2021, temp_2022, temp_2023]
for list in temp_list:
    temp.extend(list)
cuttle_fish['수온']=temp  #수온 열 추가
cuttle_fish['연']=cuttle_fish['시점'].astype(int) #연 열 추가
cuttle_fish['연'].astype(str)

month= [1,2,3,4,5,6,7,8,9,10,11,12]   #월 열 추가
month_list=[]
for i in range(10):
    month_list.extend(month)
cuttle_fish['월']= month_list
cuttle_fish['월'].astype(str)

cuttle_fish.drop(columns='시점', inplace=True)# 시점 열 삭제

cuttle_fish['시점']= cuttle_fish['연'].astype(str)+ '.' + cuttle_fish['월'].astype(str) #datetime 시점 생성
# pd.to_datetime(cuttle_fish['시점'], dayfirst=)


# 특정 월 그래프 그리는 함수
def draw_graph(month, colname):
    filter= cuttle_fish['월']==month
    x=cuttle_fish[filter]['연']
    y=cuttle_fish[filter][colname]
    plt.plot(x, y)
    plt.xlabel('연도')
    plt.ylabel(colname)
    plt.title(str(month)+'월')
    plt.savefig('img/'+ (str(month)+'월')+ colname + '.png', dpi=100)
    plt.show()



# 1. 전체 수확량 그래프
# plt.bar(cuttle_fish['시점'], cuttle_fish['합계_수'])
# plt.xticks(rotation=80 ) 
# plt.show()



# 전체 온도 변화 그래프   ->의미 없음
# plt.plot(cuttle_fish['시점'], cuttle_fish['수온'])
# plt.show()






# 2. 연도별 총수확량 그래프


#월별 수확량 변화 그래프 (중첩)

# for i in range(1,13):
#     month_cuttle_total=[]
#     year= range(2014,2024)
#     filter= cuttle_fish['월']==i
#     month_cuttle_total.append(cuttle_fish[filter].sum)
#     x=[]
#     y=[]
#     x=cuttle_fish[filter]['연']
#     y=cuttle_fish[filter]['합계_수']
#     plt.plot(x, y)
#     plt.xlabel('연도')
#     plt.ylabel('어획량(톤)')
#     plt.title(str(i)+'월')
#     plt.savefig('img/'+ (str(i)+'월')+ '.png', dpi=100)

#월별 수온 변화 그래프 
# for i in range(1,13):
#     draw_graph(i, '수온')

#월별 수온 변화 그래프 
# for i in range(1,13):
#     draw_graph(i, '합계_수')


# (충첩 그래프)
# for i in range(1,13):
#     year_list=range(2014,2024)
#     month_cuttle_total=[]
#     filter= cuttle_fish['월']==i
#     month_cuttle_total.append(cuttle_fish[filter].mean)
#     x=cuttle_fish[filter]['연']
#     y=cuttle_fish[filter]['수온']
#     plt.plot(x, y)
#     plt.xlabel('연도')
#     plt.ylabel('수온(C)')
#     plt.title(str(i)+'월')
#     plt.show()





# 1월의 연도별 수확량 변화

# print(cuttle_fish[cuttle_fish['월']==1]['합계_수'])
# print(cuttle_fish[cuttle_fish['월']==1]['연'])
# y=cuttle_fish[cuttle_fish['월']==1]['합계_수']
# x=cuttle_fish[cuttle_fish['월']==1]['연']

# plt.plot(x,y)
# plt.show()

# 온도 변화
# print(cuttle_fish[cuttle_fish['월']==1]['합계_수'])
# print(cuttle_fish[cuttle_fish['월']==1]['연'])
# y=cuttle_fish[cuttle_fish['월']==1]['합계_수']
# x=cuttle_fish[cuttle_fish['월']==1]['연']

# plt.plot(x,y)
# plt.show()

# 산점도
# plt.scatter(cuttle_fish['합계_수'], cuttle_fish['수온'])
# plt.show()



# 상관관계
# cuttle_fish['합계_수']= cuttle_fish['합계_수'].astype(int)
# corr= cuttle_fish.corr(numeric_only=True)
# print(corr)

# 연도별  수확량의 합계
total_list=[]
for i in range(2014,2024):
    filter= cuttle_fish['연']==i
    total= cuttle_fish[filter]['합계_수'].sum()
    total_list.append(total)
x=range(2014,2024)
y=total_list
plt.plot(x,y)
plt.title('연도별 오징어 수확량')
plt.xlabel('연도')
plt.ylabel('수확량(톤)')
plt.show()



###집에가서 2021년에 오징어 수확량이 오른 이유 찾기!