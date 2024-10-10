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
        time.sleep(2)


loc_lists=[]
other_lang_list=[]
cor_link_list=[]
def get_skill(recuit_link_list):
    '''
    채용공고의 스킬을 가져오는 함수+ 기업정보 링크
    '''
    for link in recuit_link_list:
        url= urlopen(f'https://www.jobkorea.co.kr{link}')
        # url=urlopen('https://www.jobkorea.co.kr/Recruit/GI_Read/45312043?Oem_Code=C1&logpath=1&stext=python&listno=44')
        soup= BeautifulSoup(url, 'html.parser')

        # 스킬 추출
        # loc_list= soup.find('dl', {'class': 'tbList'})
        # loc_num=loc_list.text.strip().find('스킬') if loc_list.text.strip().find('스킬') else 'null'
        # other_lang= loc_list.text[loc_num+3:].strip().split(sep=',')
        # other_lang_list.append(other_lang if other_lang else 'null')
  
        #링크 추출
        cor_links= soup.find('a', {'class': 'girBtn girBtn_3'}) #링크 데이터 추출
        # jar=cor_links['href'] if cor_links['href'] else 'null'
        print(cor_links['href']) if cor_links['href'] else 'null' 
        cor_link_list.append(cor_links['href']) if cor_links['href'] else 'null'

        # 지역 추출
        # dl_tags = soup.find_all('dl', {'class': "tbList"}) #tblist 클래스 가져오기
        # for dl in dl_tags:
        #     dt_tag = dl.find('dt', text='지역')   # '지역' 정보가 있는 <dt> 태그 찾기
        #     if dt_tag:
        #         dd_tag = dt_tag.find_next_sibling('dd') #dd 테그찾기
        #         if dd_tag:
        #             location_links = dd_tag.find_all('a') # a 테그찾기
        #             for link in location_links:
        #                 loc_lists.append([link.text])
        #                 print(link.text,'\n')
        #                 print(len(loc_lists))
        #                 print(len(cor_link_list))

        time.sleep(4)

        
def make_dataFrame(*list, colname):
    DF1= pd.DataFrame(*list, columns=colname)

# get_links()
# get_skill(recuit_link_list)

#csv로 저장 (이름, 링크)
# col_name_list=['기업명', '채용공고링크']
# data=dict({'기업명': cor_title, '채용공고링크': recuit_link_list})

# DF1=pd.DataFrame(data)
# DF1.to_csv('잡코리아', index=0)

df1= pd.read_csv('잡코리아.csv')
dF_cor_link=list(df1['채용공고링크'])

get_skill(dF_cor_link)
# df1['지역']=loc_lists
df1['기업정보링크']=cor_link_list
df1.to_csv('잡코리아1.csv')