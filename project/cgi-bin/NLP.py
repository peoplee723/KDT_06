# 위에 라인 : 셀 내용을 파일로 생성/ 한번 생성후에는 마스킹
# 모듈 로딩--------------------------------------------
import os.path     # 파일 및 폴더 관련
import cgi, cgitb  # cgi 프로그래밍 관련
import joblib      # AI 모델 관련
import torch
import sys, codecs # 인코딩 관련
from pydoc import html # html 코드 관련 : html을 객체로 처리?
import re
from NLPpredict import *
from collections import Counter
from konlpy.tag import Okt
import pickle
from NLPfunc import *
import torch.nn as nn
import torch
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
          <title>---뉴스 카테고리 예측---</title>
         </head>
         <body>
          <form>
            <textarea name="text" rows="30" cols="100" >{text}</textarea>
            <p><input type="submit" value="기사 감지">{msg}</p>
          </form>
         </body>
        </html>""")

    
# 사용자 입력 텍스트 판별하는 함수---------------------------------------------------------------------------
# 함수명 : detectLang
# 재 료 : 사용자 입력 데이터
# 결 과 : 판별 언어명(영어, 프랑스~)

def detectLang(text, model):
    # 한글만 남기고 모두 제거
    a= re.sub('[^ㄱ-ㅎ가-힣]+',' ',text)
    tokenizer=Okt()
    # 토큰화
    token_text=tokenizer.morphs(a)

    #단어사전을 통한 벡터화
    # 단어사전 불러오기
    with open('vocab.pikle', 'rb') as f:
        vocab=pickle.load(f)
    # 벡터화
    vec_token= vectorize2(vocab=vocab, DF=token_text, tokenizer=tokenizer)

    #패딩
    pad_token=padding2(length=50, text=vec_token)

    vec_token=pad_token[0]
    token_torch=torch.FloatTensor(vec_token).long()
    
    # 판별
    result_idx=['음식/의료', '환경','교육']
    model.eval()
    with torch.no_grad():
        result= predict_mcf2(model=model, data= token_torch, result=result_idx)

    # 판별요청 & 결과 반환 ===> 개인이 만든 함수의 predict 넣기
    
    return result 


# 기능 구현 ------------------------------------------------
# (1) WEB 인코딩 설정
if SCRIPT_MODE:
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach()) #웹에서만 필요 : 표준출력을 utf-8로

# (2) 모델 로딩 ===> 가지고온 모델에 따라 불러오기 + 로딩 다름!
## 저장경로
SAVE_PATH= r'C:\Users\KDP-25\Desktop\test\Web\project\model\nlp'

# 저장 파일명
SAVE_MODEL = SAVE_PATH+r'\model.pth'

if os.path.exists(SAVE_MODEL):
   model= torch.load(SAVE_MODEL, weights_only=False)
   print("경로상 파일이 존재합니다.")
else:
   print(f'{SAVE_MODEL} 파일이 존재하지 않습니다. 다시 확인하세요.')
    

# (3) WEB 사용자 입력 데이터 처리
# (3-1) HTML 코드에서 사용자 입력 받는 form 태크 영역 객체 가져오기
form = cgi.FieldStorage()

# (3-2) Form안에 textarea 태크 속 데이터 가져오기
text = form.getvalue("text", default="")
#text ="Happy New Year" # 테스트용 (쥬피터 내부)

# (3-3) 판별하기
msg =""
if text != "":
    resultLang = detectLang(text, model)
    msg = f"{resultLang}"

# (4) 사용자에게 WEB 화면 제공
showHTML(text,msg)
