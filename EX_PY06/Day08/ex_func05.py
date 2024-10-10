# 사용자 정의 함수
# ->매개변수의 전달되는 데이터가 지정되지 않는 경우
# 어떤 데이터 종류 = 값 ->키워드파라미터/키워드매개변수
# -형식: def함수명(**params)   => 키=값의 형태

# 목적: 회원가입 기능 함수
# 이름: register
# 매개변수: 가입하는 사람마다 입력하는 정보가 상이함 (**params)
# 결과: 가입메시지 str  

def register(**params):
    print(type(params))

register(name='홍길동', job='의적')
register(id='master', age= 10, gender='f')
register()      #dict클래스로 받음

# 목적: 회원가입 기능 함수
# 이름: register
# 매개변수: 필수 입력 사항 id, pw, email
            # 선택 입력 사항 **params
# 결과: 가입메시지 str  

def register2(id, pw, email, **params):
    print(type(params)) 

register2("Hong", "h12345", 'h@naver.com', gender= 'F')
register2("Hong", "h12345", 'h@naver.com' )
#필수 정보는 꼭 포함, 선택사항은 변수명=데이터 형태로 입력
