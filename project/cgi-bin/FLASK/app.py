from flask import Flask, request, jsonify, render_template 
import torch
from torchvision import models, transforms
from PIL import Image
import io
from flask_cors import CORS
from torchvision.transforms import v2
from torchvision import transforms
import torch.nn.functional as F

app = Flask(__name__)
CORS(app)
'''
# 클래스 수 정의 (여기에 오버워치 데이터셋의 클래스 수를 입력)
num_classes = 6  # 클래스 수를 6으로 변경 (이전에 저장된 모델의 클래스 수와 일치)

# 오버워치 모델 불러오기
model = models.resnet50(weights=None)  # 사전 학습된 가중치는 사용하지 않음
num_ftrs = model.fc.in_features
model.fc = torch.nn.Linear(num_ftrs, num_classes)  # 클래스 수에 맞게 마지막 레이어 수정
'''
model=torch.load('model_final.pth', weights_only=False, map_location=torch.device('cpu'))
# 모델 가중치 로드
model.eval()

# 예측할 캐릭터 이름 리스트 (인덱스와 매핑)
character_names = [
    "D.Va",  # 인덱스 0에 해당하는 캐릭터 이름
    "Genji",  # 인덱스 1에 해당하는 캐릭터 이름
    "Hanzo",  # 인덱스 2에 해당하는 캐릭터 이름
    "Pharah",  # 오타 수정 "Pharah"
    "Roadhog",  # 인덱스 4에 해당하는 캐릭터 이름
    "Tracer"   # 인덱스 5에 해당하는 캐릭터 이름
]

def transform_image(img_data):
    # 이미지 불러오기
    test_img=img_data

    # 이미지 전처리
    preprocess = v2.Compose([
        transforms.ToTensor(),
        v2.Resize(size=(342), interpolation=v2.InterpolationMode.BILINEAR),
        v2.CenterCrop(299),
        v2.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    test_img= Image.open(io.BytesIO(test_img)).convert("RGB")
    scaled_img=preprocess(test_img)
    scaled_img= scaled_img.unsqueeze(0)
    return scaled_img

def img_predicting(data):
    data=transform_image(data)
    # result=['Diva', 'Genji', 'Hanzo', 'Para', 'Roadhog', 'Tracer']
    pre_val=model(data)
    pre_val=F.softmax(pre_val, dim=1)
    a= pre_val.argmax().item()
    return (f'{character_names[a]}: {(pre_val[0][a].item()):.4f}')

# 기본 페이지
@app.route('/')
def home():
    return render_template('index.html')  # index.html 파일을 렌더링

# API 엔드포인트
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']
    img_bytes = file.read()
    predicted_character = img_predicting(img_bytes)
    return jsonify({'character_name': predicted_character})  # 캐릭터 이름을 반환

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
