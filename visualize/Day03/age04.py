import csv
import matplotlib.pyplot as plt
import re
import koreanize_matplotlib

def parse_district_name(city):
    city_name= re.split('[()]', city)   #숫자 부분 제거하고 문자만 반환
    return city_name

def print_population(population):
    for i in range(len(population)):   #입력받은 열의 나이명 인구수 데이터 출력
        print(f'{i:3d}세: {population[i]:4d}명', end=' ')
        if (i+1)%10==0:
            print()   #10개 마다 줄바꿈

def draw_population(city_name, population_list):
    plt.title(f'{city_name} 인구 현황')
    plt.xlabel('나이')
    plt.ylabel('인구수')
    plt.bar(range(101), population_list)
    plt.xticks(range(0, 101, 10)) #10세 단위로 눈금 생성
    plt.show()

def get_population(city):
    f=open('age.csv', encoding='euc_kr')
    data= csv.reader(f)
    next(data)

    population_list=[]
    full_district_name=''
    for row in data:
        if city in row[0]:
            full_district_name= parse_district_name(row[0])
            for data in row[3:]:
                data= data.replace(',', '')
                population_list.append(int(data))
            break     #처음 일치하는 지역만 빼옴
    f.close()
    print_population(population_list)
    draw_population(full_district_name, population_list)

# city= input('인구 구조를 알고 싶은 지역의 이름(읍면동 단위)을 입력하세요: ')
city= '대구광역시'
get_population(city)
