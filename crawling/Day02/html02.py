from urllib.request import urlopen
from bs4 import BeautifulSoup

html= urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
soup= BeautifulSoup(html, 'html.parser')

#등장인물의 이름:녹색
name_list = soup.find_all('span', {'class': 'green'})
for name in name_list:
    print(name.string)

#find_all(sting='검색어')-> 대소문자 구분
prince_list= soup.find_all(string='the prince')
print(prince_list)
print('the prince count: ', len(prince_list))

#children 추출
table_tag= soup.find('table', {'id': 'giftList'})
print('children 개수: ', len(list(table_tag.children)))

index=0
for child in table_tag.children:
    index+=1
    print(f'[{index}]: {child}')
    print('-'*30)
    