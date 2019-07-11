## R연습  

행과 열을 갖는 것 dataFrame  
화면 지우기 ctrl+l  
범주형 Factor

출력  
```R
print("내용")
```

팩토리얼  
```R
factorial(숫자)
```

times만큼 number를 반복하여 나타냄  
```R
rep(number, times)
```

난수 설정 함수  
```R
runif(number)
```

그래프를 그리는 함수  
```R
plot(x, y)
```

#### 변수 <- 값 일반적인 프로그램언어와 달리 <- 를 사용해 변수 선언 및 값 설정

합을 구하는 함수  
```R
sum(numbers) 
```

```R
read.csv(csv file in workspace folder) #csv파일을 읽어들이는 함수  
read.csv(csv file in workspace folder, stringAsFactor = False) #False로 두면 string을 factor가 아닌 chr형식으로 받는다.
```

데이터의 변수나 행정보를 볼 수 있는 함수  
```R
str(df)   
```

NA 아무것도 없는 상태를 말함  
NULL 초기화가 되지 않은 상태를 말함

```R
is.numeric(value) #숫자이면 TRUE 아니면 FALSE
is.na(value) #NA이면 TRUE 아니면 FALSE
is.character(value) #문자인지 확인
is.null(value) #NULL인지 확인
is(a) #어떤 데이터 타입인지 확인
```

논리 연산자 : &, |, !

\# 주석

범주형 데이터타입 : ex 남자 or 여자  
```R
factor(value, levels) 
```  
```R
bloodtype <- factor("A", c("A", "B", "C", "AB"))
```

c(\*values) sclar를 묶어놓은 vector이다.

tip : 3.14등의 소수점 연산을 할때 100같은 것을 곱해 정수로 만들고 연산후 다시 100을 나눈다

example1 ::  
```R
d <- c(1,2,"hi")  
d의 결과 = "1", "2", "hi" == char의 영향력이 더 크다  
데이터 크기 : integer < double < character < list
```

example2 ::  
```R
d1<-c(1,2,3,4,5)  
d2<-c("a", "b", "c", "d", "e")  
d3<-c(1.1, 2.2, 3.3, 4.4, 5.5)  
df<-data.frame(d1,d2,d3)  
data.frame은 2차원 배열 형식으로 만든다.
```

example3 ::  
```R
df <- data.frame(num=d1, name=d2, avg=d3)  
```
데이터 프레임에 대한 변수이름을 바꾸고 싶을 때 사용한다.  
바꿀 이름을 앞, 원래 변수명을 뒤에

```R
install.packages("패키지명")  #패키지 설치  
install.packages("hflights") #hflights 패키지 설치
```

```R
library(패키지명) #패키지 임포트  
library(hflights) #hflights 패키지 임포트
```

원하는 자료를 갯수만큼 보여주라  
```R
head(패키지명, 갯수) 
```

패키지or데이터프레임명$칼럼명 데이터프레임에서 특정 칼럼의 value값을 추출  
```R
hfligths$AirTime  
```

원하는 개수만 출력  
```R
head(hflights$AirTime, 10)
```

첫번째 칼럼 value를 추출  
```R
head(hflights[1]) 
```

```R
class(hflights) #hflights의 클래스 타입 출력  
class(hflights[11]) #hflights의 11번째의 클래스 타입 출력 => 1개의 데이터를 가진 dataFrame  
class(hflights[[11]]) #hflights의 11번째의 데이터 하나하나 타입 => 1개의 데이터 integer
hflights[1,2] #1행 2열 값  
hflights[c(1,11)] #1행과 11행의 값들을 반환  
hflights[c("Origin", "Dest")] #칼럼 번호 대신 칼럼명으로 쓸 수도 있음
```

부분 집합 데이터 프레임  
```R
subset(hflights, select = c("Year", "Month")) 
```  
사실상 hflights[c("Year", "Month")]와 같음

```R
colnames(데이터프레임명) # 데이터프레임의 칼럼 명을 반환  
colnames(데이터프레임명)[인덱스] # 칼럼프레임에서 ?번째 칼럼명 반환  
colnames(데이터프레임명)[인덱스] <- "다른 칼럼명" # 칼럼명 변환  
colnames(데이터프레임명) <- c("칼럼1", "칼럼2" ...) # 여러개의 칼럼명을 한꺼번에 변환
```

데이터프레임명$칼럼명 + 숫자  데이터에 숫자만큼 전부 더해줌

데이터프레임에 추가로 칼럼과 데이터값을 붙여줌  
```R
cbind(데이터프레임명, 추가데이터프레임) 
```

데이터프레임에 있는 특정 칼럼의 value의 횟수를 카운트해서 테이블로 만들어줌  
```R
table(데이터프레임$칼럼명) 
```

데이터프레임 vlaue 갯수세기  
```R
length(CountOfDest) 
```

범위 구하기  
```R
range(a) 
```

example ::  
```R
CountOfDest[CountOfDest == 1] # CountOfDest 테이블에서 value가 1인 값을 찾기
```

각 칼럼에 대한 값들과 합을 보여줌  
```R
addmargins(table, margin) 
```

막대그래프로 보여줌 main은 제목 x, y 좌표 이름, col은 색상  
```R
barplot(table, main="title", xlab="x_name", ylab="y_name", col="#00ff00") 
```

데이터 가져오기
```R
data("variable name") 
```

#### 그래프
점 그래프 만들기  
```R
plot(dataframe$x, dataframe$y, main="title", xlab="x_name", ylab="y_name", pch=20, cex=0.5, type="l", lty=1) 
```
pch는 점 모양  
cex는 점 그림 크기 배수  
type은 그래프 형태, 'l'이면 라인, 'b'는 점과 선, 'o'는 오버랩 <help탭 확인>  
lty는 1~6까지, 선의 형태 결정(실선, 점선 등)  
```R
points(iris$Petal.Width, iris$petal.Length, pch="+", col="RED)
#기존 plot에 points를 더 추가
```

dfss[1]의 자료형을 factor로 변환  
```R
dfss[1] <- as.factor(dfss$schoolname) 
```

모든 행의 8열을 나타냄  
```R
df[,8] 
```

```R
subset(dfss, subset = something > 100) # dfss에서 something 칼럼이 100개 초과인 데이터 프레임을 나타냄  
subset(dfss, select = -something) # dfss에서 something 칼럼을 제거  
subset(dfss, select = c(-s1, -s2, ...) # dfss에서 여러개 칼럼을 제거할 때
```

vector는 숫자형 데이터프레임, index는 분류기준, function은 sum이나 avg등 처리함수  
```R
tapply(vector, index, function) 
```

1부터 10까지 자동생성  
```R
c(1:10)
```

여러개의 데이터 프레임, 리스트, 함수 등을 묶어 하나의 리스트로 만듦  
```R
list(a, b, c, d) 
```

character형으로 변환  
```R
as.character(some) 
```

열의 개수가 3개인 1부터 9까지 증가하는 행렬 만듦  
```R
matrix(1:9, ncol=3) 
```

데이터 프레임 형태로 만든다  
```R
as.data.frame() 
```

#### 제어문  
if문, else문 c언어와 똑같이 중괄호와 같이 작성  
ifelse(조건, "참", "거짓") 조건에 따라 두번째 혹은 세번째가 실행됨  
for(i in 1:10){} 1부터 10까지 반복문  
while(조건){} 똑같음


```R
next() # C의 continue와 비슷함  
break  # C의 break와 같음
```

example::
```R
sum(1:3, NA, na.rm = TRUE) 
#1,2,3,na를 더할 때 na를 지움
```

```R
na.rm = TRUE # na를 다 제거  
na.ommit(x) # na를 생략  
na.pass(x) # na를 패스
```

###함수만들기
myFunc <- function(a){} 일반적인 함수 만들기  
```R
f <- function(x){
    a <- 1
    #함수 속에 함수를 만들 수 있다.
    g <- function(y){
        print(y+a)
    }
    g(x)
}
```

그래프 표에 주석달기  
```R
legend("topright", legend=c("Sepal", "Petal"), pch=c(20,43), col=c("blue", "red"), bg="gray")
```

히스토그램 (빈도수로 표현)  
```R
hist(iris$Sepal.Width)
```  
히스토그램 (밀도로 표현)  
```R
hist(iris#Sepal.Width, freq=FALSE)
```

라인 그래프  
```R
plot(destiny(iris$Sepal.Width))
```

그려져 있는 그래프에서 라인 그래프 추가  
```R
lines(density(iris$Sepal.Width))
```

### 상관관계

```R
aq2 <- na.omit(airqulity[,c(1:4)])	#airquality 데이터셋
cor(aq2) # NA값이 있을시 계산 결과 NA
```  
결과값 : minus관계는 수치가 커지면 그 관계의 상대는 작아지는 것

```R
plot(aq2) # 상관관계 그래프
pairs(aq2, panel = panel.smooth) # 기울기 그래프로 그려준다
```

### 분석 패키지

##### PerformanceAnalytics 패키지

```R
install.packages("PerformanceAnalytics")
library("PerformanceAnalytics")
```

자기자신에 대해서는 히스토그램, 다른 상관관계는 수치형식과 관계그래프로 보여줌
```R
chart.Correlation(aq2, histogram = TRUE, pch=19)
```

##### corrplot 패키지

corr 패키지 설치  
```R
install.packages("corrplot")
library("corrplot")
```

corrplot 도표 만들기
```R
aq.cor <- cor(aq2) # aq2에 대한 상관관계 데이터프레임 만들기
corrplot(aq.cor, method="number") # 숫자로 상관관계 표만들기
corrplot(aq.cor, method="square")
corrplot(aq.cor, method="circle")
corrplot(aq.cor, method="ellipse")
corrplot(aq.cor, method="shade", addshade="all", t1.col="red", diag=FALSE, addCoef.col="black", arder="FPC")
corrplot(aq.cor, method="pie")
corrplot(aq.cor, method="color")
```


범위 지정 후 자르는 함수  
```R
# cancer$age는 40세, 70세 등의 나이정보를 가지고있다.
doa <- table(cut(cancer$age, breaks = (1:9)*10))
# ( : 포함이 안됨, [ : 포함됨
```

이름 바꾸기
```R
rownames(doa)<-c("10대", "20대", "30대", "40대", "50대", "60대", "70대", "80대")
```

##### GGTHEMES

```R
install.packages("ggthemes")
library(ggplot2)
library(ggthemes)
```

```R
ggplot(data=cancer, aes(x=age))+geom_freqpoly(binwidth=20, size=3, colour="blue")+theme_bw()
# binwidth는 좌우 폭, theme_bw()는 바깥 테두리
```


#### 데이터 읽기

기존의 read.csv는 파일이 클 경우에는 시간이 오래걸림  
그래서 data.table이라는 것을 사용

```R
install.packages("data.table")
library("data.table")
df <- fread("cafe_1.csv", header=TRUE, stringsAsFactors=TRUE) #타이틀이 있는 경우 header
```


인덱스 값 찾기  
```R
doy <- table(df$year)
which(rownames(doy)=="2007")
fr <- table(df$status, df$year)
which(colnames(fr)=="2007")
```

비율 알기  
```R
prop.table(fr, margin=2) #margin 비교개수
```

데이터 프레임 만들기
```R
newdf <- data.frame(colnames(fr),fr[1,], fr[2,], pfr[1,], pfr[2,])
```

#### 문자 관련 패키지
```R
install.packages("stringr")
library(stringr)
```

NA값 가지고 있는 행 지우기
```R
df1<-df1[complete.cases(df1), ]
```

##### 10,000 꼴의 문자 숫자로 변환하기
```R
# 3,4번째 항목이 바꿔야할 숫자일 때
for(i in 3:4){
    df1[,i]<-sapply(df1[,i], function(x) gsub(",", "", x))  # ","를 ""로 변환
    df1[,i]<-as.numeric(df1[,i])   #문자열을 숫자로 변환
}
```


누적 그래프  
```R
ggplot(mtcars, aes(x=factor(cyl)))+geom_bar(aes(fill=factor(gear)))
```

박스 그래프
```R
ggplot(airquality, aes(x=Day, y=Temp, group=Day))+geom_boxplot()
```

히스토그램
```R
ggplot(airquality, aes(Temp))+geom_histogram()
```

기울기가 있는 그래프
```R
ggplot(economics, aes(x=date, y=psavert))+geom_line()+geom_abline(intercept = 12.18671, slope = -0.000544)
#intercept는 절편, slope는 기울기
ggplot(economics, aes(x=date, y=psavert))+geom_line()+geom_hline(yintercept = 12.18671, mean(economics$psavert))
ggplot(economics, aes(x=date, y=psavert))+geom_line()+geom_vline(xintercept = 2010)
```

텍스트와 같이 있는 그래프
```R
ggplot(airquality, aes(x=Day, y=Temp))+geom_point()+geom_text(aes(label=Temp, vjust=0, hjust=0))
```

영역표시
```R
ggplot(mtcars, aes(x=wt, y=mpg))+geom_point()+annotate("rect", xmin = 3, ymin = 12, xmax = 4, ymax = 21, alpha = 0.5, fill = "skyblue")
ggplot(mtcars, aes(x=wt, y=mpg))+geom_point()+annotate("rect", xmin = 3, ymin = 12, xmax = 4, ymax = 21, alpha = 0.5, fill = "skyblue")+annotate("segment", x = 2.5, xend = 3.7, y = 10, yend = 17, color = "red", arrow = arrow())
```

labs 함수
```R
ggplot(mtcars, aes(x = gear))+geom_bar()+labs(x = "기어 수", y = "자동차 수", title = "변속기 기어별 자동차수")
```

격자무늬 생성
```R
ggplot(mtcars, aes(x = gear))+geom_bar()+labs(x = "기어 수", y = "자동차 수", title = "변속기 기어별 자동차수")+theme_linedraw()
```

googleVis
```R
install.packages("googleVis")
library(googleVis)
```

움직이는 차트 실행하기
```R
motion <- gvisMotionChart(ecnomics, idvar = "psavert", timevar = "date")
plot(motion)
```

게이지 모션 차트
```R
gauge <- gvisGauge(CityPopularity, labelvar = "City", numvar = "Popularity", options = list(min = 0, max = 1000))
plot(gauge)
```

다양한 형태의 그래프 사용  
MASS 사용
```R
install.packages(MASS)
library(MASS)
x <- (1:10)
y <- x^2/log(x+1)
plot(x,y)
M1 <- rnorm(200, 3, 1)
M2 <- rnorm(200, 3, 10)
bivn.kde <- kde2d(M1, M2, n=50)
op <- par(mfrow = c(2,2))
plot(x, y)
contour(bivn.kde)
image(bivn.kde)
persp(bivn.kde, phi = 10, theta = 30, col = "gray")
par(op)
```

#### 회귀 분석
```R
lm(mpg ~ hp, data = mtcars)
# ~앞이 종속변수, ~뒤가 독립변수
# Intercept는 절편, hp의 값이 기울기
```

자동차 속도와 제동거리 관계
```R
m<-lm(dist~speed, data=cars)
#dist = -17.579 + 3.932 * speed
abline(m)
#예측
pre <- predict(m, interval = "confidence")
head(pre, 10)
#lwr 하한치, upr 상한치
predict(m, newdata = data.frame(speed=100))
#speed가 100일때 제동거리 예측
```

dplyr패키지
```R
install.packages("dplyr")
library(dplyr)
```

필터링
```R
filter(mtcars, cyl==4) #실린더가 4개인 자동차만 추출
```

정렬
```R
arrange(mtcars, mpg) #데이터와 정렬기준
arrange(mtcars, desc(mpg))
arrange(mtcars, mpg, desc(wt))
```

데이터프레임만들기
```R
dfss <- select(mtcars, mpg, cyl, hp, wt)
```

열 추가하기, 순위 매기기
```R
mutate(mtcars, mpg_rank = rank(mpg))
```

중복 제거하기
```R
distinct(mtcars, cyl)
```

요약하기
```R
summarise(mtcars, cyl_mean = mean(cyl), cyl_min = min(cyl), cyl_max(cyl))
```

##### mean(), median(), sd():표준편차, min(), max(), sum()

그룹화하기
```R
gp_cyl <- group_by(mtcars, cyl)
```

단순 갯수 세기
```R
summarise(gr_cyl, n())
# table함수와 비슷
```

중복 값을 빼고 갯수 세기
```R
summarise(gr_cyl, n_distinct(gear))
```

랜덤하게 값을 뽑는 함수
```R
sample_n(mtcars, 10)
```

전체 갯수에서 20%만 뽑기
```R
sample_frac(mtcars, 0.2)
```

#### 파이프 연산자  
서로 연결하는 연산자
```R
%>%
```

example::  
```R
group_by(mtcars, cyl) %>% summarise(n())
```

다음과 같은 연산이 있다.
```R
mp_rank <- mutate(mtcars, mpg_rank=rank(mpg))
arrange(mp_rank, mpg_rank)
```
이것을 파이프 연산자로 한꺼번에 처리할 수 있다.
```R
mp_rank <- mutate(mtcars, mpg_rank=rank(mpg)) %>% arrange(mp_rank, mpg_rank)
```
다음 방법으로 mtcars에 있는 mpg열을 뽑아낼 수 있다.
```R
mtcars %>% select(mpg)
```


#### melt 사용하기  
패키지 설치
```R
install.packages("reshape2")
library(reshape2)
```

melt사용해보기
```R
names(airquality) <- tolower(names(airquality, id.vars="ozone"))
melt_test <- melt(airquality, id.vars="ozone")
melt_test2 <- melt(airquality, id.vars = c("month", "wind", measure.vars = "ozone")
```

세로로 긴 데이터 모양을 가로로 전환하는 함수  
cast()

