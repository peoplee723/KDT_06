from urllib.request import urlopen
from bs4 import BeautifulSoup

html= urlopen('http://www.pythonscraping.com/pages/page3.html')
soup= BeautifulSoup(html, 'html.parser')

#children 추출
table_tag= soup.find('table', {'id': 'giftList'})
print('children 개수: ', len(list(table_tag.children)))

index=0
for child in table_tag.children: #\n도 child로 인식
    index+=1
    print(f'[{index}]: {child}')
    print('-'*30)

#descendants(자손)
desc= soup.find('table', {'id': 'giftList'}).descendants
list_desc=list(desc)
print('descendants 개수: ', len(list_desc))

for tag in list_desc:
    print(tag)

# next_siblings(형제) 속성
for sibling in soup.find('table', {'id': 'giftList'}).tr.next_siblings:
    print(sibling)
    print('-'*30)

#previous_siblings 속성
print('previous_siblings')
for sibling in soup.find('tr', {'id':'gift2'}).previous_siblings:
    print(sibling)

#next/previous_sibling -> tag 하나만 반환
sibling1= soup.find('tr', {'id': 'gift3'}).next_sibling
print('sibling1:', sibling1)
print(ord(sibling1)) #문자 unicode 정수 반환
#-> 다음 tag가 \n이라 공백이 나옴

#next.next사용
sibling2= soup.find('tr', {'id':'gift3'}).next_sibling.nextSibling
print(sibling2)

#parent 사용
style_tag= soup.style
print(style_tag.parent)

#.parent
img1= soup.find('img', {'src': '../img/gifts/img1.jpg'})
text= img1.parent.previous_sibling.get_text()
print(text)

