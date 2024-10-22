# Flask Framework에서 WebServer 구동 파일
# 파일명: app.py

# 모듈 로딩
from flask import Flask, render_template




# 전역변수
# FLASK WEB SERVER 인스턴스 생성
def create_app():
    APP=Flask(__name__)

    # 라우팅 기능 모듈
    from .views import main_view

    # views에서 처리한 라우팅 불러 오기
    APP.register_blueprint(main_view.main_bp)
    return APP
# 조건부 실행
if __name__ == '__main__':
    app=create_app()
    app.run()