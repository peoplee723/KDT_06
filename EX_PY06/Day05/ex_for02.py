#제어문 ->반복문

# 실습 -> 문자열을 기계어, 즉 2진수로 변환해서 저장하기
# 입력-> Hello
# 출력-> 2진수(0101010110110)
word="hello"
result=''
for i in word:
    result=result+bin(ord(i))[2:]   #합은 이어붙이기->빈 공간 
                                    #만들어서 삽입(리스트는 +연산자 안됨!!!)
print(type(result))
print(result)

#실습-> 원소/요소의 인덱스와 값을 함께 가져오기
nums=[1,3,5]
for n in nums:      #원소 데이터만 가져옴
    print(n)

#인덱스와 원소 데이터 가져오기
for e in enumerate(nums):
    print(e)
##enumerate ->원소의 인덱스와 데이터를 한쌍으로 묶어서 튜플 형태로
# # (0, 1)    #가져옴
# (1, 3)
# (2, 5)
for idx, n in enumerate(nums):
    print(idx, n)
#언패킹을 통해 인덱스, 데이터 따로 저장 가능

#range -> range를 통해 인덱스 값을 찾았음

num=[11,33,55]
for e in enumerate(num):
    print(e[0], e[1])
    num[e[0]]=int(e[1])    #==>튜플은 가독성이 떨어짐(원소in 원소)

for idx, n in enumerate(num):
    print(idx, n)
    num[idx]=int(n)         #==>가독성 나아짐