import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

link='https://finance.naver.com/item/main.naver?code='
company_dict={'삼성전자': '005930', 'SK하이닉스': '000660', 'LG에너지솔루션': '373220',
              '삼성바이오로직스': '207940', '현대차': '005380', '삼성전자우': '005935',
              '셀트리온': '068270', '기아': '000270', 'KB금융': '105560',
              '신한지주': '055550'}
company_list=list(company_dict.items())
stack_list=[]
stack_columns= ['이름', '번호', '현재가', '전일가', '시가', '고가', '저가']
for company in (company_dict.keys()):
    stack=[]
    html=urlopen(f'https://finance.naver.com/item/main.naver?code={company_dict[company]}')
    bs= BeautifulSoup(html, 'html.parser')
    table=bs.find('div', { 'class' : 'rate_info'})
    name= company
    num= company_dict[company]
    today= bs.find_all('span', {'class': 'blind'})[-10].text
    yesterday= bs.find_all('span', {'class': 'blind'})[-7].text
    siga= bs.find_all('span', {'class': 'blind'})[-3].text
    high= bs.find_all('span', {'class': 'blind'})[-6].text
    low= bs.find_all('span', {'class': 'blind'})[-2].text
    stack_list.append([name, num, today, yesterday, siga, high, low])

company_list=list(company_dict)
def main_menu():
    print('-'*30)
    print('[네이버 코스피 상위 10대 기업 목록]')
    print('-'*30)
    for i in range(10):
        print(f'[{i+1:>2}] {company_list[i]}')

def run_compnay():
    while True:
        main_menu()
        choice= int(input('주가를 검색할 기업의 번호를 입력하세요(-1: 종료): '))
        if choice==-1:
            break
        elif 1<=choice<=10:
            print(link+stack_list[choice-1][1])
            print(f'종목명: {stack_list[choice-1][0]}')
            print(f'종목코드: {stack_list[choice-1][1]}')
            print(f'현재가: {stack_list[choice-1][2]}')
            print(f'전일가: {stack_list[choice-1][3]}')
            print(f'시가: {stack_list[choice-1][4]}')
            print(f'고가: {stack_list[choice-1][5]}')
            print(f'저가: {stack_list[choice-1][6]}')

run_compnay()       
            
            
            
            
