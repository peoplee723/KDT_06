#제어문 ->반복문
# -유사하거나 동일한 코드를 1번 작성으로 재사용하기 위한 방법
# 종류-> for, while

#for 반복문
#시퀀스(이터러블) 데이터에서 원소/요소를 하나씩 읽어올 때 사용
# 형식
# for 명수명 in 시퀀스/이터러블데이터:
# ----반복실행될 코드

#실습 -> 문자열에서 문자를 1줄에 1개씩 출력하기
msg="Merry christmas 2025"
print(msg[0])  #-> 19번 적어야됨 (매우귀찮) 

for m in msg:     #->m=msg[0], 1, 2 을 저잘...끝원소까지 반복
    print(m, ord(m), end='')
print('END')

#실습-> 리스트에서 원소를 하나씩 읽어오기
#1~100 번위에서 3의 배수만 저장한 리스트
data=list(range(3,101,3))

for d in data:
    print(d, end=' ')
print('END')

#실슴-> str 타입의 원소를 가지는 리스트 입니다.
# 해당 원소를 정수로 형변환 시켜서 저장해 주세요
data=['4','9','13','12','8']  #리스트 안 원소 형변환 
                          #->일일이 인덱싱 해서 변환해야함(매우 귀찮)

for d in data:    #원래 원소의 값을 변경해야 하는 경우는 인덱스 필요!!      
    int(d)        #원소 개수를 알면 인덱스 범위를 알 수 있음

for idx in range(len(data)):   #원소의 개수만큼 범위 지정
    print(f'idx => {idx}')     #여기서 idx의 범위는 0~4
    data[idx]=int(data[idx])   #
print(data)