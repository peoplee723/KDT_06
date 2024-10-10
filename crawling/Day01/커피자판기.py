#파이썬 커피 자판기 프로그램

# 1. 모든 커피의 가격은 300원 + 소모하는 재료는 상이
# 2. 재료는 딕셔너리 형태
# 3. 종료 선택시 남은 돈 반환

# 딕셔너리 구현
# 자판기 내부 동전 (커피 구매에 따라 300원씩 증가)
# 물 500ml
# 커피 100g, 프림 100g, 설탕 100g, 종이컵 5개

# 동전 투입 (300원 미만일 경우 돈 반환)-> 메뉴 출력 (블랙, 프림, 설탕 프림), 재료 현황, 종료 -> 메뉴 선택시 재료 충분한 경우 제공 및 재료
# 변동 사항 업데이트

class VendingMachine:
    def __init__(self, input_dict):
        
        self.input_money = 0
        self.inventory= input_dict


    


    def black(self): #메뉴 고를시 소모되는 것들
        coffee_machine.inventory['coffee']-=30
        coffee_machine.inventory['water']-= 100
        coffee_machine.inventory['cup']-= 1
        coffee_machine.inventory['change']+=300
    
    def cream(self):
        coffee_machine.inventory['coffee']-= 15
        coffee_machine.inventory['cream']-= 15
        coffee_machine.inventory['water']-= 100
        coffee_machine.inventory['cup']-=1
        coffee_machine.inventory['change']+=300
    
    def sugar_cream(self):
        coffee_machine.inventory['coffee']-=10
        coffee_machine.inventory['cream']-=10
        coffee_machine.inventory['sugar']-=10
        coffee_machine.inventory['water']-=100
        coffee_machine.inventory['change']+=300

    def menu(self, coin):
        '''
        메뉴판 호출
        param= coin
        '''
        print('-'*30)
        print(f' 커피자판기 (잔액: {coin})')
        print('-'*30)
        print('1. 블랙 커피')
        print('2. 프림 커피')
        print('3. 설탕 프림 커피')
        print('4. 재료 현황')
        print('5. 종료')
    
    def choose_coffee(self,choice, coin):
        '''
        재료가 남아있는지 체크(bool)하고 재료가 있을시 커피를 주문
        params= choice
        '''
        coffee= self.inventory.get('coffee')
        cream= self.inventory.get('cream')
        sugar= self.inventory.get('sugar')
        water= self.inventory.get('water')
        cup= self.inventory.get('cup')

        if cup>=1 and water>=100:
            if choice==1:
                if coffee>=30:
                    coffee_machine.black()
                else: return False
            elif choice==2:
                if coffee>=15 and cream>=15:
                    coffee_machine.cream()
                else: return False
            elif choice==3:
                if coffee>=10 and cream>=10 and sugar>=10:
                    coffee_machine.sugar_cream()
                else: return False
    def not_enough_res(coin):
        '''
        재료 부족 문구 호출 및 작동 종료
        param=coin
        '''
        print('재료가 부족합니다.')   #메뉴에 상응하는 재료가 없을 경우 자판기 종료
        print('-'*30)
        print(f'{coin}원을 반환합니다')
        print('-'*30)
        print('커피 자판기 작동을 종료합니다')


    def run(self):   #자판기 시작
        #1. 동전 투입
        running= True

        while running:
            while True:
                coin= int(input('동전을 투입하세요: '))
                if coin<300:
                    print(f'투입된 돈 ({coin}원)이 300원보다 작습니다.')
                else: break
            while True:
                coffee_machine.menu(coin)
                choice= int(input('메뉴를 선택하세요: '))

                if choice<1 or choice>5:
                    print('올바른 메뉴를 선택해 주세요')
                elif choice==1:
                    if coffee_machine.inventory['coffee']<30 or coffee_machine.inventory['water']< 100 or coffee_machine.inventory['cup']< 1:
                        coffee_machine.not_enough_res()
                        running= False
                        break
                    else:
                        coin-=300
                        print(f'블랙 커피를 선택하셨습니다. 잔액:{coin}')
                        print('-'*30)
                        coffee_machine.black()
                        print(f'재료 현황: {coffee_machine.inventory}')
                elif choice==2:
                    if coffee_machine.inventory['coffee']<15 or coffee_machine.inventory['cream']<15 or coffee_machine.inventory['water']< 100 or coffee_machine.inventory['cup']< 1:
                        print('재료가 부족합니다.')   #메뉴에 상응하는 재료가 없을 경우 자판기 종료
                        running=False
                        print('-'*30)
                        print(f'{coin}원을 반환합니다')
                        print('-'*30)
                        print('커피 자판기 작동을 종료합니다')
                        break
                    else:
                        coin-=300
                        print(f'프림 커피를 선택하셨습니다. 잔액:{coin}')
                        print('-'*30)
                        coffee_machine.cream()
                        print(f'재료 현황: {coffee_machine.inventory}')
                elif choice==3:
                    if (coffee_machine.inventory['coffee']<10 or coffee_machine.inventory['cream']<10 or coffee_machine.inventory['sugar']<10 
                        or coffee_machine.inventory['water']< 100 or coffee_machine.inventory['cup']< 1):
                        print('재료가 부족합니다.')   #메뉴에 상응하는 재료가 없을 경우 자판기 종료
                        running=False
                        print('-'*30)
                        print(f'{coin}원을 반환합니다')
                        print('-'*30)
                        print('커피 자판기 작동을 종료합니다')
                        break
                    else:
                        coin-=300
                        print(f'설탕 프림 커피를 선택하셨습니다. 잔액:{coin}')
                        print('-'*30)
                        coffee_machine.sugar_cream()
                        print(f'재료 현황: {coffee_machine.inventory}')
                elif choice==4:
                    print(f'재료 현황: {coffee_machine.inventory}')
                elif choice==5:
                    running= False
                    print('-'*30)
                    print(f'{coin}원을 반환합니다.')
                    print('-'*30)
                    print('커피 자판기 동작을 종료합니다')
                    print('-'*30)
                    break


            
inventory_dict= {'coffee': 100, 'cream': 100, 'sugar': 100,
                 'water': 500, 'cup': 5, 'change': 0}
coffee_machine= VendingMachine(inventory_dict)
coffee_machine.run()

#각각의 기능(메뉴 호출, 재료 소모, 재료 현황 보여주기 등)을 메소드로 구현하기!!