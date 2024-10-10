# 람다표현식 또는 람다함수
# 1줄함수, 익명함수
# 형식: lambda 매개변수 : 실행코드

names={1:'Kim', 2:'Adam', 3:'Zoo'}

# 정렬-> 내장함수 sorted()
result= sorted(names)  #기본= 키로 정렬
print("오름차순 정렬 [Key] ", result)

# value로 정렬
result= sorted(names.items(), key=lambda items: items[1])
# 람다의 items(변수)에 names.item((1, Kim), ...) 에  
print("오름차순 정렬 [Value] ", result)

print(sorted("This is a test string from Andrew".split(), key=str.lower))

print(sorted("This is a test string from Andrew".split()))

# map와 lambda
data=[11,22,33,44]

# 각 원소의 값에 곱하기 2해서 다시 리스트에 저장
def multi2(value): return value*2
data2=list(map(lambda a:a*2, data))
print(data2)

