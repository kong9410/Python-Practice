## R연습  

행과 열을 갖는 것 dataFrame

print("내용") 출력하는 함수

factorial(숫자) 팩토리얼을 구하는 함수

rep(number, times) times만큼 number를 반복하여 나타냄

runif(number) 난수 설정 함수

plot(x, y) 그래프를 그리는 함수

변수 <- 값 일반적인 프로그램언어와 달리 <- 를 사용해 변수 선언 및 값 설정

sum(numbers) 합을 구하는 함수

read.csv(csv file in workspace folder) csv파일을 읽어들이는 함수  
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
