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

    # http://127.0.0.1:5000/info
    def info():
        return '''
        <body style='background-color: skyblue; text-align: center'>
        <h1>INFORMATION</h1>
        </body>'''



    
    # 초기 화면
    @APP.route('/main')
    def mainpage():
        return render_template('index.html')


    # f'''
    #     <body style='background-color: skyblue; text-align: center'>
    #         <h1>{age}'s INFORMATION</h1>
    #         hello ~~ I'm {age} years old!
    #     </body>
    #     '''

    # http://127.0.0.1:5000/info/숫자변수(age)
    @APP.route('/go')
    def gohome():
        return APP.redirect('./info')


    # html과 연결
    @APP.route('/')
    def index():
        return render_template('index.html')
    return APP


# 조건부 실행
if __name__ == '__main__':
    app=create_app()
    app.run()