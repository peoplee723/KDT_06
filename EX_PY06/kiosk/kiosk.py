#키오스크
# 필요한 조건
# 햄버거 선택 -> 추가,제거 재료 선택-> 햄버거 선택..... 햄버거 선택 창에서 결제 ->배달, 포장 선택 ->결제수단 선택 ->주문표 및 영수증 출력

# 전체-> 정해진 범위 내의 숫자만 입력하기(정수+메뉴의 범위만큼)
        # 공백오류, 특수문자 오류
def check_data(data, data_cnt):
    data = data.split()              #리스트변환                
    if data_cnt == len(data) :       #데이터수 체크
        isok=True
        for d in data:
            if not d.isdecimal():
                isok=False
        return isok
        if data[0].isdecimal and data[1].isdecimal:
            return True               #숫자인지 체크
        else:
            return False
    else:
        return False

# 검증된 데이터를 바탕으로 출력하기
def talk_data(check_data):
    if check_data(choice, 1):
        choice= int(choice)
    else: print('올바른 번호를 입력해 주세요')



# 0(메인화면) ->1주문 ->1.2 메뉴선택(메뉴당 재료추가+제거 옵션, 선택한 메뉴 보여주기 및 선택한 메뉴 제거)
                # ->1.3 ->포장, 매장식사 선택 -> 포인트 적립여부 묻기-> 결제 -> 영수증 출력여부->영수증 및 번호표 출력
            # -->직원호출시 기다려 달라는 문구

# 메인화면 ->(1. 주문하기    2.직원호출)

def print_main_menu():
    print(f'{"*":*^19}')
    print(f'{"     버  거  킹":19}')
    print(f'{"*":*^19}')
    print(f'{"*  1  주문  하기  *":19}')
    print(f'{"*":*^19}')
    print(f'{"*  2  직원  호출  *":19}')
    print(f'{"*":*^19}')

# 주문 화면  --글자 + :17==19가 되도록
def print_menu():
    print(f'{"*":*^19}',end=' '), print(f'{"*":*^19}')
    print(f'{"*  1  와     퍼   *":17}',end=' '), print(f'{"*  2  불고기 와퍼 *":12}')
    print(f'{"*":*^19} {"*":*^19}')
    print(f'{"*  3  치즈  와퍼  *":15}',end=' '), print(f'{"*  4  통새우 와퍼 *":13}')
    print(f'{"*":*^19} {"*":*^19}')
    print(f'{"*  5  불고기 버거 *":14}',end=' '), print(f'{"*  5  치즈  버거  *":19}')
    print(f'{"*":*^19} {"*":*^19}')
    print(f'{"*":*^19} {"*  6  결     제   *":19}')
main_menu=[_, '와퍼','불고기 와퍼', '치즈 와퍼', '통새우 와퍼', '불고기 버거',' 치즈버거' ]
order=[]

# 1->wp, 2-> bw, 3-> cw, 4->sw, 5->bb, 6->cb

# 1-1. 햄버거 선택시 추가/제거 선택 화면
def print_addition_():
    print(f'{"*":*^19}')
    print(f'{"*  1  재료  추가  *":19}')
    print(f'{"*":*^19}')
    print(f'{"*  2  재료  빼기  *":19}')
    print(f'{"*":*^19}')
    print(f'{"*  2  선택  안함  *":19}')
    print(f'{"*":*^19}')
# 1-2. 재료 추가 화면
def print_adddtion_1():
    print(f'{"*":*^19} {"*":*^19}',)
    print(f'{"*  1  패티  추가  *":15} {"*  2  양상추 추가 *":14}')
    print(f'{"*":*^19} {"*":*^19}')
    print(f'{"*  3  치즈  추가  *":15} {"*  4  토마토 추가 *":14}')
    print(f'{"*":*^19} {"*":*^19}')
    print(f'{"*  5  계속  담기  *":15} {"*  6  뒤로  가기 *":15}')
   
# 1->pat, 2->cab, 3-> che, 4->tom, 


# 키오스크 시작
while True:
    print_main_menu()       #메인 화면
    choice = (input('메뉴 선택: '))
    if check_data(choice, 1):
        choice= int(choice)
    else: print('올바른 번호를 입력해 주세요');continue
    if choice==1:
        while True:
            print_menu()
            choice= input('메뉴를 선택해 주세요') #1-버거 선택
            if check_data(choice, 1):
                choice= int(choice)
            else: print('올바른 번호를 입력해 주세요');continue
            if choice<6:
                order.append(main_menu[choice])
                print_addition_()      #1-1재료 추가/제거 선택
                choice= input('메뉴를 선택해 주세요')
                if check_data(choice, 1):
                    choice= int(choice)
                else: print('올바른 번호를 입력해 주세요');continue
                if choice ==1:
                    while True:
                        print_adddtion_1()    #1-2재료 추가 화면
                        extra= input('메뉴를 선택해 주세요')
                        if check_data(extra, 1):
                            choice= int(extra)
                        else: print('올바른 번호를 입력해 주세요');continue
                        if choice== 1:
                            pass
                        
                            

                    


    