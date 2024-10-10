# compile
# 동일 패턴을 여러번 검색하는 경우 편리성의 위해 객체 생성

import re

#compile() 사용 안할 때
m= re.match('[a-z]+', 'Python') # 첫글자가 대문자라 none반환
print(m)
print(re.search('apple', 'I like apple!'))

#compile 사용 시
p= re.compile('[a-z]+')
m=p.match('pythoN')
print(m)
print(p.search('I like aplle 123'))

#match()-> 문자열의 처음부터 검사
m= re.match('[a-z]+', 'pythoN')
print(m)
m= re.match('[a-z]+', 'PYthoN')
print(m)

print(re.match('[a-z]+', 'regex python'))
print(re.match('[a-z]+', ' regexpython')) #첫 문자열이 공백이라 none
print(re.match('[a-z]+', 'regexpythoN'))
print(re.match('[a-z]+$', 'regexpythoN'))#문자열의 끝이 대문자라 none
print(re.match('[a-z]+', 'regexPython'))
print(re.match('[a-z]+$', 'regexpython'))

#findall() -> 일치하는 모든 문자열 리스트로 반환
p= re.compile('[a-z]+')
print(p.findall('life is too short! Regular expression test'))

# search() -> 일치하는 첫번째 문자열만 반환
result= p.search('I like aplle 123')
print(result)
result= p.findall('I like apple 123')
print(result)

#전화번호 분석

tel_checker= re.compile(r'^(\d{2,3})-(\d{3,4})-(\d{4})$')

print(tel_checker.match('02-123-4567'))
match_groups= tel_checker.match('02-123-4567').groups()
print(match_groups)

match_group= tel_checker.match('02-123-4567').group()
print(match_group)

print(tel_checker.match('053-950-45678'))
print(tel_checker.match('053950-4567'))


#dash(-) 제거하고 검사하기
tel_number= '053-950-4567'
tel_number= tel_number.replace('-', '')
print(tel_number)

tel_checker1= re.compile(r'^(\d{2,3})(\d{3,4})(\d{4})$')
print(tel_checker1.match(tel_number))
print(tel_checker1.match('0239501234'))

m= tel_checker.match('02-123-4567')

print(m.groups()) # 매칭 결과를 튜플로 출력
print('group(): ', m.group())
print('group(0): ', m.group(0)) #0-> 모두 출력
print('group(1): ', m.group(1))
print('group(2,3): ', m.group(2,3))
print('start(): ', m.start())  #매칭된 문자열의 시작 인덱스
print('end(): ', m.end())       #매칭된 문자열의 끝 인덱스+1

#휴대전화번호
cell_phone= re.compile('^(01(?:0|1|[6-9]))-(\d{3,4})-(\d{4})$')

print(cell_phone.match('010-123-4567'))
print(cell_phone.match('019-1234-5678'))
print(cell_phone.match('001-123-4567')) #규칙에 맞지 않는 형태->none
print(cell_phone.match('010-1234567')) #-없음

#전방 긍정 탐색->일치시 패턴 앞의 문자열 반환(?=패턴)

lookahead1= re.search('.+(?=won)', '1000 won')
if lookahead1!=None:
    print(lookahead1.group())
else:
    print('None')
lookahead2= re.search('.+(?=am)', '2023-01-26 am 10:00:01')
print(lookahead2.group())

#전방 부정 탐색 -> 불일치시 패턴 앞의 문자열 반환(?!패턴)
lookahead3= re.search('\d{4}(?!-)', '010-1234-5678')
print(lookahead3)

#후방 긍정 탐색-> 일치시 패턴 뒤 문자열 반환(?<=패턴)
lookbehind1= re.search('(?<=am).+', '2023-01-26 am 11:10:01')
print(lookbehind1)

lookbehind2= re.search('(?<=:)', 'USD: $51')
print(lookbehind2)

#후방 부정 탐색 -> 불일치시 패턴 뒤 문자열 반환(?<!패턴)
lookbehind4= re.search(r'\b(?<!\$)\d+\b', 'I paid $30 for 100 apples.')
print(lookbehind4)
