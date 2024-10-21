import torch
import torch.nn as nn
from typing import Literal
import torch.nn.functional as F

def predicting(model, data, type: Literal['reg', 'binary', 'muticlass'], result):
    dataTS=torch.FloatTensor(data).reshape(1,-1)
    '''
    만들어진 모델을 바탕으로 예측하는 함수
    result: 분류일 경우 라벨 이름 목록
    '''
    # 예측
    pre_val=model(dataTS)
    if type=='reg':
        print(pre_val.item())
    elif type=='binary':
        if pre_val>0.5:
            print(result[0], f'{pre_val:.4f}')
        else: print(result[1], f'pre_val:.4f')


    elif type=='multiclass':
        pre_val=F.softmax(pre_val, dim=1)
        a= pre_val.argmax().item()
        print(f'{result[0]}: {max(pre_val[0].detach()):.4f}')
        return f'{result[0]}: {max(pre_val[0].detach()):.4f}'
    
def predict_mcf(model, data, result):
    dataTS=torch.FloatTensor(data).reshape(1,-1)
    pre_val=model(dataTS)
    pre_val=F.softmax(pre_val, dim=1)
    num=pre_val.argmax(dim=1)
    print(f'{result[num]}: {max(pre_val[0].detach()):.4f}')
    return f'{result[num]}: {max(pre_val[0].detach()):.4f}'


class make_model(nn.Module):
    '''
    커스텀 모델을 만드는 함수
    model_type= 'reg'|'binary'|'mclf'
    은닉층 수= 리스트 수-1
    '''
    def __init__(self, in_in, out_out, hidden: list) -> None:
        super().__init__()


        self.in_layer= nn.Linear(in_in, hidden[0])
        self.h1_layer=nn.Linear(hidden[0], hidden[1])
        self.h2_layer=nn.Linear(hidden[1], hidden[2])
        self.h3_layer=nn.Linear(hidden[2], hidden[3])
        self.out_layer= nn.Linear(hidden[-1], out_out)
    
    def forward(self, input_data):
        
        y= self.in_layer(input_data)
        y= F.relu(y)

        
        y=self.h1_layer(y)
        y=F.relu(y)
        
        y=self.h2_layer(y)
        y=F.relu(y)

        y=self.h3_layer(y)
        y=F.relu(y)

        y=self.out_layer(y)
        
        
        return y
