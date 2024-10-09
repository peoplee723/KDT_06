#윷놀이 게임 프로그램

#1. 육가락 생성
# 1-1 윷가락을 저장할 리스트 생성[0,0,0,0]
# 1-2 윷 던질때 0,1값 생성 및 저장+ 점수계산(합계 ->3:도, 2:개, 3:걸 0:윷 5:모)

#2. 게임 종료 조건
# 2-1 20점 이상이면 게임 종료
# 2-2 20점 이상이면 모,윷이어도 게임종료

# 경기 순서 상관 없음

#3. 종료시
# 3-1 승패 결과 출력

# while True:
    # 흥부/놀부가 순서대로 윷 던짐 (순서는 range에서 홀수면 )
    # if 홀수: 흥부턴
        # if 윷 또는 모
            # 한번 더 던지기
        # if 점수가 20점 이상
            # 경기 종료
    #if 짝수: 놀부턴
         # if 윷 또는 모
            # 한번 더 던지기
        # if 점수가 20점 이상
            # 경기 종료
import random as rd
import numpy as np

class player:
    def __init__(self,pname,pscore):
        self.pname=pname
        self.pscore=pscore

    def displayInfo(self, pname, pscore):
        print(self. pname)
        print(self. pscore)

    def player_score(self, num):
        pscore+=num
        return pscore
    

#선수 생성
P1= player('흥부',0)
P2= player('놀부',0)

# 윷가락 생성   (1==앞면{xxx}, 0==뒷면)
plate= [0,0,0,0]


# 던진 결과에 따른 점수 생성
def plate_result():
    if plate.count(1)==3: #도
        print('도')
        score+=1
        one_more=False
        return 1
    elif plate.count(1)==2: #개
        print('개')
        score+=2
        one_more=False
        return 2
    elif plate.count(1)==3: #걸
        print('걸')
        score+=3
        one_more=False
        return 3
    elif plate.count(1)==4: #모
        print('모')
        score+=5
        one_more=True
        return 5
    elif plate.count(0)==4: #윷
        print('윷')
        score+=4
        return 4
        one_more=True

# 윷 던지기
for j in range(4):
    plate[j]=rd.randrange(2)
#두 선수가 번갈아 가면서 던진 결과(점수)를 가져가기
for i in range(1,101):

    if i%2==0:
        #흥부가 윷 던짐
        one_more=False
        score=0
        plate_result()
        while one_more== True:  #윷 또는 모일때 한번 더 던짐
            plate_result()
        player(score)                  #던진 결과를 점수에 추가
        if P1.pscore>=20:
            break
    if i%2!=0:
        #놀부가 윷을 던짐
        one_more=False
        score=0
        plate_result()
        while one_more== True:  #윷 또는 모일때 한번 더 던짐
            plate_result()
        player(score)                  #던진 결과를 점수에 추가