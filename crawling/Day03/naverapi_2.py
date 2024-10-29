import urllib.parse
import urllib.request
import datetime
import json

def get_request_url(url):
    client_id= 'vAcuTP8HYLTwb34u12a0'
    client_secret= 'NwFeqYc5YY'

    req= urllib.request.Request(url)
    req.add_header('X-Naver-Client-Id', client_id)
    req.add_header('X-Naver-Client-Secret', client_secret)

    try:
        response= urllib.request.urlopen(req)
        if response.getcode() ==200:
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print(f'Error for URL: {url}')

def get_naver_search(node, search_text, start, end, display):
    base= "https://openapi.naver.com/v1/search"
    node= f'/{node}.json'
    query_string= f'{urllib.parse.quote(search_text)}'

    parameters= ('?query={}&start={}&end={}&display={}'.
                 format(query_string, start, end, display))
    url= base+ node+ parameters
    response= get_request_url(url)

    if response is None:
        return None
    else:
        return json.loads(response)

def main():
    node= 'kin' #크롤링 대상
    search_text= '홈택스'
    cnt= 0

    json_response= get_naver_search(node, search_text, 1, 1000,100)
    if (json_response is not None) and (json_response['display'] !=0):
        for post in json_response['items']:
            cnt+=1

            print(f'[{cnt}]', end=' ')
            print(post['title'])
            print(post['description'])
            # print(post['originallink'])
            print(post['link'])
            # print(post['pubDate'])

if __name__ == '__main__':
    main()

