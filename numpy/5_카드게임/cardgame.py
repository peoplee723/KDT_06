from card import Card
from player import Player
from gamedealer import GameDealer

# 진행 순서
# 1. 카드 나누어 주기: n장
# 2. 딜러가 가진 카드 수 및 카드
# 3.흥부 카드 리스트
# 4. 놀부 카드 리스트
# 5. 흥부 카드 검사 및 리스트 
# 놀부 카드 검사 및 리스트
# 카드 나누어 주기, 카드 검사 반복
# 딜러가 가진 카드가 0 또는 플레이어 보유 카드가 0이면 게임 종료
def block():
    print('='*50)



def play_game():
    # 1. 플레이어 생성
    player1= Player('흥부')
    player2= Player('놀부')
    dealer= GameDealer()

    # 2. 카드 생성 + 섞기
    dealer.make_deck()
    dealer.shuffle_deck()

    # 3. 카드 전달 후 딜러 가드 출력
    player1.add_card_list(dealer.draw_card(10))
    player2.add_card_list(dealer.draw_card(10))
    
    dealer.show_deck()
    block()
    
    #4. 플레이어 카드 출력
    block()
    player1.display_tow_card_lists()
    block()
    player2.display_tow_card_lists()

    running=True
    while running:
        input('다음 단계 진행을 위해 Enter 키를 누르세요!')

        #4. 짝 맞는거 확인 및 이동
        pair_card= player1.check_one_pair_card()
        if pair_card:
            player1.open_card_list.extend(pair_card)
        block()
        player1.display_tow_card_lists()
        block()

        pair_card= player2.check_one_pair_card()
        if pair_card:
            player2.open_card_list.extend(pair_card)
        block()
        player2.display_tow_card_lists()
        block()
        if len(dealer.deck)==0 or len(player1.holding_card_list)==0 or len(player2.holding_card_list)==0:
            print('게임 종료')
            break
        else:
            player1.add_card_list(dealer.draw_card(4))
            player2.add_card_list(dealer.draw_card(4))
    
            dealer.show_deck()
            block()

    
# 1. 짝이 맞는 카드가 없을 때 X 숫자가 같은 카드가 3장 있을 때
# ValueError: list.remove(x): x not in list


# 2. 마지막 턴에서 딜러가 카드를 나눠줄 때
# 마지막 카드 줄때 오류
# IndexError: pop index out of range
# =>pop에서 인덱스를 부여하지 않고 랜덤으로 가져가도록 바꿈


if __name__ == '__main__':
    play_game()