from urllib.request import urlopen
from urllib.parse import quote  #한글 입력시 오류 해결
import requests
from bs4 import BeautifulSoup

query= quote('지진')
url= f'https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query={query}'

html=urlopen(url)
soup= BeautifulSoup(html.read(), 'html.parser')
blog_results= soup.select('a.title_link')
print('검색 결과수: ', len(blog_results))
search_count= len(blog_results)
dsec_results= soup.select('a.dsc_link')

for i in range(search_count):
    title= blog_results[i].text
    link= blog_results[i]['href']
    print(f'{title}, [{link}]')
    print(dsec_results[i].text)
    print('-'*100)
    