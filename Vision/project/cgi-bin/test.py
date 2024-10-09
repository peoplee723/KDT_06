# 위에 라인 : 셀 내용을 파일로 생성/ 한번 생성후에는 마스킹

# 모듈 로딩--------------------------------------------
import os.path     # 파일 및 폴더 관련
import cgi, cgitb  # cgi 프로그래밍 관련
import joblib      # AI 모델 관련
import sys, codecs # 인코딩 관련
from pydoc import html # html 코드 관련 : html을 객체로 처리?
import torch
import torch.nn
import torch.nn.functional as F
from predict import *


# 동작관련 전역 변수----------------------------------
SCRIPT_MODE = True    # Jupyter Mode : False, WEB Mode : True
cgitb.enable()         # Web상에서 진행상태 메시지를 콘솔에서 확인할수 있도록 하는 기능


# 사용자 정의 함수-----------------------------------------------------------
# WEB에서 사용자에게 보여주고 입력받는 함수 ---------------------------------
# 함수명 : showHTML
# 재 료 : 사용자 입력 데이터, 판별 결과
# 결 과 : 사용자에게 보여질 HTML 코드
def showHTML(data, msg):
    print("Content-Type: text/html; charset=utf-8")
    print(f"""
    <!DOCTYPE html>
    <html lang="en">
     <head>
      <meta charset="UTF-8">
      <title>---건강 점수 측정---</title>
     </head>
     <body>
      <form>
        <input type='text' name='q0' placeholder='나이' value='{data[0]}'><br/>
        <input type='text' name='q1' placeholder='키' value='{data[1]}'><br/>
        <input type='text' name='q2' placeholder='몸무게' value='{data[2]}'><br/>
        <input type='text' name='q3' placeholder='평균 수면 시간' value='{data[3]}'><br/>
        <input type='text' name='q4' placeholder='흡연 여부(예=1, 아니요=0)' value='{data[4]}'><br/>
        <input type='text' name='q5' placeholder='한달 평균 음주 횟수' value='{data[5]}'><br/>
        <input type='text' name='q6' placeholder='하루 평균 과일 섭취 횟수' value='{data[6]}'><br/>
        <input type='text' name='q7' placeholder='하루 평균 채소 섭취 횟수' value='{data[7]}'><br/>
        <input type='text' name='q8' placeholder='한달 평균 운동 횟수' value='{data[8]}'><br/>
        <p><input type="submit" value="결과보기"></p>
        <p>{msg}</p>
      </form>
     </body>
    </html>""")

    
# 사용자 입력 텍스트 판별하는 함수---------------------------------------------------------------------------
# 함수명 : detectLang
# 재 료 : 사용자 입력 데이터
# 결 과 : 판별 언어명(영어, 프랑스~)


def detectLang(data_input, model):
    result=""
    if data_input == [""]*9: result="입력 대기" 
    elif len(data_input) !=9: 
      
        result ="다시 입력하세요."
    data_input = list(map(int, data_input))
    d=data_input
    bmi=d[2]/d[1]*d[1]
    sample=[d[0],d[2],bmi, d[3], 0, d[4], d[5], d[6], d[8]*10, d[5],d[6], 0,0,0,0,0,0,0,1,0,0,0,0,0,0]
    # 텐서화
    dataTS = torch.FloatTensor(sample).reshape(1,-1)
    # print(dataTS, dataTS.shape)

    # test data 예측-----------------------------------------
    # 모델 로드
    # pklfile = r'C:\Users\KDP-43\Desktop\DL_project\cgi-bin\model\alive_1\model_all.pth'

    # SepsisModel = joblib.load(pklfile)

    model.eval()
    with torch.no_grad():
        result ='' #predict_mcf(Model, dataTS,
                  #              result=['Poor', 'Fair', 'Good', 'Very_good', 'Excellent'])



    return result

# 기능 구현 ------------------------------------------------
# (1) WEB 인코딩 설정
if SCRIPT_MODE:
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach()) #웹에서만 필요 : 표준출력을 utf-8로

# # (2) 모델 로딩

# pklfile = r'C:\Users\KDP-43\Desktop\DL_project\cgi-bin\model\alive_1\model_all.pth'
    
# SepsisModel = joblib.load(pklfile)

## 저장경로
# SAVE_PATH= r'C:\Users\KDP-25\Desktop\KDT_06\Pytorch\models\health'

# 저장 파일명
# SAVE_MODEL = SAVE_PATH+'\model_train_all.pth'

# if os.path.exists(SAVE_MODEL):
#    Model= torch.load(SAVE_MODEL, weights_only=False)
#    print("경로상 파일이 존재합니다.")
# else:
#    print(f'{SAVE_MODEL} 파일이 존재하지 않습니다. 다시 확인하세요.')



# (3) WEB 사용자 입력 데이터 처리
# (3-1) HTML 코드에서 사용자 입력 받는 form 태크 영역 객체 가져오기
form = cgi.FieldStorage()
# (3-2) Form안에 textarea 태크 속 데이터 가져오기
data = []
data.append(form.getvalue("q0", default="20"))
data.append(form.getvalue("q1", default="180"))
data.append(form.getvalue("q2", default="60"))
data.append(form.getvalue("q3", default="8"))
data.append(form.getvalue("q4", default="0"))
data.append(form.getvalue("q5", default="2"))
data.append(form.getvalue("q6", default="3"))
data.append(form.getvalue("q7", default="3"))
data.append(form.getvalue("q8", default="60"))
#text ="Happy New Year" # 테스트용 (쥬피터 내부)

# (3-3) 판별하기
# msg =""
# if not '' in data:
result_input = detectLang(data, Model)
result_input = f'{result_input}'

# result_input = detectLang(data)

# data 초기화
data = [""]*9
# (4) 사용자에게 WEB 화면 제공
showHTML(data,result_input)

