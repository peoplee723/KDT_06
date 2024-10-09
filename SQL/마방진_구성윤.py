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

# while True:
#     size= int(input ('홀수 배열의 크기를 입력하세요'))
#     if size%2 ==0:
#         print(f'{size}는 홀수가 아닙니다, 다시 입력해 주세요') #오류 출력+ 다시 입력
#     else: break
size=3
#배열 출력
# for i in range(size):
#     square.append([])
#     for j in range(size):
#         square[i].append(0)    #--->[]가 하나 더 있음
matrix= [[0 for col in range(size)] for row in range(size)]


def out_box(y, x): #범위를 벗어났을때 이동 경로 수정
    #y(행) 가 0보다 작을때 맨 아래로 이동
    if y<0:
        y=size-1
    # x가 크기보다 클때 0으로 이동
    if x>size:
        x=0
def down(y,x):
    pass
    # 이미 위치에 숫자가 있을때 아래로 이동


#가운데에서 시작    (인덱싱은 0부터 시작!!!!!!) -> y,x
y= 0            #(행)
x=size//2        #(열)
#시작 번호
count=1
# matrix[x][y]= count
# print(matrix[x][y])
end=False
#1. 시작지점 설정 (가운데, 0)
matrix[y][x]=1
print(matrix)
while end== False:
    # 정상적 진행 -> y,x -> y-1, x+1
    y-=1
    x+=1
    #y(행) 가 0보다 작을때 맨 아래로 이동
    if y<0:
        y=size-1
        if matrix[y][x]>0:
            y+=2
            x-=1

    # x가 크기보다 클때 0으로 이동
    if x>size-1:
        x=0
        if matrix[y][x]>0:
            y+=2
            x-=1

    # 위치에 숫자가 있을때 아래로 이동
    if matrix[y][x]>0:
        y+=2
        x-=1

        if matrix[y][x]>0:
            y+=2
            x-=1
    matrix[y][x]=count #조건 거친 후 입력
    print(matrix)

# print(matrix)