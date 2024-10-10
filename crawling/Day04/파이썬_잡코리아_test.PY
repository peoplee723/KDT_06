from bs4 import BeautifulSoup
from urllib.request import urlopen 
from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
import time
import numpy as np
from PIL import Image

#한 페이지당 20개씩 링크를 가져와서 링크_list 생성
# -> 링크 들어가서 경력, 고용형태, 지역, 학력, 스킬 가져오기
#++ 기업정보
recuit_link_list=[]
cor_title=[]
def get_links():
    '''
    잡코리아 링크 가져오는 함수+기업이름
    parms= 링크 모아놓을 빈 리스트
    return
    '''
    num=1
    while num<=25:
        url= urlopen(f'https://www.jobkorea.co.kr/Search/?stext=python&tabType=recruit&Page_No={num}')
        soup= BeautifulSoup(url, 'html.parser')

        links= soup.find_all('a', {'class': "corp-name-link dev-view"})
        for link in links:
            link= link['href']
            recuit_link_list.append(link)
            print(link)
        for link in links:
            link= link.text.strip()
            cor_title.append(link)
            print(link)
        num+=1
        # time.sleep(2)


loc_lists=[]
other_lang_list=[]
cor_link_list=[]
def get_skill(recuit_link_list):
    '''
    채용공고의 스킬을 가져오는 함수+ 기업정보 링크
    '''
    for link in recuit_link_list:
        url= urlopen(f'https://www.jobkorea.co.kr{link}')
        soup= BeautifulSoup(url, 'html.parser')

        # 스킬 추출
        try:
            jar1=soup.find('dt', text='스킬').next.next.next.text.strip().split(',')
            loc_list= list(jar1)
            print(jar1)
            for loc in (loc_list):
                print(loc.strip())
                # other_lang= loc_list
                # print(other_lang)        
                other_lang_list.append(loc.strip())

        except Exception as e:
        
            print(e)
        time.sleep(4)
        #링크 추출
        # cor_links= soup.find('a', {'class': 'girBtn girBtn_3'})    #링크 데이터 추출
        # jar=cor_links['href']
        # print(jar)
        # cor_link_list.append(jar)
        # print(jar)

    
# get_skill(recuit_link_list)
# print(cor_link_list)

salary_link_lists=[]
def get_salary_links(cor_link_list):
    '''
    기업정보 링크 통해서 연봉정보 링크 가져오는 함수
    (/Recruit/Salary/41569190)
    parmas=cor_link_list
    '''
    # cor_link_list=['/Recruit/Co_Read/C/41569190?Oem_Code=C1']
    for link in cor_link_list:
        url= urlopen(f'https://www.jobkorea.co.kr{link}')
        soup= BeautifulSoup(url, 'html.parser')
        try:
            jar= soup.find_all('a', {'class': "company-nav-item" })[2] if soup.find_all('a', {'class': "company-nav-item" })[2] else 'null'
            jar2= jar['href']
        except Exception as e:
            print(e)
        print(jar2)
        salary_link_lists.append(jar2)
        time.sleep(4)

#지역
def get_loc(recuit_link_list):
    for link in recuit_link_list:
        url= urlopen(f'https://www.jobkorea.co.kr{link}')
    # url=urlopen('https://www.jobkorea.co.kr/Recruit/GI_Read/45312043?Oem_Code=C1&logpath=1&stext=python&listno=44')
        soup= BeautifulSoup(url, 'html.parser')
        dl_tags = soup.find_all('dl', {'class': "tbList"}) #tblist 클래스 가져오기
        for dl in dl_tags:
                dt_tag = dl.find('dt', text='지역')   # '지역' 정보가 있는 <dt> 태그 찾기
                if dt_tag:
                    dd_tag = dt_tag.find_next_sibling('dd') #dd 테그찾기
                    if dd_tag:
                        location_links = dd_tag.find_all('a') # a 테그찾기
                        for link in location_links:
                            loc_lists.append(link.text)
                            print(link.text)
        # time.sleep(4) 

# get_salary_links(cor_link_list)
salary_lists=[]
def get_salary_info(salary_link_lists):
    '''
    전체 평균 연봉을 가져오는 함수
    params= salary_link_lists
    '''
    # salary_link_lists=['/Recruit/Salary/41569190']
    for link in salary_link_lists:
            url= urlopen(f'https://www.jobkorea.co.kr{link}')
            soup= BeautifulSoup(url, 'html.parser')
            try:
                jar= soup.find('div', {'class': 'salary'}).text.strip()
                jar2= jar.replace('만원', '') if jar else 'null'
                jar3= jar2.replace('\n', '') if jar2 else 'null'
                salary_lists.append(jar3)
            except Exception as e:
                print(e)
    time.sleep(4)

cor_emlo_lists=[]
def get_cor_emplo(cor_link_list):
    '''기업 정보 링크를 통해 사원수 가져오는 함수\
        params= cor_link_list
        '''
    cor_link_list=['/Recruit/Co_Read/C/41569190?Oem_Code=C1']
    for link in cor_link_list:
        url= urlopen(f'https://www.jobkorea.co.kr{link}')
        soup= BeautifulSoup(url, 'html.parser')
        jar=soup.find_all('div', {'class', 'values'})[0].text
        jar2= jar.replace('명', '') if jar.replace('명', '') else 'null'
        print(jar2)
        cor_emlo_lists.append(jar2)
# get_cor_emplo(cor_link_list)

get_links()
# get_skill(recuit_link_list)


# get_salary_links(cor_link_list)
# get_salary_info(salary_link_lists)

# col_name_list=['기업명', '채용공고링크', '스킬', '지역', '기업정보']
# DF1=pd.DataFrame(cor_title, recuit_link_list, other_lang_list, loc_lists,cor_link_list, columns=col_name_list )
# DF1.to_csv('잡코리아', index=0)


# # 연봉 링크 가져오기
# df=pd.read_csv('잡코리아1.csv')
# df_link= df['기업정보링크']
# get_salary_links(df_link)
# # df_salary=dict({'연봉링크': salary_link_lists})
# df_salary=pd.DataFrame(salary_link_lists)
# df_salary.to_csv('연봉링크.csv')

# #연봉 정보 가져오기
# df=pd.read_csv('연봉링크.csv')
# get_salary_info(df)
# df_salary_info=pd.DataFrame(salary_lists)
# df_salary_info.to_csv('연봉정보.csv')



# 지역 정보 가져오기
# df=pd.read_csv(r'C:\Users\KDP-25\Desktop\KDT_06\crawling\Day04\잡코리아.csv')
# df_link= df['채용공고링크']
# get_loc(df_link)
# df_loc_list=pd.DataFrame(loc_lists, columns=['지역'])
# df_loc_list.to_csv('지역정보.csv')

#스킬 정보 가져오기
# df=pd.read_csv('잡코리아.csv')
# df_link= df['채용공고링크']
# try:    
#     get_skill(df_link)
# except Exception as e:
#     print(e)
# df_skill_list=pd.DataFrame(other_lang_list)
# df_skill_list.to_csv('스킬정보')
