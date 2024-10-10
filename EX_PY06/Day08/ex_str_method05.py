# 1개 문자열을 여러개 문자열로 분리해주는 메서드
# split() -> 분리기준:공백(기본값)

msg=' Happy New Year '
result= msg.split()
print(result, type(result)) #->리스트로 반환해줌

phone='010-2222-3333'
p_result= phone.split('-')
print(p_result, type(p_result)) 

phone='오늘은 날씨가 좋군요. 내일도 날씨가 좋을까요?'
result= phone.split('.')
print(result, type(result)) 

# 여러개 문자열을 하나의 문자열로 합쳐주는 메서드
# 함칠문자.join(여러개 문자열)
# 010*2222
con='*'
phone2=con.join(p_result)
print(phone2,type(phone2))

con='`'
phone2=con.join(p_result)
print(phone2,type(phone2))

# 문자열 구성하는 문자 검사 메서드 => 변수명.isOOO()
# -----------------------------------------------------------------------------
# 문자열 내에 숫자 존재여부 체크 메서드들 3종류
# - 변수명.isnumeric()  
# -> 0~9까지의 숫자, 5¹, 5₁, ①, ➊, ⅒, Ⅳ, ⅳ, 百
# - 변수명.isdigit()    
# -> 0~9까지의 숫자, 5¹, 5₁, ①, ➊ 
# - 변수명.isdecimal()  : 
#  - >0~9까지의 숫자
#    ==> 실수, 음수, 나머지 : False
# - isdecimal() < isdigit() < isnumeric()
# -----------------------------------------------------------------------------
