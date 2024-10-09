dic_file={'Seoul': ['South Korea', 'Asia', 9655000],
          'Tokyo': ['Japan', "Asia", 14110000],
          'Beijing': ['China', 'Asia', 21540000],
          'London': ['United Kingdom', 'Europe', 14800000],
          'Berlin': ['Germany', 'Europe', 3426000],
          'Mexico City': ['Mexico', 'America', 21200000]}

#1. 전체 데이터 출력
def main():
    print(
'-----------------------------------------\n'
'1.	전체 데이터 출력\n'		
'2.	수도 이름 오름차순 출력\n'										
'3.	모든 도시의 인구수 내림차순 출력\n'		
'4.	특정 도시의 정보 출력\n'		
'5.	대륙별 인구수 계산 및 출력\n'		
'6.	프로그램 종료\n'
'-----------------------------------------\n'
)
main()
num= int(input('메뉴를 입력하세요'))
if num==1:
    for i in range(1,7):
        print(f'[{i}] {list(dic_file)[i-1]}: {list(dic_file.values())[i-1]}')

elif num==2:
    #이름 오른차순 정렬
    sort_name= sorted(dic_file.items(), key= lambda x: x[0])
    for i in range(1,7):
        print(f'[{i:^}] {sort_name[i-1][0]:^11}: {sort_name[i-1][1][0]:^14} {sort_name[i-1][1][1]:^7} {sort_name[i-1][1][2]:^11,}')

elif num==3:
    #도시 인구수 내림차순
    sort_people= sorted(dic_file.items(), key= lambda x: x[1][2], reverse=True)
    for i in range(1,7):
        print(f'[{i}] {sort_people[i-1][1][0]:^14}: {sort_people[i-1][1][2]:^11,}')

elif num==4:
    city= input('출력할 도시 이름을 입력하세요')
    if city not in list(dic_file):
        print(f'도시이름: {city}은 key에 없습니다')
    else:
        print(f'도시: {city}')
        print(f'국가: {dic_file[city][0]}, 대륙: {dic_file[city][1]}, 인구수: {dic_file[city][2]:,}')

elif num==5:
    big= input('대륙 이름을 입력하세요(Asia, Europe, America): ')
    country_list= list(dic_file)
    big_num=0
    for list in country_list:
        if dic_file[list][1]==big:
            print(f' {list}: {dic_file[list][2]:,}')
            big_num+=int(dic_file[list][2])
    print(f'{big} 전체 인구수: {big_num:,}')

elif num==6:
    print('프로그램을 종료합니다')

