# 위에 라인 : 셀 내용을 파일로 생성/ 한번 생성후에는 마스킹
# 모듈 로딩--------------------------------------------
import os.path     # 파일 및 폴더 관련
import cgi, cgitb  # cgi 프로그래밍 관련
import joblib      # AI 모델 관련
import torch
import sys, codecs # 인코딩 관련
from pydoc import html # html 코드 관련 : html을 객체로 처리?
from get_train_model import *

# 동작관련 전역 변수----------------------------------
SCRIPT_MODE = True    # Jupyter Mode : False, WEB Mode : True
cgitb.enable()         # Web상에서 진행상태 메시지를 콘솔에서 확인할수 있도록 하는 기능

# 사용자 정의 함수-----------------------------------------------------------
# WEB에서 사용자에게 보여주고 입력받는 함수 ---------------------------------
# 함수명 : showHTML
# 재 료 : 사용자 입력 데이터, 판별 결과
# 결 과 : 사용자에게 보여질 HTML 코드

def showHTML(text, msg):
    print("Content-Type: text/html; charset=utf-8")
    print(f"""
    
        <!DOCTYPE html>
        <html lang="en">
         <head>
          <meta charset="UTF-8">
          <title>---건강 점수 예측---</title>
         </head>
         <body>
          <form>
          <label for="q1">질문 1: 나이</label><br>
            <textarea name="q1" rows="1" colos="10" >{text}</textarea><br><br>

            <label for="q2">질문 2: 키</label><br>
            <textarea name="q2" rows="1" colos="10" ></textarea><br><br>

            <label for="q3">질문 3: 몸무게</label><br>
            <input type="text" id="q3" name="q3" required><br><br>

            <label for="q4">질문 4: 평균 수면 시간</label><br>
            <input type="text" id="q4" name="q4" required><br><br>

            <label for="q5">질문 5: 흡연 여부(예=1,아니요=0)</label><br>
            <input type="text" id="q5" name="q5" required><br><br>
                
            <label for="q6">질문 6: 한달 평균 음주 횟수</label><br>
            <input type="text" id="q6" name="q6" required><br><br>


            <label for="q7">질문 7: 하루 평균 과일 섭취 횟수</label><br>
            <input type="text" id="q7" name="q7" required><br><br>

            <label for="q8">질문 8: 하루 평균 채소 섭취 횟수</label><br>
            <input type="text" id="q8" name="q8" required><br><br>  

            <label for="q9">질문 9: 한달 평균 운동 횟수</label><br>
            <input type="text" id="q9" name="q9" required><br><br>

            <p><input type="submit" value="결과보기">{msg}</p>
          </form>
         </body>
        </html>""")

    
# 사용자 입력 텍스트 판별하는 함수---------------------------------------------------------------------------
# 함수명 : detectLang
# 재 료 : 사용자 입력 데이터
# 결 과 : 판별 언어명(영어, 프랑스~)

def detectLang(q1,q2,q3,q4,q5,q6,q7,q8,q9):
    # 데이터 프레임에 삽입
    # bmi=q3/q2*q2
    # if q6>0: q6= 1
    # if q7>0: q7= 1
    # sample=[q1,q3,bmi, q4, 0, q5, q6, q6, q9*10, q6,q7, 0,0,0,0,0,0,0,1,0,0,0,0,0,0]
    # # 판별요청 & 결과 반환 ===> 개인이 만든 함수의 predict 넣기
    # result = predicting(healthModel, sample, type='muticlass',
    #                     result=['Poor', 'Fair', 'Good', 'Very_good', 'Excellent'])
    
    # return result
    pass



# 기능 구현 ------------------------------------------------
# (1) WEB 인코딩 설정
if SCRIPT_MODE:
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach()) #웹에서만 필요 : 표준출력을 utf-8로

# (2) 모델 로딩 ===> 가지고온 모델에 따라 불러오기 + 로딩 다름!
# if SCRIPT_MODE:
#     modelfile = os.path.dirname(__file__)+ '/health_wbs.pth' # 웹상에서는 절대경로만
# else:
#     modelfile = './health_wbs.pth'
# modelfile= 'model_all.pth'
# healthModel = torch.load(modelfile)

# (3) WEB 사용자 입력 데이터 처리
# (3-1) HTML 코드에서 사용자 입력 받는 form 태크 영역 객체 가져오기
form = cgi.FieldStorage()

# (3-2) Form안에 textarea 태크 속 데이터 가져오기
text = form.getvalue("text", default="")
# q1 = form.getvalue("q1", default="")
# q2 = form.getvalue("q2", default="")
# q3 = form.getvalue("q3", default="")
# q4 = form.getvalue("q4", default="")
# q5 = form.getvalue("q5", default="")
# q6 = form.getvalue("q6", default="")
# q7 = form.getvalue("q7", default="")
#text ="Happy New Year" # 테스트용 (쥬피터 내부)

# (3-3) 판별하기
msg =""
if text != "":
    resultLang = detectLang(text)
    msg = f"{resultLang}"

# (4) 사용자에게 WEB 화면 제공
showHTML(text,msg)