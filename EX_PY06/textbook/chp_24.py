#23.1
a=[[10,20], [30,40], [50,60]]
print(a[0][0])
print(a[1][1])

#24.1    -->str 메서드 
# replace
a='Hello, world!'  
print(a.replace('world', 'python'))

# maketrans, translate
table= str.maketrans('aeiou', '12345')
print('apple'.translate(table))
##변환 테이블을 만들어서 문자 일부만 변환

#split 
a=('apple pear grape pineapple orange')
print(type(a))
a=a.split()
print(a)

# join  리스트를 str(하나의 문자열)로 변환
a='-'.join(a)
print(a)

a='   pyThon  '
print(a.upper())           #괄호 빼먹지 않기!
print(a.lower())         #삭제의 개념이라 괄호안에 문자 넣으면 삭제 가능
print(a.lstrip())
print(a.rstrip())
print(a.strip())

a=' "python" '
print(a.ljust(10))  
print(a.rjust(10))
print(a.center(10))    ##남는 공간 이용하여가운데 정렬

print(a.rjust(10).upper())
print('35'.zfill(4))  #->str메서드 남는 공간0으로 채움

a='apple pineapple'
print(a.find('pl')) #처음찾은 인덱스, 없으면 -1
print(a.find('xy'))
print(a.index('pl')) #find와 동일,but 없으면 ERROR
a= 'I am %s' %'james'
print(a)

