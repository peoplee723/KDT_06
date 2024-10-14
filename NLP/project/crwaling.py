from bs4 import BeautifulSoup
from urllib.request import urlopen
from collections import Counter
# from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
import time
import numpy as np
from PIL import Image
import re
import csv

# 뉴스기간 2024-01-01 ~ 2024-09-30
time_list=[]
for a in range(140):
    time_list.append(pd.Timestamp(19503+a, unit="D").strftime("%Y%m%d"))

#한 페이지당 20개씩 링크를 가져와서 링크_list 생성
# -> 링크 들어가서 경력, 고용형태, 지역, 학력, 스킬 가져오기
#++ 기업정보


def get_links(time_list, idx):
    '''
    뉴스 링크 가져오는 함수
    return
    '''
    article_link_list=[]
    for time in time_list:
        url= urlopen(f'https://news.naver.com/breakingnews/section/102/{idx}?date={time}')
        soup= BeautifulSoup(url, 'html.parser')

        links= soup.find_all('div', {'class': "sa_text"})
       
        for link in links:
            # print(link.find('a')['href'])
            article_link_list.append(link.find('a')['href'])
    return article_link_list



def get_skill(article_link_list, save_num):
    '''
    뉴스 본문 가져오는 함수
    '''
    article_main_list=[]
    count=0
    with open(f'{save_num}.csv', mode='a', newline='', encoding='utf-8') as f:
        writer= csv.writer(f)
        for link in article_link_list:

            url= urlopen(link)
            soup= BeautifulSoup(url, 'html.parser')

            # 본문 추출
            try:
                jar1=soup.find_all('article')
                article_main_list.append(jar1)
                # print(jar1)
                writer.writerows(jar1)
                # f.append(jar1)


            except Exception as e:
           
                print(e)
            count+=1
            if count%10==0:
                print(count)
    return article_main_list
def makeCSV(article_main_list, num):
    articleDF= pd.DataFrame()
    articleDF['text']=article_main_list
    articleDF['label']=num
    articleDF.to_csv(f'all_{num}.csv')

#크롤링
idx=['250','252', '255']
save_num=['0','1','2']

for i in range(1,3):
    article_link_list= get_links(time_list, idx=idx[i])
    print(len(article_link_list))
    article_main_list=get_skill(article_link_list, save_num=save_num[i])
    makeCSV(article_main_list, num=save_num[i])


# 0 교육
# 1 환경
# 2 식품/의료