#튜플 데이터 자료형 살펴보기
#내장함수: len,max,min,sum
# 연산자: 덧셈, 곱셈, 멤버
# .

nums=11,22,33,44,55
print(f'nums의 개수: {len(nums)}')
print(f'nums의 최대값: {max(nums)}')
print(f'nums의 합계: {sum(nums)}')
print(f'nums의 정렬: {sorted(nums)}, {sorted(nums, reverse=True)}')

print(max('abc','Abc'))
print(sorted(['abc','Zoo']))

#연산자

#덧셈
data=11,22
data2='A','B','C'
data3=[1,2]
print(data+data2)   #->한개의 튜플로 만듦
#TypeError: can only concatenate(연결시키다) tuple 
# (not "list") to tuple
#print(data+data3)  #list+tuple->안됨


#곱셈 (tuple*int)->반복
print(data*3)

#멤버연산다 =>in, not in
print(11 in data)
print('a' in data)
print('a' not in data)
