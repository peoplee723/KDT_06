# Flask 에서 '/URL'에 대한 라우팅 처리 파일
# 파일명: main_views.py

# 모듈 로딩
from flask import Blueprint, render_template

# blueprint 인스턴스 생성 (최소 입력값: 이름, import이름, url_prefix, 템플릿 폴더)
main_bp= Blueprint('main', import_name='__name__', 
                   url_prefix='/', template_folder='templates')

# 라우팅 기능 함수 정의 
# 엔드포인트 지정 가능
# -> 나중에 함수가 바꿔도 엔드포인트가 그대로이기 때문에 코드가 꼬이는 것을 방지 가능
@main_bp.route('/', endpoint='hello')
def index():
    return render_template('index.html')
