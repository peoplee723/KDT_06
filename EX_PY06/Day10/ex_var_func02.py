# 전역변수
persons=['Hong']
year=2024
gender ={'H':'남자'}
# 사용자 정의 함수
def add_person(name):
    global year              #->리스트 자체가 바뀌지 않았기 때문에 가능(내용물만 바꿈)
    year+=1
    persons.append(name)
    gender[name]='여'
def remove_person(name):
    persons.remove(name)
    gender.pop(name)
# 함수 호출
print(f'persons = {persons}')
add_person('Park')
print(f'persons = {persons}')
print(f'gender = {gender}')

remove_person('Park')
print(f'persons = {persons}')
print(f'gender = {gender}')


