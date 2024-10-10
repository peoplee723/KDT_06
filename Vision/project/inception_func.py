import torchvision.transforms as transforms
from torchvision.transforms import v2
from PIL import Image

def img_processing(img_data):
    # 이미지 불러오기
    test_img=img_data

    # 이미지 전처리
    preprocess = v2.Compose([
        transforms.ToTensor(),
        v2.Resize(size=(342), interpolation=v2.InterpolationMode.BILINEAR),
        v2.CenterCrop(299),
        v2.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    test_img= Image.open(test_img)
    scaled_img=preprocess(test_img)
    scaled_img= scaled_img.unsqueeze(0)


def img_predicting(data):
    result=['Diva', 'Genji', 'Hanzo', 'Para', 'Roadhog', 'Tracer']

    pre_val=model(data)
    pre_val=F.softmax(pre_val, dim=1)
    a= pre_val.argmax().item()
    print(a)
    # print(pre_val[0][1].item())
    print(f'{result[a]}: {(pre_val[0][a].item()):.4f}')