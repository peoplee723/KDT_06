# 문자열에서 좌우 여백 제거 메서드
# -strip(), lstrip(), rstrip()
# 문자열 내부에 공백은 제거x

msg="Good Luck"
data='  Happy New Year 2025! '

# 좌우 공백 모두 제거
m1= msg.strip()
print(f'원본 msg: {len(msg)}, 제거m1: {len(m1)}')

d1=data.strip()
print(f'원본 msg: {len(data)}, 제거d1: {len(d1)}')

# 왼쪽만 제거
d1=data.lstrip()
print(f'원본 msg: {len(data)}, 제거d1: {len(d1)}')

#오른쪽만 제거
d1=data.rstrip()
print(f'원본 msg: {len(data)}, 제거d1: {len(d1)}')

#실습 -> 이름을 입력 받아서 저장하세요 -->() 잊지 말기!!
# name= input('이름: ').strip()
# if len(name)>0:
#     print(f'이름: {name}')
# else:
#     print('이름은 입력하지 않았습니다.')

#입력받은 데이터에 따라 출력을 다르게 합니다
# 알파벳=★, 숫자면 ♥, 나머지 무시
# data=input('알파벳, 숫자 또는 문자 1개 입력: ').strip()

# if 'a'<=data<='z' or 'A'<=data<='Z':
#     print('★')
# elif '0'<=data<='9':
#     print('♥')
