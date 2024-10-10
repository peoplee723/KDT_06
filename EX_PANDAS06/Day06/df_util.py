# Sries/DataFrame에서 사용되는 사용자 정의 함수들
#-----------------------------------------------------------------
#함수기능: DataFrame의 기봊ㄴ정보와 속성 확인 기능
#함수이름: checkDataFrame
# 매개변수:DataFrame 인스턴스 변수명, DataFrame 인스턴스 이름
# 리턴값: x(바로 출력)
#------------------------------------------------------------------
def checkDataFrame(object, name):
    print(f'\n[{name}]')
    object.info()
    print(f'인덱스: {object.index}')
    print(f'컬럼: {object.columns}')
