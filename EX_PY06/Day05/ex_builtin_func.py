#내장함수

##정수 관련 내장함수
# 2, 8, 10, 16진수(프로그램)
# 숫자표현 0~9 0 1 2 3 4 5 6...9 10 11 12....100 1000 10000 100000 1000000...
# 10진수 -> 0~9
# 8진수 -> 0~7
# 2진수 -> 0,1
# 16진수 -> 0~9 A~F
# 정수를 2진수로 변환해주는 내장함수bin(정수)  (binary)
                        # 0b2진수 (0b가 이진수인걸 나타냄)=>
#                       class=str

print(4, bin(4), type(bin(4))) #-> 4 0b|100 <class 'str'>

#정수를 8진수로 변환해주는 내장함수 oct(정수)
print(4, oct(4), type(oct(4))) #-> 4 0o|4 <class 'str'>
                              # 0은 빗금이 있고 Oo는 없음

#정수를 16진수로 변환해주는 내장함수 hex(정수)
print(4, hex(40000), type(hex(40000)))#->4 0x|9c40 <class 'str'>

#16진수를 10진수로 변환해주는 내장함수int()
print(int('0b10', base=2))

age=18          ;print(age)
age=0x12        ;print(age)
age=0b10010     ;print(age)

#enumerate(): 
# 전달된 반복가능한 객체에서 원소당 번호를 부여해서 튜플로 묶어줌
# 원소의 인덱스 정보가 필여한 경우 사용
nums=[11,33,55]
print("enumerate() 변환:", list(enumerate(nums)))
