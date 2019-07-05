

# 리스트 컴프리헨션
word1 = "Hello"
word2 = "World"
result = [i + j for i in word1 for j in word2]
print(result)

words = 'The quick brown fox jumps over the lazy dog'.split()
print(words)
stuff = [[w.upper(), w.lower(), len(w)] for w in words]
print(stuff)


# 이차원 리스트 만들기
case1 = ["A", "B", "C"]
case2 = ["D", "E", "A"]
result = [i+j for i in case1 for j in case2]
print(result)
result = [[i+j for i in case1] for j in case2]
print(result)

# vector와 scalar의 곱셈을 실행하는 코드이다.
interation_max = 1000
vector = list(range(interation_max))
scalar = 2
#for _ in range(interation_max):
result = [scalar * value for _ in range(interation_max) for value in range(interation_max)]
print(result)
