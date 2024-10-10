# 모듈 내에서 일부 변수 또는 함수,클래스만 포함하는 경우
# 형식 from 모듈명 import 변수/함수/클래스명
# 파일안에 동일한 변수/함수/클래스가 존재하면 나중에 지정한 것 실행!
from math import pi, factorial, e 

from random import *   #(*= 모든 것)

# 전역변수
pi='apple'
# =>이름이 똑같으면 사용자가 지정한 이름 우선

print(f'내장모듈 math 안에서 pi사용{pi}')
# print(math.factorial) ->not defined
print(random(), randint(1,10))