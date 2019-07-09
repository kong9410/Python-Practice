## R연습  

행과 열을 갖는 것 dataFrame  
화면 지우기 ctrl+l  
범주형 Factor

print("내용") 출력하는 함수

factorial(숫자) 팩토리얼을 구하는 함수

rep(number, times) times만큼 number를 반복하여 나타냄

runif(number) 난수 설정 함수

plot(x, y) 그래프를 그리는 함수

변수 <- 값 일반적인 프로그램언어와 달리 <- 를 사용해 변수 선언 및 값 설정

sum(numbers) 합을 구하는 함수

read.csv(csv file in workspace folder) csv파일을 읽어들이는 함수  
read.csv(csv file in workspace folder, stringAsFactor = False) False로 두면 string을 factor가 아닌 chr형식으로 받는다.
str(df) 불러들여온 파일의 변수나 행정보를 볼 수 있다  

NA 아무것도 없는 상태를 말함

NULL 초기화가 되지 않은 상태를 말함

is.numeric(value) 숫자이면 TRUE 아니면 FALSE

is.na(value) NA이면 TRUE 아니면 FALSE

is.character(value) 문자인지 확인

is.null(value) NULL인지 확인

is(a) 어떤 데이터 타입인지 확인

논리 연산자 : &, |, !

\# 주석

factor(value, levels) 범주형 데이터타입 : ex 남자 or 여자  
bloodtype <- factor("A", c("A", "B", "C", "AB"))

c(\*values) sclar를 묶어놓은 vectord이다.

tip : 3.14등의 소수점 연산을 할때 100같은 것을 곱해 정수로 만들고 연산후 다시 100을 나눈다

example1 :: d <- c(1,2,"hi")  
d의 결과 = "1", "2", "hi" == char의 영향력이 더 크다  
데이터 크기 : integer < double < character < list

example2 ::  
d1<-c(1,2,3,4,5)  
d2<-c("a", "b", "c", "d", "e")  
d3<-c(1.1, 2.2, 3.3, 4.4, 5.5)  
df<-data.frame(d1,d2,d3)  
data.frame은 2차원 배열 형식으로 만든다.

example3 ::  
df <- data.frame(num=d1, name=d2, avg=d3)  
데이터 프레임에 대한 변수이름을 바꾸고 싶을 때 사용한다.  
바꿀 이름을 앞, 원래 변수명을 뒤에

install.packages("패키지명")  패키지 설치  
install.packages("hflights") hflights 패키지 설치

library(패키지명) 패키지 임포트  
library(hflights) hflights 패키지 임포트

head(패키지명, 갯수) 원하는 자료를 갯수만큼 보여주라

패키지or데이터프레임명$칼럼명 데이터프레임에서 특정 칼럼의 value값을 추출  
hfligths$AirTime  
head(hflights$AirTime, 10) 원하는 개수만 출력

head(hflights[1]) 첫번째 칼럼 value를 추출

class(hflights) hflights의 클래스 타입 출력  
class(hflights[11]) hflights의 11번째의 클래스 타입 출력 => 1개의 데이터를 가진 dataFrame  
class(hflights[[11]]) hflights의 11번째의 데이터 하나하나 타입 => 1개의 데이터 integer
hflights[1,2] 1행 2열 값  
hflights[c(1,11)] 1행과 11행의 값들을 반환  
hflights[c("Origin", "Dest")] 칼럼 번호 대신 칼럼명으로 쓸 수도 있음

subset(hflights, select = c("Year", "Month")) 부분 집합 데이터 프레임  
사실상 hflights[c("Year", "Month")]와 같음

colnames(데이터프레임명) 데이터프레임의 칼럼 명을 반환  
colnames(데이터프레임명)[인덱스] 칼럼프레임에서 ?번째 칼럼명 반환  
colnames(데이터프레임명)[인덱스] <- "다른 칼럼명" 칼럼명 변환  
colnames(데이터프레임명) <- c("칼럼1", "칼럼2" ...)  여러개의 칼럼명을 한꺼번에 변환

데이터프레임명$칼럼명 + 숫자  데이터에 숫자만큼 전부 더해줌

cbind(데이터프레임명, 추가데이터프레임) 데이터프레임에 추가로 칼럼과 데이터값을 붙여줌

table(데이터프레임$칼럼명) 데이터프레임에 있는 특정 칼럼의 value의 횟수를 카운트해서 테이블로 만들어줌

length(CountOfDest) 데이터프레임 vlaue 갯수세기 

range(a) 범위 구하기

example :: CountOfDest[CountOfDest == 1] CountOfDest 테이블에서 value가 1인 값을 찾기

addmargins(table, margin) 각 칼럼에 대한 값들과 합을 보여줌

barplot(table, main="title", xlab="x_name", ylab="y_name", col="#00ff00") 막대그래프로 보여줌 main은 제목 x, y 좌표 이름, col은 색상

data("variable name") 데이터 가져오기

#### 그래프

plot(dataframe$x, dataframe$y, main="title", xlab="x_name", ylab="y_name", pch=20, cex=0.5, type="l", lty=1) 점 그래프 만들기  
pch는 점 모양  
cex는 점 그림 크기 배수  
type은 그래프 형태, 'l'이면 라인, 'b'는 점과 선, 'o'는 오버랩 <help탭 확인>  
lty는 1~6까지, 선의 형태 결정(실선, 점선 등)  
```R
points(iris$Petal.Width, iris$petal.Length, pch="+", col="RED)
#기존 plot에 points를 더 추가
```

dfss[1] <- as.factor(dfss$schoolname) dfss[1]의 자료형을 factor로 변환

df[,8] 모든 행의 8열을 나타냄

subset(dfss, subset = something > 100) dfss에서 something 칼럼이 100개 초과인 데이터 프레임을 나타냄  
subset(dfss, select = -something) dfss에서 something 칼럼을 제거  
subset(dfss, select = c(-s1, -s2, ...) dfss에서 여러개 칼럼을 제거할 때

tapply(vector, index, function) vector는 숫자형 데이터프레임, index는 분류기준, function은 sum이나 avg등 처리함수

c(1:10) 1부터 10까지 자동생성

list(a, b, c, d) 여러개의 데이터 프레임, 리스트, 함수 등을 묶어 하나의 리스트로 만듦

as.character(some) character형으로 변환

matrix(1:9, ncol=3) 열의 개수가 3개인 1부터 9까지 증가하는 행렬 만듦

as.data.frame() 데이터 프레임 형태로 만든다

if문, else문 c언어와 똑같이 중괄호와 같이 작성  
ifelse(조건, "참", "거짓") 조건에 따라 두번째 혹은 세번째가 실행됨  
for(i in 1:10){} 1부터 10까지 반복문  
while(조건){} 똑같음

next() C의 continue와 비슷함  
break  C의 break와 같음

example::
```R
sum(1:3, NA, na.rm = TRUE) 
#1,2,3,na를 더할 때 na를 지움
```

na.rm = TRUE na를 다 제거  
na.ommit(x) na를 생략
na.pass(x) na를 패스

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


