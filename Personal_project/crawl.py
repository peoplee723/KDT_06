import os
import sys
import urllib.request
from bs4 import BeautifulSoup
from urllib.request import urlopen
from collections import Counter
# from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
from urllib.parse import quote


# 질문
# div.questionDetail
# 대답
# answer_1 > div.answerDetail._endContents._endContentsText


# 연말정산: %EC%97%B0%EB%A7%90%EC%A0%95%EC%82%B0
def get_links(time_list):
    '''
    뉴스 링크 가져오는 함수
    return
    '''
    article_link_list=[]
    for time in time_list:
        url= urlopen(f'https://kin.naver.com/search/list.naver?query=%EC%97%B0%EB%A7%90%EC%A0%95%EC%82%B0={time}')
        soup= BeautifulSoup(url, 'html.parser')


        jar2= soup.find_all('a',{'class':"_nclicks:kin.txt _searchListTitleAnchor"})
        for j in jar2:
            link= j.get('href')
            article_link_list.append(link)
            # print(link)
        if time%100==0:
            print(time)
    return article_link_list

# time_list=[]
# for a in range(1,500):
#     time_list.append(a)
# # 링크 크롤링
# links=get_links(time_list)

# # 데이터프레임으로 변환 후 csv로 저장
# linkDF=pd.DataFrame()
# linkDF['link']=links
# linkDF.to_csv('./link.csv')
# print(len(links))

def get_QNA(links):
    a_list, q_list=[],[]
    count=1
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
        # print(jar3[0].get_text(), len(jar3))
        a=[]
        for j in range(len(jar3)):
            text=jar3[j].get_text(strip=True)
            a.append(text.replace('\u200b', ''))
            # print(text)
        # 추출한 텍스트 리스트에 추가
        a_list.append(a)
        # if count%100==0: print(count)
        count+=1
    print(len(kin_list[0]))
    print(len(kin_list[1]))

    return q_list, a_list
    # print(texts)


links=pd.read_csv('link.csv')

q_list, a_list =get_QNA(links['link'])


# 혹시 모르니 따로도 저장 (0 질문, 1 대답)
# with open('answer.csv', mode='a', newline='') as f:
#     writer=csv.writer(f)
#     writer.writerows(kin[1])
# with open('question.csv', mode='a', newline='') as f:
#     writer=csv.writer(f)
#     writer.writerows(kin[0])
# 따로 저장
# q, a= pd.DataFrame(), pd.DataFrame()
# q['question']=kin[0]
# a['answer']=kin[1]
# q.to_csv('question.csv', index=False)
# a.to_csv('answer.csv', index=False)

# 하나의 DF로 묶어서 저장
links=pd.read_csv('./link.csv')
kin=pd.DataFrame()
kin['link']=links['link']

kin['question']=q_list
kin['answer']=a_list
kin.to_csv('./kin.csv')
