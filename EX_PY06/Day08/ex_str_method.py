# str데이터 타입 전용 함수 즉, 메서드 살펴보기

# 문자열을 구성하는 문자를 검사해주는 메서드
#  isxxxx()  ->결과 논리형(True/False)

# 알파벳으로 구성된 문자열인지 검사 isalpha()
data='Good'
print(f'd{data} =>{data.isalpha()}')

# 알파벳으로 구성된 문자열인지+대문자인지 검사 isupper()
data='Good'
print(f'{data} =>{data.isupper()}')
print(f'GOOD => {"GOOD".isupper()}')

# 알파벳으로 구성된 문자열인지+소문자인지 검사 islower()
data='Good'
print(f'{data} =>{data.islower()}')
print(f'GOOD => {"GOOD".islower()}')
print(f'good => {"good".islower()}')

# 숫자로 구성된 문자열인지 검사: isdecimal()
print(f'1234 => {"1234".isdecimal()}')
print(f'Happy1234 => {"Happy1234".isdecimal()}')

#숫자와 문자가 혼합된 문자열 검사: isalnum()
print(f'1234 => {"1234".isalnum()}')
print(f'Happy1234 => {"Happy1234".isalnum()}')
print(f'Happy => {"Happy".isalnum()}')

# 공백 문자 여부 검사: isspace()
print(f'1234   => {"1234  ".isspace()}')
print(f'   => {"  ".isspace()}')
