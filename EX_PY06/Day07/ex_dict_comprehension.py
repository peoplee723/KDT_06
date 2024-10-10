#list/set/dict 자료,반복, 조건부표현식

keys=['a','b','c','d']
       #dict.fromkeys 빈 딕트 생성, 벨류=none
x={key:value for key, value in dict.fromkeys(keys).items()}
print(x)
#키와 밸류를 keys를 통해 새 딕트를 만들어서 새 딕트의 키와 벨류를
#  x에 넣는다

#23 24 빼고 