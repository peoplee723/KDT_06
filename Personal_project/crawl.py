# 네이버 검색 API 예제 - 블로그 검색
import os
import sys
import urllib.request
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
from urllib.parse import quote


# client_id = "vAcuTP8HYLTwb34u12a0"
# client_secret = "NwFeqYc5YY"
# encText = urllib.parse.quote("홈택스")
# # url = "https://openapi.naver.com/v1/search/kin/display=100?query=" + encText # JSON 결과
# url = "https://openapi.naver.com/v1/search/kin.xml?query=" + encText+'&display=100&start=100' # XML 결과
# request = urllib.request.Request(url)
# request.add_header("X-Naver-Client-Id",client_id)
# request.add_header("X-Naver-Client-Secret",client_secret)
# response = urllib.request.urlopen(request)
# rescode = response.getcode()

# link_list=[]
# if(rescode==200):
#     response_body = response.read().decode('utf-8')
#     body= BeautifulSoup(response_body, "lxml-xml")
#     jar= body.find_all('link')
#     for j in range(1, len(jar)):
#         link= jar[j].get_text()
#         print(link, end='\n')
#         link_list.append(link)
#     print(len(link_list))
# else:
#     print("Error Code:" + rescode)

# 질문
# div.questionDetail
# 대답
# answer_1 > div.answerDetail._endContents._endContentsText



def get_links(time_list):
    '''
    뉴스 링크 가져오는 함수
    return
    '''
    article_link_list=[]
    for time in time_list:
        url= urlopen(f'https://kin.naver.com/search/list.naver?query=%ED%99%88%ED%83%9D%EC%8A%A4&page={time}')
        soup= BeautifulSoup(url, 'html.parser')


        jar2= soup.find_all('a',{'class':"_nclicks:kin.txt _searchListTitleAnchor"})
        for j in jar2:
            link= j.get('href')
            article_link_list.append(link)
            # print(link)
        if time%100==0:
            print(time)
    return article_link_list

time_list=[]
for a in range(1,2400):
    time_list.append(a)
# 링크 크롤링
links=get_links(time_list)

# 데이터프레임으로 변환 후 csv로 저장
linkDF=pd.DataFrame()
linkDF['link']=links
linkDF.to_csv('./link.csv')
print(len(links))

def get_QNA(links):
    q_list=[]
    a_list=[]
    for i in links:

        link=i
        encoded_link = quote(link, safe=':/?=&')
        request = urllib.request.Request(encoded_link)
        url= urlopen(request)
        response= url.read().decode('utf-8')
        soup= BeautifulSoup(response, 'html.parser')


        # 질문 추출
        jar2= soup.find('div',{'class':"questionDetail"})
        # print(jar2.get_text(strip=True), type(jar2))
        q= (jar2.get_text(strip=True))
        # print(q)
        q_list.append(q)
        # 대답 추출
        jar3= soup.find_all('div', {'class': 'se-main-container'})
        # print(jar3[1].get_text(), len(jar3))
        a=[]
        for i in range(len(jar3)):
            text=jar3[i].get_text(strip=True)
            a.append(text.replace('\u200b', ''))
        # 추출한 텍스트 리스트에 추가
        a_list.append(a)
        if i%100==0: print(i)
    print(len(a_list))
    print(len(q_list))

    return a_list, q_list
    # print(texts)



a, q=get_QNA(links)
# 혹시 모르니 따로도 저장
answer, question=pd.DataFrame(), pd.DataFrame()
answer['answer']=a
question['question']=q
answer.to_csv('./answer.csv')
question.to_csv('./question.csv')

# 하나의 DF로 묶어서 저장
kin=pd.DataFrame()
kin['link']=links
kin['question']=q
kin['answer']=a
kin.to_csv('./kin.csv')
