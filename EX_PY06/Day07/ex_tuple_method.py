# tuple 전용 함수 즉, 메서드
# 수정 불가 즉, 추가-삭제-변경 x
nums=(10,20,30)

idx=nums.index(20)
print(idx)
if 5 in nums:
   idx=nums.index(5)
   print(idx)
 
 #데이터 갯수 메서드
#  count(데이터)
print(10, nums.count(10))
print(5, nums.count(5))
