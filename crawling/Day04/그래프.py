import pandas as pd
import matplotlib.pylab as plt
import koreanize_matplotlib
from wordcloud import WordCloud
import numpy as np
from PIL import Image


#연봉을 토대로 히스토그램 그리기
def make_hist():
    DF=pd.read_csv(r'C:\Users\KDP-25\Desktop\KDT_06\crawling\Day04\연봉정보.csv')
    DF.drop(columns=['Unnamed: 0'], inplace=True)
    print(DF.info())

    plt.hist(DF, bins=200, histtype='bar')
    plt.xlabel='연봉(만원)'
    plt.title('직원들의 연봉 범위')
    plt.show()
    print(DF.describe())
make_hist()

# 지역 -> 파이
# 연봉->히스토그램
# 스킬 -> 클라우드
