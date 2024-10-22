# Flask Framework에서 WebServer 구동 파일
# 파일명: app.py

# 모듈 로딩
from flask import Flask, render_template




# 전역변수
# FLASK WEB SERVER 인스턴스 생성
def create_app():
    APP=Flask(__name__)

    # 라우팅 기능 함수
    # @서버 인스턴스 변수명.route('url')
    @APP.route('/info')
    @APP.route('/info/')



    
    # 초기 화면
    @APP.route('/main')
    def mainpage():
        return render_template('index.html')
    
    # ML화면 이동
    @APP.route('/ml')
    def ml_page():
        return render_template('ML.html')
    
    # DL화면 이동
    @APP.route('/dl')
    def dl_page():
        return render_template('DL.html')
    
    # vision화면 이동
    @APP.route('/vision')
    def vision_page():
        return render_template('vision.html')
    
    # nlp화면 이동
    @APP.route('/nlp')
    def nlp_page():
        return render_template('nlp.html')


    # html과 연결
    @APP.route('/')
    def index():
        return render_template('index.html')
    return APP


# 조건부 실행
if __name__ == '__main__':
    app=create_app()
    app.run()