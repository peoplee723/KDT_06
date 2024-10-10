import pandas as pd
from tabulate import tabulate
df= pd.read_csv(r'C:\Users\KDP-25\Desktop\KDT_06\crawling\Day02\할리스')

#특정 지역에 있는 커피 매장 출력하기(무한반복)
print(df)
#검색할 매장의 지역 입력 -> 검색된 매장 수 출력+ 매장이름, 주소, 전화번호 출력
word_list=[]
def coffe_search():
    while True:
        word= input('검색할 매장의 지역을 입력하세요: ') #검색할 지역 입력받기 
        if word=='quit':
            break
        else:
            filter=df['지역']==word
            filtered_df= df[filter]
            filtered_df= filtered_df[['매장이름', '주소', '전화번호']]
            filtered_df.columns=['매장이름', '주소', '전화번호']
            filtered_df.index=pd.RangeIndex(start=1, stop=len(filtered_df.index)+1) #새 인덱스 부여

            
            print('검색된 매장의 수: ', len(filtered_df.index))
            print(tabulate(filtered_df, tablefmt='pretty', headers=['매장이름', '주소', '전화번호']))   
coffe_search()
