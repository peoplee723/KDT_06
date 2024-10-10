# 클래스 (class)
# 객체지향 언어에서 데이터를 정의하는 자료형
# 데이터를 정의할 수 있는 데이터가 가진 속성과 기능을 명시

# 구성요소: 속성/attribute/feild + 기능/메서드

# 클래스 정의: 햄버거를 나타내는 클래스
# 클래스 이름: 버거
# 클래스 속성: 번, 패티, 야채, 치즈
# 클래스 기능: 햄버거 설명기능
class Burger:
    #힙 영역에 객체 생성시 속성값을 저장하는 기능
    def __init__(self, bread, patty, veg, kind):
        self.bread= bread
        self.patty= patty
        self.veg= veg
        self.kind= kind
    #클래스의 기능, 즉 메서드 (괄호안 self는 필수!)
    def printInfo(self):
        print(f'빵: {self.bread}, 패티: {self.patty}, 야채: {self.veg}, 브랜드: {self.kind}')


    def get_bread(self):
        return self.bread
    def set_bread(self, bread):
        self.bread= bread
# 객체생성
# Burger1= Burger()
# ->__init__() missing 4 required positional arguments: 
# 'bread', 'patty', 'veg', and 'kind'

# 불고기 버거
Burger1=Burger('브리오슈', '불고기', '양상추 양파 토마토','롯데리아' )

# 치츠버거 객체생성
Burger2= Burger('참깨빵', '쇠고기패티', '치즈 양상추 양파 토마토', '맥도날드')

# 버거 정보확인

Burger1.printInfo()
Burger2.printInfo()

# 속성을 변경하거나 읽어오는 메서드=> getter/setter 메서드

print(Burger1.bread, Burger1.get_bread())

# 속성 읽기-> 직접접근, 간접접근(getter 메서드)

# 속성 변경 방법: 직접점근, 간점점근(setter 메서드)

Burger1.bread='들깨빵'
Burger1.set_bread('올리브빵')
Burger1.printInfo()
