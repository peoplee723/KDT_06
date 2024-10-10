#while 반복문

num=10
while num>10:
    print(num)
    num=num-1

#리스트에 원소 읽기
##while 반복문 : 개수  알아야 함
nums=[11,22,33]
cnt=0
while cnt<len(nums):          #리스트안 원소 개수만큼 반복
    print(cnt,nums[cnt])          #리스트 안 원소 출력
    cnt=cnt+1                 #반복제한 위한 변수

#실습-> Hello 문자열의 원소를 하나씩 출력하기
msg='Hello'
print(len(msg))
idx=0
while idx<len(msg):
    print(idx, msg[idx])
    idx=idx+1