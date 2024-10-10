import pandas as pd
import matplotlib.pylab as plt
import koreanize_matplotlib
from wordcloud import WordCloud

def make_skill_gragh():
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

#연봉을 토대로 히스토그램 그리기
DF=pd.read_csv(r'C:\Users\KDP-25\Desktop\KDT_06\crawling\Day04\연봉정보.csv')
DF.drop(columns=['Unnamed: 0'], inplace=True)
print(DF.info())

plt.hist(DF, bins=20, histtype='bar', color='royalblue')
plt.xlabel='연봉(만원)'

plt.title('직원들의 연봉 범위')
plt.show()

# 지역 -> 파이
# 연봉->히스토그램
# 스킬 -> 클라우드