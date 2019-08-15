### pointwise : 손실함수를 한 document에서 찾는것


### pairwise : 손실함수를 한쌍의 document에서 찾는것  
- regression model을 만든다.  
- 어떤 결과에 대해서 정확하게 classification을 하는 것이 중요한게 아니다.  
- 입력 x1, x2가 rank(x1) > rank(x2)를 만족하면 f(x1) > f(x2)가 성립하는 실수 함수 f:X -> R를 찾는 것이다. (rank가 클수록 좋다고 가정했을 때)  
- 입력값이 확실하게 차이나도록 할 수 있게 +a를 정의해주면 더 좋을 것이다.  
- 즉, 좋은 입력 점수가 안 좋은 입력의 점수보다 a이상 높게 f를 가르치는 것  
- f(x1) > f(x2) + a 가 만족되지 않는 경우만 제재  
- max(0, f(x2) + a - f(x1)) 을 최소화 시킨다. 앞의 부등식이 만족되지 않으면 0, 그렇지 않으면 f(x2)+a가 얼마나 더 컸는지만큼 loss가 추가될것이다.  

### pairwise ranking loss를 사용하는 논문 : https://arxiv.org/abs/1704.03135  
- 이미지와 관련된 여러 레이블을 뽑는게 목표  
레이블 선정단계  
1. 가능한 모든 클래스에 confidence score를 계산해 순위표를 만듦  
2. 클래스마다 있는 threshold를 넘으면 해당 클래스에 속한다 판정  

label decision 모듈 g  
g의 버전  
1. label count estimation : g를 n-way classification을 푸는 함수로 사용 (n이 한 이미지에 허락되는 최대 label 개수)  
2. threshold estimation : 각 클래스마다 고유의 threshold real value값을 regression으로 정한다.

### listwise : 전체 document목록들을 최적의 방법으로 찾는 것  
list wise approaches는 pointwise or pairwise에 비해 복잡해질 수 있음  



예측 LSTM모델 만들기  
univariate : 일도량, 분포가 변량이 하나  
multivariate : 다변량  
multi-step : 다단계  

#### 코드

https://machinelearningmastery.com/how-to-develop-lstm-models-for-time-series-forecasting/  
univariate lstm model  
- 하나의 과거 관측으로부터 학습해 시퀀스의 다음 값을 예측하는 모델  

