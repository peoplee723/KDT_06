# list와 메모리#### 
#list 생성
nums=[10, 20,]  #= nums=list()-> 생성자
nums2= list([10,20])

print(f'nums의 id=> {id(nums)}')
print(f'nums2의 id=> {id(nums2)}')

print(f'nums[1]의 id=> {id(nums[1])}')
print(f'nums[0]의 id=> {id(nums2[0])}')
print(f'nums2[1]의 id=> {id(nums[1])}')
print(f'nums2[0]의 id=> {id(nums2[0])}')
#두 리스트의 주소는 다르다
#->but, 데이터의 주소가 같다  
