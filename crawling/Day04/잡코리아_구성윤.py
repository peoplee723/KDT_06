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
from matplotlib.patches import ConnectionPatch

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


#-------------------------------------------------------------------------------#
# 그래프 그리기

# 워드클라우드
def get_titles(start_num, end_num, search_word, title_list):
    while start_num <= end_num:
        url= ('https://search.naver.com/search.naver?where=news&sm=tab_jum&query={}&start={}'.format(search_word, start_num))

        req= requests.get(url)
        time.sleep(1)
        if req.ok:
            soup= BeautifulSoup(req.text, 'html.parser')
            news_titles= soup.find_all('a', {'class': 'news_tit'})
            for news in news_titles:
                title_list.append(news['title'])
        start_num+=10
        print('title 개수:', len(title_list))
        print(title_list)

def make_wordcloud(title_list, stopwords, word_count):
    okt= Okt()
    sentences_tag= []

    for sentence in title_list:
        morph= okt.pos(sentence)
        sentences_tag.append(morph)
        print(morph)
        print('-'*80)
    
    noun_adj_list=[]
    for sentence1 in sentences_tag:
        for word, tag in sentence1:
            if tag in ['Noun', 'Adjective', 'Alpha']:
                noun_adj_list.append(word)

    counts= Counter(noun_adj_list)
    tags= counts.most_common(word_count)
    print('-'*80)
    print(tags)

    tag_dict= dict(tags)

    for stopword in stopwords:
        if stopword in tag_dict:
            tag_dict.pop(stopword)
    print(tag_dict)

    path= r'c:\Windows\Fonts\malgun.ttf'

    img_mask= np.array(Image.open('P_reverse.jpg'))
    wordcloud= WordCloud(font_path=path, width=800, height=600,
                         background_color='white', max_font_size=200,
                         repeat=True,
                         colormap='inferno', mask=img_mask)
    
    cloud= wordcloud.generate_from_frequencies(tag_dict)
    plt.figure(figsize=(10,8))
    plt.axis('off')
    plt.imshow(cloud)
    plt.show()

if __name__ == '__main__':
    search_word= '파이썬'
    title_list=[]
    stopwords= [search_word, 'python']

    get_titles(1, 200, search_word, title_list)

    make_wordcloud(title_list, stopwords, 50)

# 블로그 워드클라우드

def get_titles(start_num, end_num, search_word, title_list):
    while start_num <= end_num:
        url= ('https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query={}&start={}'.format(search_word, start_num))

        req= requests.get(url)
        time.sleep(1)
        if req.ok:
            soup= BeautifulSoup(req.text, 'html.parser')
            news_titles= soup.find_all('div', {'class': 'title_area'})
            for news in news_titles:
                title_list.append(news.text)
        start_num+=10
        print('title 개수:', len(title_list))
        print(title_list)

def make_wordcloud(title_list, stopwords, word_count):
    okt= Okt()
    sentences_tag= []

    for sentence in title_list:
        morph= okt.pos(sentence)
        sentences_tag.append(morph)
        print(morph)
        print('-'*80)
    
    noun_adj_list=[]
    for sentence1 in sentences_tag:
        for word, tag in sentence1:
            if tag in ['Noun', 'Adjective', 'Alpha']:
                noun_adj_list.append(word)

    counts= Counter(noun_adj_list)
    tags= counts.most_common(word_count)
    print('-'*80)
    print(tags)

    tag_dict= dict(tags)

    for stopword in stopwords:
        if stopword in tag_dict:
            tag_dict.pop(stopword)
    print(tag_dict)

    path= r'c:\Windows\Fonts\malgun.ttf'

    img_mask= np.array(Image.open('P.jfif'))
    wordcloud= WordCloud(font_path=path, width=800, height=600,
                         background_color='white', max_font_size=200,
                         repeat=True,
                         colormap='inferno', mask=img_mask)
    
    cloud= wordcloud.generate_from_frequencies(tag_dict)
    plt.figure(figsize=(10,8))
    plt.axis('off')
    plt.imshow(cloud)
    plt.show()

if __name__ == '__main__':
    search_word= '파이썬'
    title_list=[]
    stopwords= [search_word, 'python', 'Python', '코딩', '아나콘다', '설치', '프로그래밍']

    get_titles(1, 200, search_word, title_list)

    make_wordcloud(title_list, stopwords, 50)


#파이그래프 그리기 (matplotlib 예시코드 참조)
DF= pd.read_csv('지역정보.csv')
DF.drop(columns=['Unnamed: 0'], inplace=True)
DF_list= (DF['지역'])
seoul=0
busan=0
inchan=0
daegu=0
changju=0
gyunggi=0
other=5
for list in DF_list:
    if ('서울') in list:
        seoul+=1 
    if ('경기') in list:
        gyunggi+=1
    if ('부산') in list:
        busan+=1 
    if ('대구') in list:
        daegu+=1
    if ('인천') in list: 
        inchan+=1 
    if ('충청북') in list:
        changju+=1
    
    # print(list, '\n')
print(seoul)
print(busan)
print(inchan)
print(daegu)
print(gyunggi)
pie_data_list=[busan+daegu+other, gyunggi, seoul]
sum_num=(busan+daegu+other)
bar_data_list=[busan/sum_num, daegu/sum_num, other/sum_num]
label_list=['그외', '경기','서울']

fig, (ax1, ax2)= plt.subplots(1, 2, figsize=(9,5))
fig.subplots_adjust(wspace=0)

#pie그리기
overall_ratios = pie_data_list
labels = label_list
explode = [0.1, 0, 0]
# rotate so that first wedge is split by the x-axis
angle = -180 * overall_ratios[0]
wedges, *_ = ax1.pie(overall_ratios, autopct='%1.2f%%', startangle=angle,
                     labels=labels, explode=explode, colors=['#4374D9', '#47C83E', '#E9537C' ])

# bar 그리기
age_ratios = bar_data_list
age_labels = ['부산', '대구', '기타']
bottom = 1
width = .2

# Adding from the top matches the legend.
for j, (height, label) in enumerate(reversed([*zip(age_ratios, age_labels)])):
    bottom -= height
    bc = ax2.bar(0, height, width, bottom=bottom, color='C0', label=label,
                 alpha=0.1 + 0.25 * j)
    ax2.bar_label(bc, labels=[f"{height:.0%}"], label_type='center')

ax2.set_title('서울&경기 외')
ax2.legend()
ax2.axis('off')
ax2.set_xlim(- 2.5 * width, 2.5 * width)

# use ConnectionPatch to draw lines between the two plots
theta1, theta2 = wedges[0].theta1, wedges[0].theta2
center, r = wedges[0].center, wedges[0].r
bar_height = sum(age_ratios)

# draw top connecting line
x = r * np.cos(np.pi / 180 * theta2) + center[0]
y = r * np.sin(np.pi / 180 * theta2) + center[1]
con = ConnectionPatch(xyA=(-width / 2, bar_height), coordsA=ax2.transData,
                      xyB=(x, y), coordsB=ax1.transData)
con.set_color([0, 0, 0])
con.set_linewidth(4)
ax2.add_artist(con)

# draw bottom connecting line
x = r * np.cos(np.pi / 180 * theta1) + center[0]
y = r * np.sin(np.pi / 180 * theta1) + center[1]
con = ConnectionPatch(xyA=(-width / 2, 0), coordsA=ax2.transData,
                      xyB=(x, y), coordsB=ax1.transData)
con.set_color([0, 0, 0])
ax2.add_artist(con)
con.set_linewidth(4)
plt.suptitle('지역별 채용공고 현황')

plt.show()

#스킬 정보 워드클라우드
title_list= pd.read_csv('스킬정보.csv')['0']

word_count=50
stopwords=['python', 'Python']
path= r'c:\Windows\Fonts\malgun.ttf'
def make_skill_gragh(start_num, end_num, search_word, title_list):

    okt= Okt()
    sentences_tag= []

    for sentence in title_list:
        morph= okt.pos(sentence)
        sentences_tag.append(morph)
        print(morph)
        print('-'*80)
    
    noun_adj_list=[]
    for sentence1 in sentences_tag:
        for word, tag in sentence1:
            if tag in ['Noun', 'Adjective', 'Alpha']:
                noun_adj_list.append(word)

    counts= Counter(noun_adj_list)
    tags= counts.most_common(word_count)
    print('-'*80)
    print(tags)

    tag_dict= dict(tags)

    for stopword in stopwords:
        if stopword in tag_dict:
            tag_dict.pop(stopword)
    print(tag_dict)

    img_mask= np.array(Image.open('alice_wordcloud.png'))
    wordcloud= WordCloud(font_path=path, width=800, height=600,
    background_color='white', max_font_size=200,
    repeat=True,
    colormap='inferno', mask=img_mask)
        
    cloud= wordcloud.generate_from_frequencies(tag_dict)
    plt.figure(figsize=(10,8))
    plt.axis('off')
    plt.imshow(cloud)
    plt.show()
make_skill_gragh()

#히스토그램

def make_hist():
    DF=pd.read_csv(r'C:\Users\KDP-25\Desktop\KDT_06\crawling\Day04\연봉정보.csv')
    DF.drop(columns=['Unnamed: 0'], inplace=True)
    print(DF.info())

    plt.hist(DF, bins=200, histtype='bar')
    plt.xlabel='연봉(만원)'
    plt.title('직원들의 연봉 범위')
    plt.show()
make_hist()