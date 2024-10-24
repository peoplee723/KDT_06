# Flask 에서 '/URL'에 대한 라우팅 처리 파일
# 파일명: main_views.py

# 모듈 로딩
from flask import Blueprint, url_for, request
from DbWeb.models.models import Question, Answer
from datetime import datetime
from werkzeug.utils import redirect
from DbWeb import DB


# blueprint 인스턴스 생성 (최소 입력값: 이름 import이름, url_prefix)
answer_bp=Blueprint('answer', '__name__', url_prefix='/answer')

# 라우팅 기능 함수 정의
# 엔드포인트 지정시 루트이름? 이 엔드포인트로 지정됨
# -> 나중에 함수가 바꿔도 엔드포인트가 그대로이기 때문에 코드까 꼬이는 것을 방지 가능

@answer_bp.route('/create/<int:question_id>', methods=('POST',))
def create(question_id):
    question=Question.query.get(question_id)
    content= request.form['content']
    answer= Answer(content=content, create_date=datetime.now())
    question.answer_set.append(answer)
    DB.session.commit()
    return redirect(url_for('main.question_id', question_id=question.id))