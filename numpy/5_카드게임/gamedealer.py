from card import Card
import random


# 1. deck()에 카드 52장 생성
# 2. deck에서 10장씩 각 플레이어에게 전달
#    (생성된 덱 셔플 -> 덱 나눠준 만큼 삭제+ 플레이어에게 생성)
# 3. 딜러가 가지고 있는 카드 목록 출력

class GameDealer:
    def __init__(self):
        self.deck=[]
        self.suit_number= 13
    
    def	make_deck(self):
        '''
        카드를 생성하는 함수
        return: none
        '''
        card_suits= ["♠","♥","♣","◆"]
        card_numbers= ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        deck= self.deck
        for suit in card_suits:
            for num in card_numbers:
                card= Card(suit, num)
                deck.append(card)

    def sort_draw(self,num):
        '''
        시험용-> 같은 숫자 3장이 나오도록 처리
        '''
        false_draw=[]
        for i in range(num-7):
            false_draw.append(self.deck.pop(i*(13)))
        for i in range(num-3):
            false_draw.append(self.deck.pop())
        return false_draw

    def shuffle_deck(self):
        '''
        생성된 카드를 섞는 함수
        '''
        random.shuffle(self.deck)

    
    def show_deck(self):
        '''
        현재 카드를 출력하는 함수
        '''
        print(f'[GameDealer] 딜러가 가진 카드 수: {len(self.deck)}')
        num=1
        for card in self.deck:
            print(card, end=' ')
            if num%13== 0:
                print()
            num+=1
        print()

    def draw_card(self,num):
        '''
        덱에서 카드를 뽑는 함수
        params: num
        return: card_list
        '''
        a=list()
        limit=1
        if num<=len(self.deck):
            for i in range(num):
                draw= self.deck.pop()
                a.append(draw)
        return a


# dealer= GameDealer()
# dealer.make_deck()
# for card in dealer.deck:
#     print(card)
# print(dealer.deck[0])
# -> 인덱싱, for문 추출 가능

# +pop()인덱스 부여 안했을때 랜덤으로 뽑음


