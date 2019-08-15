
<<<<<<< HEAD
교사 학습 : 데이터와 함께 답을 입력, 다른 데이터의 답을 예측
비교사 학습 : 데이터는 입력하지만 답은 입력하지 않음, 다른 데이터의 규칙성을 찾음
강화 학습 : 부분적으로 답을 입력, 데이터를 기반으로 최적의 답을 찾아냄 << 핵심적인것

SI : 글자인식
UI : 최종적으로 내야하는 답이 정해져 있지 않음
=======
두개의 방식  
supervised learning  
unsupervised learning  

알고리즘의 종류  
머신러닝  
딥러닝  
강화학습  

batch 사이즈를 어떻게 하느냐

online learning : 데이터가 많아지고 적어지고 왔다갔다 하는 데이터를 학습  
offline learning : 

classification 분류하는 방법들  
svms, knn, decision trees, neural network, random forests

classification = supervised  
clustering = unsupervised  

matrix를 컴퓨터가 좋아한다...  

Regression  
Linear regression, non linear regression(곡선, 포물선 등)

어떻게 분류할 수 있는지 알아내는 것 : clustering algorithm

Dimensionality  
principal component analysis(PCA) : 어떤 구성으로 되어있는지를 만들어놓고, 분석을 하자


feature enginerring and extraction


Model evalution  
tf, idf : training을 통해서 나온 모델을 평가해서 계속해서 정확도를 높이는 것  
ex)암 환자가 A병동에 있다. A1... A2... A3... 이 집단으로  
feature enginerring extraction을 함, 진단을해서 진짜 암이면 true positive  
암이 아닌데 positive가 나옴, false positive  
암을 가지고 있는데 암 판정이 안나옴, ture negative  
암이 없고 암 판정이 안나옴, false negative  
이것으로 미래를 예측

ROC :  그래프를 보고 어떤게 더 정확  
AUC : 군집단의 크기를 보고 예측, AUC를 보고 얼마나 정확한지 알 수 있음

bias trace off  
결코 버릴 수 없는 값

underfitting  
fitting을 제대로 못한 것들

overfitting  
fitting을 너무 많이해서 근삿값, 분포도를 제대로 잡지 못함

one-hot encoding = 한값만 가지는거 << 검색해보자

image data  
pixel 강도와 edge  
대상이 어떻게 detection이 되었느냐  
어떤 정보의 꼭지를 잡고있는 것 = 메타 데이터  
ex) 한국어의 메타데이터 : 한글  
NRP 메타데이터 : 명사 대명사 ...  


*** Text preprocessing  
텍스트데이터  
tokenization : 가방이 : 가방 + 이 Tokenization  
lowercasing : 첫글자대문자(이런 정보 필요없음), 소문자로 만들어줌 : lowercasing  
temoval of special characters : ㅋㅋㅋ ㅎㅎㅎ , ' 없애줌  
contraction expansions : 같은 문자라고 앞뒤 맥락에 따라서 순서나 의미가 다름  
stopword removal : , ' !  
spell corrections : 오타  
streamming and lemmatization : stramming 꽃을 잘라놓고 이게 어떤 꽃이냐 물어보는 것, lying -> lie 까지 바꿀수있는것


feature engineering  
어떤것이 얽혔을 때 이것을 의미화 한다

bag of words model : 순서같은거 생각안하고 마구 집어넣는 것, 똑같은 단어가 많이 나오면 그것이 키워드  
키워드 뽑기는 쉬우나 오류가 생길가능성이 있음,  
TF-IDF model : 키워드를 제대로 찾는것

filter methods : 채워넣기  
wrapper methods :  
embedded methods : 특정한것  

deep learning


여태까지한거 `session.run()`을 해서 기록을 볼 수 있음
`tf.global_variables_initializer`을 호출하여 명시적으로 초기화해야함

```python
from __future__ import print_function
import tensorflow as tf

g = tf.Graph()
```

- RNN
x에서 ht값으로 가는 과정
x와 h가 멀어질 수록 관계성이 멀어질 수 있음
RNN의 한계점이 있으니 LSTM을 꼭 사용
기억을 더 잘하려고 씀
- LSTM - Long Short Term Memory
가장 먼저 Forget할 것을 올림
데이터와 tan을 pointwise operation을 해 중요하다 싶은 것은 위로 올림
한번더 그냥 보낼지 옆 레이어로 보낼지 결정하게됨

- 딥러닝은 feature engineering이 자동화되는것


- tensorflow는 세션 기반, 그림을 그리고 아키텍쳐 속에서 한꺼번에 처리
- keras는 tensorflow를 백엔드로 두고 인터프리터처럼 중간 중간 결과를 보여줌

- 선형 뉴런 
x값을 통해   
선을 찾아내는 과정  

- 비선형 뉴런

- autoencoder
내부가 어떻게 되었든 내가 입력한 값을 그대로 나오게 해라
- variational autoencoder
>>>>>>> 29624fb7e8cd336937a0e2f5298b2f5c8bb42e77
