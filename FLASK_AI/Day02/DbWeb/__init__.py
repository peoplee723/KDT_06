# Flask Framework에서 WebServer 구동 파일
# 파일명: app.py

# 모듈 로딩
from flask import Flask




# application 생성 함수
# - 함수명: create_app (이름 변경 불가!!)
def create_app():
    APP=Flask(__name__)

    # #URL 즉, 클라이언트 요청 페이지 주소를 보여줄 기능 함수
    # # (함수만으로 URL처리 안됨 -> 따로 만듦)
    # def printPage():
    #     return '<h1>Hello~</h1>'


    # # URL 처리 함수 연결
    # APP.add_url_rule('/', view_func=printPage, endpoint='INDEX')

    # 위 연결을 간단히 만든 게 APP.route()
    # endpoint 부여 역시 가능
    # @APP.route('/', endpoint='INDEX')
    # def printPage():
    #     return '<h1>Hello~</h1>'    

    # blueprint 사용시 URL 처리 무듈 등록만 하면 됨 (처리 영역을 분리시킴)
    # URL 처리 모듈 등록
    from .views import main_views
    APP.register_blueprint(main_views.main_bp)

    return APP
    
# 조건부 실행
if __name__ == '__main__':
    app=create_app()
    app.run()