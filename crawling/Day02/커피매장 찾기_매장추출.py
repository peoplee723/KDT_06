from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

num=1
url=f'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={num}&sido=&gugun=&store='
city_results=[]
storeName_results=[]
address_results=[]
tel_results=[]

while num <=49:
    url=f'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={num}&sido=&gugun=&store='
    html= urlopen(url)
    soup= BeautifulSoup(html.read(), 'html.parser')
    for i in range(10):
        city_results.append(soup.select('td')[0+(i*6)].text)
        storeName_results.append(soup.select('td')[1+(i*6)].text)
        address_results.append(soup.select('td')[3+(i*6)].text)
        tel_results.append(soup.select('td')[5+(i*6)].text)
    num+=1
url=f'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo=50&sido=&gugun=&store='
for i in range(5):
        city_results.append(soup.select('td')[0+(i*6)].text)
        storeName_results.append(soup.select('td')[1+(i*6)].text)
        address_results.append(soup.select('td')[3+(i*6)].text)
        tel_results.append(soup.select('td')[5+(i*6)].text)
print(city_results)
print(storeName_results)
print(address_results)
print(tel_results)
column= ['지역', '주소', '매장이름', '전화번호']
datadic= {'지역': city_results, '주소': address_results, '매장이름': storeName_results, '전화번호': tel_results}

df= pd.DataFrame(data=datadic, columns=column)
print(df)
df.to_csv('할리스', index=0)