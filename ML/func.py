import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.ensemble import VotingClassifier, BaggingClassifier, GradientBoostingClassifier, RandomForestClassifier
from sklearn.linear_model import ElasticNet, Ridge, Lasso, LinearRegression
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler, OneHotEncoder, OrdinalEncoder, LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, r2_score, f1_score, confusion_matrix, precision_recall_curve

from typing import Dict, Optional, Any
from numbers import Integral
import numbers


# 함수를 만들자!
# 전처리된 데이터를 기준으로, 피쳐 스케일링-> 교차검증, 학습, 검증, 테스트를 통해 최적의 모델 선정하기
                            # => 스케일링 방법 + 하이퍼파라미터, 값에 따라 모델 생성해야함!

# 선형 회귀 모델-> 최적의 모델 만들기
# 선정 과정: 스케일링-> 교차검증 -> 학습-> 테스트 =>최적 모델 선정
# 변수 설정: 스케일링 모델, 교차검증cv값(스코어링값), 학습모델, 각 하이퍼파라미터값, 결과 스코어 도출
# gridsearchCV-> 알파값 알아서 반복해줌+ 최고 모델, 스코어 도출 가능함
# ++ CV값 바꾸기


# 클래스로 만들자
class make_model():
    # 인스턴스 생성시 DF파일 받음
    def __init__(self, Data) -> None:
        self.sc_model=None
        self.model=None
        self.cv_model=None #?
        self.data=Data
        self.X_train=None
        self.X_test=None
        self.Y_train=None
        self.Y_test=None
        self.X_train_scaled=None
        self.X_test_scaled=None
        self.best_model=None
        self.pred=None
    
    def encoding(self, encoder_name):
        # if encode_name== 'OneHotEncoder': encode_model=OneHotEncoder()
        # if encode_name== 'OrdinalEncoder': encode_model= OrdinalEncoder()
        # if encode_name== 'LabelEncoder': encode_model= LabelEncoder()
        encode_model=encoder_name
        encode_model.fit(self.X_train)

    # 피쳐, 타겟 분리  ->test, train 안적어도 되도록
    def split(self,featureN, target, testsize, stratify=None, random_state=None|int):
            '''
            피쳐와 타겟 분리하는 함수(인스턴스에 저장)\n
            params: featur, target, testsize, stratify\n
            return: 각 분리된 데이터의 shape, ndim\n
            '''
            X_train, X_test, Y_train, Y_test= train_test_split(featureN, target, 
                                                               test_size=testsize, stratify=stratify,
                                                               random_state=random_state)
            self.X_train=X_train; self.X_test=X_test; self.Y_train=Y_train; self.Y_test=Y_test
            print(f'X_train: {X_train.shape},{X_train.ndim}\n\
X_test: {X_test.shape},{X_test.ndim}\n\
Y_train: {Y_train.shape},{Y_train.ndim}\n\
Y_test: {Y_test.shape},{Y_test.ndim}')
    # 스케일링
    def get_scaled(self, scaler_name, get_data=True):
        '''
        분리된 데이터를 바탕으로 스케일링 하는 함수(인스턴스에 저장 또는 반환)\n
        params: scaler_name, get_data\n
        return: 스케일링된 데이터의 shape, nidim 또는 스케일링된 데이터\n
        '''
         
        # if scaler_name=='MinMaxScaler': self.sc_model=MinMaxScaler()
        # elif scaler_name=='RobustScaler': self.sc_model=RobustScaler()
        # elif scaler_name=='StandardScaler': self.sc_model=StandardScaler()
        self.sc_model=scaler_name
        # shape 변환-> numpy일 경우 reshape, Series일 경우 DataFrame으로

        
        self.sc_model.fit(self.X_train)
        if ~get_data:
            X_train_scaled= self.sc_model.transform(self.X_train)
            X_test_scaled= self.sc_model.transform(self.X_test)
            return X_train_scaled, X_test_scaled
        else:
            self.X_train_scaled= self.sc_model.transform(self.X_train)
            self.X_test_scaled= self.sc_model.transform(self.X_test)
            print(f'X_train_scaled: {self.X_train_scaled.shape},{self.X_test_scaled.ndim}\n\
X_test_scaled: {self.X_test_scaled.shape},{self.X_test_scaled.ndim}')
    
    # 교차검증 + 튜닝 with girdsearchCV
    def get_best_grid_model(self, model_name, Hparams: dict, cv, scoring=None):
    
        '''
        GridSearch를 바탕으로 최적의 모델 뽑는 함수\n
        Hparams는 dict형태로!\n
        params: model_name, params, cv, scoring\n
        return: cv_results
        '''

        # if model_name== 'DecisionTreeClassifier': self.mode= DecisionTreeClassifier()
        # if model_name== 'LinearRegression': self.model=LinearRegression()
        # if model_name== 'Ridge': self.model=Ridge()
        # if model_name== 'Lasso': self.model=Lasso()
        # if model_name== 'ElasticNet': self.model=ElasticNet()
        self.model= model_name
        cv_model= GridSearchCV(self.model, param_grid=Hparams, cv=cv, return_train_score=True, refit=True, scoring=scoring)
        cv_model.fit(self.X_train_scaled, self.Y_train)
        self.best_model= cv_model.best_estimator_
        return cv_model
    
    #교차검증 + 튜닝 with Randomize_searchCV
    def get_best_rand_model(self, model_name, Hparams: dict, cv, scoring=None):
        '''
        Randomize를 바탕으로 최적의 모델 뽑는 함수\n
        params는 dict형태로!\n
        params: model_name, params, cv, scoring\n
        return: cv_results
        '''

        self.model= model_name
        cv_model= GridSearchCV(self.model, param_grid=Hparams, cv=cv, return_train_score=True, refit=True, scoring=scoring)
        cv_model.fit(self.X_train_scaled, self.Y_train)
        self.best_model= cv_model.best_estimator_
        return cv_model

def get_best_threshold(model, X_test, Y_test):
    pred_proba = model.predict_proba(X_test)[:, 1] 
    precisions, recalls, thresholds = precision_recall_curve(Y_test, pred_proba)

    precisions, recalls, thresholds = precision_recall_curve(y_test, pred_proba_class1 )
    print('반환된 분류 결정 임곗값 배열의 Shape:', thresholds.shape)
    print('반환된 precisions 배열의 Shape:', precisions.shape)
    print('반환된 recalls 배열의 Shape:', recalls.shape)

    print("thresholds 5 sample:", thresholds[:5])
    print("precisions 5 sample:", precisions[:5])
    print("recalls 5 sample:", recalls[:5])

    #반환된 임계값 배열 로우가 147건이므로 샘플로 10건만 추출하되, 임곗값을 15 Step으로 추출. 
    thr_index = np.arange(0, thresholds.shape[0], 15)
    print('샘플 추출을 위한 임계값 배열의 index 10개:', thr_index)
    print('샘플용 10개의 임곗값: ', np.round(thresholds[thr_index], 2))

    # 15 step 단위로 추출된 임계값에 따른 정밀도와 재현율 값 
    print('샘플 임계값별 정밀도: ', np.round(precisions[thr_index], 3))
    print('샘플 임계값별 재현율: ', np.round(recalls[thr_index], 3))



def get_test_score(Y_train, pred):
        '''
        성능 평가지표를 도출하는 함수
        '''
        (tn, fp, fn, tp)= confusion_matrix(Y_train, pred).reshape(-1)
        Accuracy= (tp+tn)/(tp+fp+fn+tp)
        Precision= tp/(tp+fp)
        Recall= tp/(tp+fn)
        F1_score= 2*(Recall*Precision)/(Recall+Precision)
        con_matrix= confusion_matrix(Y_train, pred, labels=[0,1])
        print(f'matrix= {con_matrix}\n\
Accuracy= {Accuracy}\n\
Precision: {Precision}\n\
Recall: {Recall}\n\
F1_score: {F1_score}')



# 반복문 돌릴수 있도록 best모델에 리스트 또는 딕트 형태로 append? 
# cv_rsults_에 estimator 불러올 수 있나?
# 탐색적 분석 단계에 groupby 후 데이터시각화

def data_check(data):
    '''
    데이터 고유값을 확인하는 함수
    '''
    item=[]
    for feature in data.columns:
        i=data[feature].unique()
        print(feature, i)
        item.extend(i)

    print(item)