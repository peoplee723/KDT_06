#홀수차 마방진 생성


# 0. 입력받은 크기만큼 홀수차 배열 생성
# + 짝수 입력시 오류 출력+ 다시 입력할수 있도록
# 1. 시작위치는 무조건 가운데 열 (열 개수 /2 +1)
# 2. 다음 위치는 오른쪽 대간선 방향으로 이동
# 2-1. y축 방향으로 범위 벗어나면 
#       ->마지막 행으로 이동
# 2-2. x축 방향으로 범위 벗어나면   
#       ->첫째 열으로 이동
# 2-3. 다음 이동 위치에 이미 값이 있으면
    #   -> 아래로 이동




#배열 입력
#3*3 예시
# square= 열   0    1   2
#    행   0 ([ [], [], [] ] ,
#         1  [ [], [], [] ],
#         2  [ [] ,[], [] ])
square=[]
# 홀수 배열 입력
while True:
    size= int(input ('홀수 배열의 크기를 입력하세요'))
    if size%2 ==0:
        print(f'{size}는 홀수가 아닙니다, 다시 입력해 주세요') #오류 출력+ 다시 입력
    else: break
#배열 출력
# for i in range(size):
#     square.append([])
#     for j in range(size):
#         square[i].append(0)    #--->[]가 하나 더 있음
matrix= [[0 for col in range(size)] for row in range(size)]

# 마방진을 출력하는 함수
def show_matrix(size):
    for i in range(size):
        for j in range(size):
            print(f'{matrix[i][j]:>3}',end=' ') 
            if j>=size-1:
                print()
    print('----------------')



def out_box(y, x): #범위를 벗어났을때 이동 경로 수정
    #y(행) 가 0보다 작을때 맨 아래로 이동
    if y<0:
        y=size-1
    # x가 크기보다 클때 0으로 이동
    if x>size:
        x=0
def down(y,x):
    if matrix[y][x]>0:
        y+=2
        x-=1

    # 이미 위치에 숫자가 있을때 아래로 이동


#가운데에서 시작    (인덱싱은 0부터 시작!!!!!!) -> y,x
y= 0            #(행)
x=size//2        #(열)
#시작 번호
count=1
end=False
#1. 시작지점 설정 (가운데, 0)
matrix[y][x]=1
show_matrix(size)
while end== False:
    count+=1
    # 정상적 진행 -> y,x -> y-1, x+1
    y-=1
    x+=1
    # 범위를 벗어나서 이동한 장소에 숫자가 있을 경우 이동 취소+아래로 이동
    if y<0 and x>=size and matrix[size-1][x*0]>0:
        y+=2; x-=1
    #y(행) 가 0보다 작을때 맨 아래로 이동
    if y<0:     
        y=size-1
     # x가 크기보다 클때 0으로 이동
    if x>=size:
        x=0
        if matrix[y][x]>0:
            y+=2
            x-=1
    # 위치에 숫자가 있을때 아래로 이동
    if matrix[y][x]>0:
        y+=2
        x-=1
        #이동 후 범위 벗어날 경우 이동
        if y<0:
            y=size-1
        if x>size:
            x=0
    matrix[y][x]=count #조건 거친 후 입력
    show_matrix(size)
    if count==size*size:
        end= True
# x=2, y=1 ->



# 오른쪽 대각선 이동 값을 다른 변수로 저장
# ->이미 값이 있는 경우 오른쪽 대각선 이동 안하고 아래로 이동해야하기 때문
# +out of range 오류 최소화 가능?