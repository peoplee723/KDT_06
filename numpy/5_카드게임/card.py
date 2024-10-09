class Card:
    def __init__(self, card_suit, card_number):
        self.suit= card_suit
        self.number= card_number
    
    def __str__(self):
        '''
        객체를 문자열로 변환
        :return:
        '''
        return f'({self.suit}, {self.number:>2})'
        