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


salary_lists=[]
def get_salary_info(salary_link_lists):
    '''
    전체 평균 연봉을 가져오는 함수
    params= salary_link_lists
    '''
    # salary_link_lists=['/Recruit/Salary/41569190']
    for link in salary_link_lists:
            try:
                if link =='null': break 
                else:
                    url= urlopen(f'https://www.jobkorea.co.kr/{link}')
                
                    soup= BeautifulSoup(url, 'html.parser')

                    jar= soup.find('div', {'class': 'salary'}).text.strip()
                    jar2= jar.replace('만원', '') if jar else 'null'
                    jar3= jar2.replace('\n', '') if jar2 else 'null'
                    salary_lists.append(jar3)
                    print(jar3)
            except Exception as e:
                    print(e)
        # time.sleep(4)


#연봉 정보 가져오기
df=pd.read_csv('연봉링크.csv')
print(df['0'])
get_salary_info(df['0'])
df_salary_info=pd.DataFrame(salary_lists)
df_salary_info.to_csv('연봉정보.csv')
