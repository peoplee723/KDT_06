# 원소/요소 변경하기 ->데이터 변경(수정),삭제

datas=[1,3,5,7,9,11]

#0번 원소를 100으로 변경하기
datas[0]=100
print(datas)

#0번 원소를 삭제하기
del datas[0]
print(datas)

# 0번부터 2번원소까지 자리에 삼 오 칠 변경
datas[:3]=['삼','오','칠']
print(datas)

# 100으로 변경
datas[:3]=[100]
print(datas)  #--->[100, 9, 11]

datas[:2]=[22,33,44,55,66,77,88,99]
print(datas)#->[22, 33, 44, 55, 66, 77, 88, 99, 11]

datas[:]=[]
print(datas)#---->[]

#여러개 원소를 삭제하기
datas[:]=[22,33,44,55,66,77,88,99,11]
del datas[:3]
print(datas)

