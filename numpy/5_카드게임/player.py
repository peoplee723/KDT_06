# 1. 자신이 가지고 있는 리스트 2개 출력
# 2. 딜러에게 받는 카드는 hoding에 저장
# 3. 숫자 짝이 맞는 카드는 open으로 이동


class Player:
    def __init__(self, name):
        self.name= name
        self.holding_card_list= list()
        self.open_card_list= list()
    
    def __str__(self):
        '''
        객체를 문자열로 변환
        :return:
        '''
        return f'[{self.name}]'
    
    def add_card_list(self, card_list):
        '''
        카드 뽑는 함수
        params: card_list
        '''
        self.holding_card_list.extend(card_list)
    
    def display_tow_card_lists(self):
        '''
        holding_card_list와 open card_list 출력하는 함수
        '''
        num=1
        print([self.name],'Open card list:', len(self.open_card_list))
        for card in self.open_card_list:
            print(card, end=' ')
            if num%13== 0:
                print()
            num+=1
        num=1
        print()
        print([self.name], 'holding card list:', len(self.holding_card_list))
        for card in self.holding_card_list:
            print(card, end=' ')
            if num%13== 0:
                print()
            num+=1
        print('\n')
    
    def check_one_pair_card(self):
        '''
        짝이 맞는 카드가 있는지 확인+ 짝이 맞는 경우 open_card_list로 이동시키는 함수
        '''
        print(f'[{self.name}: 숫자가 같은 한쌍의 카드 검사]')
        hold= self.holding_card_list
        open=self.open_card_list
        pair=list()
        out_num=[]
        # 짝이 맞는지 확인-> 짝을 맞는 것을 확인하고 제거 + 
           #보류
        # for i in range(len(hold)):
        #     for j in range(len(hold)):
        #         if i not in (lambda x: x, out_num) and j not in (lambda x: x, out_num):
        #             if hold[i].number== hold[j].number and hold[i]!= hold[j]:
        #                 out_num.append(i)
        #                 out_num.append(j)
        #                 a= hold.pop(i)
        #                 b= hold.pop(j)
        #                 pair.append(a)
        #                 pair.append(b)
        for card in hold:
            for card2 in hold:
                if (card!= card2) and (card.number==card2.number) and (card not in pair):
                    hold.remove(card)
                    hold.remove(card2)
                    pair.append(card)
                    pair.append(card2)
        return pair
# hold 카드 리스트에서 숫자가 같은 것을 탐지-> 빼낼 방법?
        