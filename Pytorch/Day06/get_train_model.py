from get_model import Custom_model
from torchmetrics.classification import F1Score, MulticlassF1Score
import torch.nn as nn
import torch.nn.functional as F
from torchmetrics.regression import R2Score, MeanSquaredError
import torch
import matplotlib.pyplot as plt
from typing import Literal

def model_training(model, trainDL, testDL, optimizer, EPOCH, type: Literal['reg', 'binary', 'muticlass'], numcls=None):
    '''
    type= 'reg'|'binary'|'mclf'
    return: LOSS_HISTORY, SCORE_HISTORY
    '''
    # 손실, 평가값 저장
    LOSS_HISTORY, SCORE_HISTORY= [[],[]], [[],[]]
    for epoch in range(EPOCH):
        print(f'{epoch+1}/{EPOCH}')
        model.train()
        loss_total, score_total= 0,0
        loss_val_total, score_val_total=0,0

        for train_feature, train_target in trainDL:
            # 학습
            pre_y=model(train_feature)

            # 손실
            if type=='reg':
                Lossfunc=MeanSquaredError()
                Scorefunc=R2Score()
            elif type=='binary':
                Lossfunc= nn.BCELoss()
                Scorefunc=F1Score(task='binary')
            elif type=='mutilcass':
                Lossfunc=nn.CrossEntropyLoss()
                Scorefunc=F1Score(task='multiclass', num_classes=numcls)

            loss= Lossfunc(pre_y, train_target)
            loss_total+=loss.item()

            # 평가
            score= Scorefunc(pre_y, train_target.reshape(-1,1))
            score_total+=score.item()
            # 최적화
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        # 검증

        model.eval()
        with torch.no_grad():
            for feature, target in testDL:
                # 학습
                pre_val= model(feature)

                # 손실
                loss= Lossfunc(pre_val, target)
                loss_val_total+=loss.item()

                # 평가
                score= Scorefunc(pre_val, target.reshape(-1,1))
                score_val_total+=score.item()

        
        # 저장
        LOSS_HISTORY[0].append(loss_total/len(trainDL))
        SCORE_HISTORY[0].append(score_total/len(trainDL))
        print(f'Train\n Loss: {loss_total/len(trainDL)}\n Score: {score_total/len(trainDL)}')

        LOSS_HISTORY[1].append(loss_val_total/len(testDL))
        SCORE_HISTORY[1].append(score_val_total/len(testDL))
        print(f'Val\n Loss: {loss_val_total/len(testDL)}\n Score: {score_val_total/len(testDL)}')


        return LOSS_HISTORY, SCORE_HISTORY
    

def draw_result(EPOCH, LOSS_HISTORY, SCORE_HISTORY):
    '''
    결과 시각화
    '''

    fig, (ax1, ax2)= plt.subplots(1,2, figsize=(15,6))
    ax1.plot(range(1,EPOCH+1), LOSS_HISTORY[0][:EPOCH], label='Train')
    ax1.plot(range(1,EPOCH+1), LOSS_HISTORY[1][:EPOCH], label='Val')
    ax1.set_title('Train & Val Loss')
    ax2.plot(range(1, EPOCH+1), SCORE_HISTORY[0][:EPOCH], label='Train')
    ax2.plot(range(1, EPOCH+1), SCORE_HISTORY[1][:EPOCH], label='Val')
    ax2.set_title('Train & Val Score')
    plt.legend()
    plt.show()