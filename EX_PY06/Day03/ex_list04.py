#list와 str

msg="Happy"

#str=> list형변환
datas=list(msg)
print(datas)#---['H', 'a', 'p', 'p', 'y']
msg=['Happy']
datas=list(msg)
print(datas) #->['Happy'] 리스트 안의 문자==자체로 1개의 원소
# 데이터 타입  
             #iterable->>반복 가능한 == 다음 원소를 읽을 수 있어야함
            # 3.14-> 3.14000, 03.14 ... 다음 원소 읽을 수x
            # sequence-->>여러개 data있어야함 순서o


