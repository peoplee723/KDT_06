from urllib.parse import urlparse

urlString= 'https://shopping.naver.com/home/p/index.naver'

url= urlparse(urlString)
print(url.scheme)
print(url.netloc)
print(url.path)
