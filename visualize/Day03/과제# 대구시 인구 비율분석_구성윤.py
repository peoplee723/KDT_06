import csv
import matplotlib.pyplot as plt
import platform
import math
import koreanize_matplotlib


#subplot (5,2) 생성후 한 figure에 그래프 10개 넣기 


f=open('gender.csv', encoding='euc_kr')
data= csv.reader(f)
city_list=['대구광역시', '대구광역시 중구', '대구광역시 동구', '대구광역시 서구', '대구광역시 남구', 
           '대구광역시 북구', '대구광역시 수성구', '대구광역시 달서구', '대구광역시 달성군', '대구광역시 군위군']
city_people_list=[]
label_list=['남성', '여성']
axs_list= ['ax1', 'ax2', 'ax3', 'ax4', 'ax5', 'ax6', 'ax7', 'ax8', 'ax9', 'ax10']
for city in city_list:
    idx_num= (city_list.index(city))
    gender_list=[]
    male_list= []
    female_list= []
    for row in data:
        if city in row[0]:
            for i in range(106,207):
                male_list.append(int(row[i].replace(',', ''))) #해당하는 도시의 연령별 데이터 저장
                
                female_list.append(int(row[i+103].replace(',', ''))) #규칙성 찾아내기!
                
            break #도시 하위 목록 많음
    f.close()
    print(f' {city}: (남: {sum(male_list):,} 여: {sum(female_list):,})')
    gender_list.append(sum(male_list))
    gender_list.append(sum(female_list))
    city_people_list.append(gender_list)
  
    
fig= plt.figure(figsize=(15,15))
# axs[1,1].pie(city_people_list[0], labels=label_list)
for i in range(1,11):
    ax= fig.add_subplot(5,2, i)
    ax.pie(city_people_list[i-1], labels=label_list, autopct='%.1f%%',startangle=90)
    ax.set_title(city_list[i-1])
    # plt.title(list[i-1])

fig.tight_layout()
fig.suptitle('대구광역시 구별 남녀 인구 비율')
plt.show()