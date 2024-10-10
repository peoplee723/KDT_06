#연산자
# 
# 
#
d1={1,3,5,7}
d2={2,4,6,8, 7}

#덧셈연산
#print(d1+d2)
#TypeError: unsupported operand type(s) for +: 'set' and 'set'
#지원 안함 --->method를 통해 연산(집합의 형태)

#합집합 ->중복은 제거됨  .union 또는 |(shift+\)
print(d1.union(d2), d1|d2)

# 공통원소(교집합)     .intersection 또는 &
print(d1.intersection(d2), d1&d2)

#차집합 (공통원소를 제외한 나머지)   .difference 또는 -
print(d1.difference(d2), d1-d2)

