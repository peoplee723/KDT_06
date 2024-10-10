#내장함수 range()
# 숫자 범위를 생성하는 내장함수
#형식: range(시작숫자, 끝수자+1,간격)
#range(끝수자+1)-> 0부터 끝수자, 간격=1

#1부터 100까지의 숫자를 저장하세요
nums=range(1, 101)
print(nums)
print(f'nums값: {nums}\n타입: {type(nums)}\n개수: {len(nums)}')
print(nums[54])

#원소 읽기->인덱싱
print(nums[32])

#원소 슬라이싱 ->range 형태로 나옴
print(nums[40:45])  #->range(41, 46)

print(list(nums[40:45])) #->형변환하여 도출
#print(tuple(nums[20:45]))

#실습1. 1~100에서 3의 배수만 저장하세요
three=range(3,101,3)
print(list(three))

#1.0~10.0사이의 숫자
#range(1.0,10.0,1)  #TypeError: 'float' object cannot be 
                #   interpreted as an integer
                #range->정수만 가능
datas=list(range(1,11))
#print(float(datas)) #TypeError: float() argument must be 
                    #a string or a number, not 'list'
                    #list는 플롯으로 변환 x
#map=> list 형변환                    
datas=(map(float, datas)) #->하나하나 플롯으로 변환
                          # class=map
print(type(datas),datas)
datas=list(map(float, datas)) #=리스트로 변환
