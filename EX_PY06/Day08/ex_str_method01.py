#str 데이터 타입 전용 함수, 즉 메서드 살펴보기

msg='Hello 0705'

#원소/요소 인덱스 찾기 메서드 - find(문자1개 또는 문자열)
# H의 인덱스
idx=msg.index('H')           #인덱스값 반환
print(f'H의 인덱스: {idx}')

# 7의 인덱스
idx=msg.index('7')
print(f'7의 인덱스: {idx}')

# llo의 인덱스
idx=msg.index('llo')
print(f'llo의 인덱스: {idx}')  #문자열의 경우 시작위치 반환

# LLO의 인덱스
# msg='Hello'
idx=msg.find('llO')
print(f'llO의 인덱스: {idx}')  #존재하지 않으면 -1도출

msg='Hello 0705'
# H의 인덱스
idx=msg.index('H')           
print(f'H의 인덱스: {idx}')


# h의 인덱스
if 'h' in msg:
    idx=msg.index('H')        #인덱스는 없으면 ERROR           
    print(f'H의 인덱스: {idx}')
else: print(f'존재하지 않는 글자입니다.')

# 문자열에 동일한 문자가 여러개 존재하는 경우
msg='Good Luck Good'
# o의 인덱스 찾기 =>첫번째 o 인덱스
idx=msg.find('o')
print(f'o의 인덱스: {idx}')
#두번째 o
idx=msg.find('o',idx+1)
print(f'두번째 o의 인덱스: {idx}')
i=-1
idx=0
while i+1<msg.count('o'):
    idx=msg.find('o',idx+1)
    i+=1
    print(f'{i+1}번째 o의 인덱스: {idx}')


# 문자열의 뒷부분부터 찾기하는 메서드 
# ==>rfind(문자, 시작점, 끝점+1), rindex()
msg="Happy"

#p 인덱스 찾기
idx= msg.rfind('p')
print(f'p의 인덱스 {idx}')

#p 두번째 인덱스 찾기
idx= msg.rfind('p', 0, idx)  #인덱스 0~idx-1 사이의 인덱스 찾기
print(f'p의 인덱스 {idx}')   #단, 뒤에서 부터 

#파일명에서확장자 txt,jepg, xlsx, zip 찾기
files= ['hello.txt', '경제분석.doc', 'kakao_123465789.jpg']
list=[]
for f in files:
    x=f.find('.')
    list.append(f[x+1:])
print(list)

#dic로 만들면?

files= ['hello.txt', '경제분석.doc', 'kakao_123465789.jpg']
list=[]
name=[]
dic={}
for f in files:
    x=f.find('.')
    list.append(f[x+1:])
    name.append(f[:x])
dic=tuple(zip(name,list))
print(list)
print(dic,type(dic))