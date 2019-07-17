
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


