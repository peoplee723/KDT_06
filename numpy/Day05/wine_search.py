import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats
from sklearn.model_selection import train_test_split
from statsmodels.formula.api import ols
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

file_name='winequality-red.csv'
df=pd.read_csv(file_name)

# df_filter= df['redisual']
print(df.describe())
# print(df.corr(method='pearson'))

file_name2='winequality-white.csv'
df2=pd.read_csv(file_name2)
print(df2.describe())
# print(df2.corr(method='pearson')
print(df.isna().count(), df2.isna().count())
columns= ['고정산도', '휘발성산도', '구연산', '잔여 설탕', '염화물', '유리 이산화황', 
          '총 이산화황', '밀도', '산도', '황산염', '알코올']
# 설탕, 알코올, 밀도 설탕이 알코올에, 알코올이 밀도에 영향

# t테스트
def t_test():
    for name in df.columns:
        a=scipy.stats.ttest_ind(df[name], df2[name], equal_var=False)
        print(name)
        print()
        print(a)
        print()
# t_test()

# StandardScaler 객체 생성
scaler = StandardScaler()

# 데이터 적합 및 변환
scaled_data = scaler.fit_transform(df)
scaled_data2= scaler.fit_transform(df2)

# 결과 출력
print("원본 데이터:\n", df)
print("스케일링된 데이터:\n", scaled_data)

print(scaled_data)
df_red= pd.DataFrame(scaled_data, columns=df.columns)
df_white= pd.DataFrame(scaled_data2, columns=df2.columns)
print(df_red)
print(df_white)

# 화이트 레드 구분자 생성 (red=0, white=1)
df_red['color']=0
df_white['color']=1
df_mix=pd.concat([df_white, df_red], axis=0)
df_mix= df_mix.reset_index(drop=True)
print(df_mix)

# df_x= ['fixed_acidity', 'volatile_acidity', 'citric_acid', 'residual_sugar',
#        'chlorides', 'free_sulfur_dioxide', 'total_sulfur_dioxide', 'density',
#        'pH', 'sulphates', 'alcohol', 'quality']
# df_y=['color']

# 독립 변수와 종속 변수 분리
X = df_mix.drop('color', axis=1)  # 'quality'를 제외한 모든 열이 독립 변수
y = df_mix['color']               # 'quality'가 종속 변수

# 3. 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)



# 5. 다중 회귀 모델 생성 및 학습
model = LinearRegression()
model.fit(X_train, y_train)

# 6. 예측
y_pred = model.predict(X_test)

# 7. 평가
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R^2 Score: {r2}")

# 회귀 계수 및 절편
coefficients = model.coef_
intercept = model.intercept_

print("회귀 계수:", coefficients)
print("절편:", intercept)


