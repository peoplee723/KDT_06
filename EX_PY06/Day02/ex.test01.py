#입력 & 출력 실습

#실습1. 데이터 저장 및 변수생성 그리고 출력
#- 생년월일
#- 띠
#- 별자리
#- 혈액형
#- 
birth= '2000년 07월 23일'
El= '용띠'
star= '쌍둥이자리'
blood= 'A'
print('나는 %s %s입니다'%(birth, El))
print(F'혈액형은 소심한 {blood}형 입니다')
#---------------------------------------

#실습2. 입력 받은 데이터 저장 단, 파일로 저장
#- 좋아하는 계절
#- 좋아하는 나라
#- 여행가고 싶은 나라
#-
nara1=input("좋아하는 나라:")
season=input("종아하는 계절")
nara2=input("여행하고 싶은 나라")
TRAVEL= 'travel.txt'
f=open(TRAVEL, mode='w', encoding='utf-8')
f.write(season)
f.write('\n')#f.write 사용시 줄 바꾸고 싶으면 일일이 넣어야함
f.write(nara1)
f.write('\n')
f.write(nara2)
f.close()
#print 사용하면 자동으로 줄 바꿔줌+ 형태 바꾸기도 쉬움
#but, 마지막에 줄바꿈 사용됨
print(f'좋아하는 나라: {nara1}',file=f)
print(f'좋아하는 계절: {season}',file=f)
print(f'여행하고 싶은 나라: {nara2}',file=f,end='')#빈줄 없애기 위해