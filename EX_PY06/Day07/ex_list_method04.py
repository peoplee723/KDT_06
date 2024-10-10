

datas=[11,22,33]
nums=datas

nums[0]='백'
print(datas,'\n',nums, sep='')

##리스트 복사해주는 메서드 
# copy()  --->얕은 복사 (깊은 복사는 모듈)
nums2=datas.copy()
nums[0]='A'
print(datas,'\n',nums, nums2, sep='')
