import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib

# 시작 연도와 끝 연도, 월을 입력받음
# 월의 연도기간동안의 최고, 최저기온 평균 구하기
# +날짜 datetime으로 변경

# 꺾은선 그래프 2개 출력
# (마이너스 깨짐 방지, 타이틀 이름 변경, 그래프 색깔 및 마커와 lengend표시)

file_name= 'daegu-uft8-df.csv'
df= pd.read_csv(file_name)
df['날짜']= pd.to_datetime(df['날짜'], format='%Y-%m-%d')

def drawgraph(title, x_data, Max, Max_label, Min, Min_label):

    plt.figure()
    plt.rcParams['axes.unicode_minus'] =False
    plt.plot(x_data, Max, marker='s', color='r', label=Max_label)
    plt.plot(x_data, Min, marker='o', color='b', label=Min_label)
    plt.xticks(x_data)
    plt.legend
    plt.title(title)



def temp_minmax_mean():
    start_year= 2014
    end_year= 2023
    search_month= 12
    # xx년 ~ yy년의 m월 데이터 추출

    df_index=df[(df['날짜'].dt.year >= start_year)& (df['날짜'].dt.year<= end_year)&
                (df['날짜'].dt.month== search_month)]
    # 연 최저/최고기온 평균 추출

    #1. 연도 추출
    year_set=set({ })
    for i in df['날짜'].dt.year:
        if start_year<=int(i)<=end_year:
            year_set.add(i)
        year_list= list(year_set)
    year_list.sort()
    
    # 특정 월의 평균 기온 추출 ->해당 월의 연당 최고기온의 평균 추출
    df_maxmean_list=[]
    df_minmean_list=[]
    for year in year_list:
        #한 연도 데이터 추출
        df_max= df[(df['날짜'].dt.year==year) & (df['날짜'].dt.month==search_month)]
        df_maxmean_list.append(round(df_max['최고기온'].mean(),1))
        print(df_maxmean_list)

        df_min= df[(df['날짜'].dt.year==year) & (df['날짜'].dt.month==search_month)]
        df_minmean_list.append(round(df_min['최저기온'].mean(),1))

temp_minmax_mean()