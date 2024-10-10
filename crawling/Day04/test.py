from bs4 import BeautifulSoup
from urllib.request import urlopen 
import requests
from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import time
import numpy as np
from PIL import Image
import csv
link_lists=[]
cor_name=[]
def get_links(link_lists):
    num=1
    while num<=25:
        url= urlopen(f'https://www.jobkorea.co.kr/Search/?stext=python&tabType=recruit&Page_No={num}')
        soup= BeautifulSoup(url, 'html.parser')

        links= soup.find_all('a', {'class': "corp-name-link dev-view"})
        for link in links:
            link= link['href']
            link_lists.append(link)
        for link in links:
            link= link.text.strip()
            cor_name.append(link)
        num+=1
        time.sleep(2)
loc_lists=[]
other_lang_list=[]
link_num_list=[]
def get_skill(link_lists, other_lang_list, link_num_list):
    '''
    채용공고의 스킬을 가져오는 함수+ 기업정보 링크
    '''
    for link in link_lists:
        # url= urlopen(f'https://www.jobkorea.co.kr{link}')
        url=urlopen('https://www.jobkorea.co.kr/Recruit/GI_Read/45312043?Oem_Code=C1&logpath=1&stext=python&listno=44')
        soup= BeautifulSoup(url, 'html.parser')

        # 스킬 추출
        loc_list= soup.find('dl', {'class': 'tbList'})
        loc_num=loc_list.text.strip().find('스킬')
        other_lang= loc_list.text[loc_num+3:].strip().split(sep=',')
        other_lang_list.append(other_lang if other_lang else np.nan)
  
        #링크 추출
        cor_links= soup.find('a', {'class': 'girBtn girBtn_3'}) #링크 데이터 추출
        link_num=cor_links['href'] 
        print(link_num)
        link_num_list.append(link_num)

        dl_tags = soup.find_all('dl', {'class': "tbList"}) #tblist 클래스 가져오기
        for dl in dl_tags:
            dt_tag = dl.find('dt', text='지역')   # '지역' 정보가 있는 <dt> 태그 찾기
            if dt_tag:
                dd_tag = dt_tag.find_next_sibling('dd') #dd 테그찾기
                if dd_tag:
                    location_links = dd_tag.find_all('a') # a 테그찾기
                    for link in location_links:
                        loc_lists.append(link) 
                        print(link)
        time.sleep(2)
# get_links(link_lists)
# get_skill(link_lists, other_lang_list, link_num_list)
# print(link_num_list)


# <a class="girBtn girBtn_3" href="/Company/1830029/Salary?C_IDX=254" 

#container > section > div.readSumWrap.clear > 
# article > div.tbRow.clear > div:nth-child(2) > dl > dd:nth-child(6) > a
# 주<span class="tahoma">5</span>일
                                # (월~금)


url = urlopen(f'https://www.jobkorea.co.kr/Recruit/GI_Read/45288844?Oem_Code=C1&logpath=1&stext=python&listno=46')
soup = BeautifulSoup(url, 'html.parser')

dl_tags = soup.find_all('dl', {'class': "tbList"}) #tblist 클래스 가져오기
for dl in dl_tags:
    dt_tag = dl.find('dt', text='지역')   # '지역' 정보가 있는 <dt> 태그 찾기
    if dt_tag:
        dd_tag = dt_tag.find_next_sibling('dd') #dd 테그찾기
        if dd_tag:
            location_links = dd_tag.find_all('a') # a 테그찾기
            for link in location_links:
                print(link.text)  



#크롤링 할 것들
# 1. 기업 이름
# 2. 연봉 정보
# 3. 지역 정보
# if 문을 통해 없는 정보는 빈칸으로 놔두기
# 