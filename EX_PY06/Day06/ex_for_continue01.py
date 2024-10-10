#반복문과 컨티뉴
# continue 구문을 만나면 구문 아래 코드 실행x
# - 반복문으로 가서 다음 요소 데이터를 가지고 진행
# 3의 배수인 경우만 화면에 출력하세요

data=list(range(1,51))

for d in data:
    if d%3==0:
        print(d)

for d in data:
    if d%3: continue           ##조건이 참일때 아래 구분 전부 실행 안함
    print(d)                   ##->3의 배수가 아닌 경우 참이라 print(d) 실행 안함
    print(d)
    print(d)