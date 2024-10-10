# 메시지를 입력받습니다.
# 알파벳 대문자인경우 소문자로, 소문자인 경우 대문자로,
# 나머지는 그대로 되도록 출력하기
print(ord('B'), ord('b'))    #->대문자가 32더 작음
msg="HeLLo"
print(msg)
for m in msg:
    if 'a'<=m<'z':
        print(chr(ord(m)-32),end='')
    elif 'A'<=m<='Z':
        print(chr(ord(m)+32), end='')
    else:
        print(m,end='')
