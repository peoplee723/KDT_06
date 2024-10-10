##문자열에서 사용가능한 내장함수
# 문자 ==>코드/기계어 변환 내장함수 ord(문자 1개)
"""c: str | bytes | bytearray,
    /
) -> int
Return the Unicode code point for a one-character string"""

print(f'A의 코드값: {ord("A")}')
print(f'가의 코드값: {ord("가")}')
print(f'口의 코드값: {ord("口")}')
print(f'の의 코드값: {ord("の")}')

#코드/기계어 ->문자 변환 내장함수 chr(코드값 정수)
print(f'97의 문자: {chr(97)}')
print(f'123455의 문자: {chr(123455)}')
