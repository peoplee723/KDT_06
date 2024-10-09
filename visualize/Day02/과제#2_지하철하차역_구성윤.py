import pandas as pd
import matplotlib.pyplot as plt
import csv
from tabulate import tabulate
plt.rc('font', family= 'Malgun Gothic')
file_name= 'subwaytime.csv'
df= pd.read_csv(file_name)


#7시 8시 데이터만 추출
df_working_time= df.iloc[:,[1,3,11,13]]
df_working_time.drop(index=0, inplace=True)
df_working_time['Unnamed: 11']=df_working_time['Unnamed: 11'].astype('int64')
df_working_time['Unnamed: 13']=df_working_time['Unnamed: 13'].astype('int64')

df_working_time['하차인원']=df_working_time['Unnamed: 11']+ df_working_time['Unnamed: 13']
df_working_time.drop(columns='Unnamed: 11', inplace=True)
df_working_time.drop(columns='Unnamed: 13', inplace=True)

df_working_time_1= df_working_time[df['호선명']=='1호선']
df_working_time_2= df_working_time[df['호선명']=='2호선']
df_working_time_3= df_working_time[df['호선명']=='3호선']
df_working_time_4= df_working_time[df['호선명']=='4호선']
df_working_time_5= df_working_time[df['호선명']=='5호선']
df_working_time_6= df_working_time[df['호선명']=='6호선']
df_working_time_7= df_working_time[df['호선명']=='7호선']

list=[df_working_time_1, df_working_time_2, df_working_time_3, df_working_time_4,
      df_working_time_5, df_working_time_6, df_working_time_7]


print(max)
df_1= df_working_time_1['하차인원'].max()
df_2= df_working_time_2['하차인원'].max()
df_3= df_working_time_3['하차인원'].max()
df_4= df_working_time_4['하차인원'].max()
df_5= df_working_time_5['하차인원'].max()
df_6= df_working_time_6['하차인원'].max()
df_7= df_working_time_7['하차인원'].max()


max_data=(df_working_time_7[df_working_time_7['하차인원']==df_7])
print(max_data)
# 1호선   종각  356704
# 2호선   역삼  488949
# 3호선  양재(서초구청)  318850
# 4호선  충무로  224078
# 5호선  여의도  340464
# 6호선   공덕  131646
# 7호선  가산디지털단지  494848
num_list=[356704, 488949, 318850, 224078, 340464, 131646, 494848]
name_list=['1호선 종각', '2호선 역삼', '3호선 양재(서초구청)', '4호선 충무로', '5호선 여의도', '6호선 공덕', '7호선 가산디지털단지']

# pd.concat([max_data, (df_working_time_2[df_working_time_2['하차인원']==df_2])],
#           axis=1)

# print(max_data)
# max_data.loc[1]=(df_working_time_2[df_working_time_2['하차인원']==df_2])
# max_data.loc[2]=(df_working_time_3[df_working_time_3['하차인원']==df_3])
# max_data.loc[3]=(df_working_time_4[df_working_time_4['하차인원']==df_4])
# max_data.loc[4]=(df_working_time_5[df_working_time_5['하차인원']==df_5])
# max_data.loc[5]=(df_working_time_6[df_working_time_6['하차인원']==df_6])
# max_data.loc[6]=(df_working_time_7[df_working_time_7['하차인원']==df_7])

plt.bar(name_list, num_list, label=name_list)
plt.title('출근 시간대 지하철 노선별 최대 하차 인원 및 하차역')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

