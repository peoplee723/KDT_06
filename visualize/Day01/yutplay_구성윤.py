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
            # 한번 더 던지기   (근데 20점 이상이면 종료해야하기 때문에 던진 결과에 따른 점수를 바로바로 추가시켜야 함)
        # if 점수가 20점 이상
            # 경기 종료
    #if 짝수: 놀부턴
         # if 윷 또는 모
            # 한번 더 던지기
        # if 점수가 20점 이상
            # 경기 종료
import random as rd
class player:
    def __init__(self,pname,pscore):
        self.pname=pname
        self.pscore=pscore

    def player_score(self, num):
        self.pscore+=num
    

#선수 생성
P1= player('흥부',0)
P2= player('놀부',0)

# 윷가락 생성   (1==앞면{xxx}, 0==뒷면)
plate= [0,0,0,0]

# 무조건 윷을 던지는 함수
def onemore(bool):
    one_more=bool
def plate_cheat(player_name):
           # 윷 던지기
    for j in range(4):
        plate=[1,1,1,1]
    if plate.count(1)==4: #모
        print('모! 한번더!')
        player_name.player_score(5)
        if player_name.pscore>=20:
                print(f'{player_name.pname}가 {player_name.pscore}점으로 승리!')
        else: plate_cheat(player_name)
        one_more=True
   
    elif plate.count(0)==4: #윷
        print('윷!, 한번더!')
        player_name.player_score(4)

        one_more=True

# 던진 결과에 따른 점수 생성 및 점수 추가
def plate_result(player_name):
           # 윷 던지기  ------------>리스트에 점수와 결과를 담고 (모 제외) 
                                    # 인덱싱으로 출력하면 코드 줄일 수 있음!
    for j in range(4):
        plate[j]=1
        plate[j]=rd.randrange(2)
    score=0
    if plate.count(1)==3: #도          
        print(f'도, 총점: {player_name.pscore}')
        score=1
        if player_name.pscore>=20:
                print(f'{player_name.pname}가 {player_name.pscore}점으로 승리!') #승리 도출
        player_name.player_score(1)  #점수 추가
    elif plate.count(1)==2: #개
        print(f'개 , 총점: {player_name.pscore}')
        score=2
        player_name.player_score(2)
        if player_name.pscore>=20:
                print(f'{player_name.pname}가 {player_name.pscore}점으로 승리!')
    elif plate.count(1)==1: #걸
        print(f'걸 , 총점: {player_name.pscore}')
        score=3
        player_name.player_score(3)
        if player_name.pscore>=20:
                print(f'{player_name.pname}가 {player_name.pscore}점으로 승리!')
    elif plate.count(0)==4: #윷
        score=4
        print(f'윷!, 한번더!, 총점: {player_name.pscore}')
        player_name.player_score(4)
        if player_name.pscore>=20:
                print(f'{player_name.pname}가 {player_name.pscore}점으로 승리!')
        else: plate_cheat(player_name)   
    elif plate.count(1)==4: #모
        print(f'모!, 한번더!, 총점: {player_name.pscore}')
        score=5
        player_name.player_score(5)
        if player_name.pscore>=20:
                print(f'{player_name.pname}가 {player_name.pscore}점으로 승리!')
        else: plate_cheat(player_name)
    
   

# # 윷 던지기
# for j in range(4):
#     plate[j]=rd.randrange(2)
#두 선수가 번갈아 가면서 던진 결과(점수)를 가져가기
def Game_start(state):
    for i in range(1,101):

        if i%2!=0:
            print('흥부턴')
            #흥부가 윷 던짐
            
            
            plate_cheat(P1)  if state== 'cheat' else plate_result(P1)
            if P1.pscore>=20:
                break
                        
        if i%2==0:
            print('놀부턴')
            #놀부가 윷을 던짐
            plate_cheat(P1)  if state== 'cheat' else plate_result(P1)
            if P2.pscore>=20:
                break
        if P2.pscore>=20 or P1.pscore>=20:
            break
Game_start('')
#'cheat' 입력시 항상 모가 나옴, 그 외에는 랜덤으로 윷 생성