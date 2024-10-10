# 기능 -> 원하는 단의 구구단 출력
# 이름 ->dan
# 매개 변수-> num1
# 결과 ->매개 변수에 해당하는 단 출력(none)

def dan(num1):
    print(f'{num1}단')
    for i in range(1,10):
            print(f'{num1} * {i} = {(i//10)*(i%10)}')

dan(9)



# 기능-> 파일의 확장자 반환
# 이름-> file_ext
# 매개 변수: a(파일이름.확장자)
# 함수결과 : 파일이름 : 확장자
# file.txt
def file_ext(filename):
    x=filename.rfind('.')    #파일이름에 . 있는 상황까지 고려하면 rfind
    print(f'{filename[:x]} : {filename[x+1:]}')
    

file_ext('filsadfasdf.jpg')
