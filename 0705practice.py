

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
# type 1
def scalar_vector_product(scalar, vector):
    result = []
    for value in vector:
        result.append(scalar*value)
    return result

interation_max = 1000

vector = list(range(interation_max))
scalar = 2

for _ in range(interation_max):
    result = scalar_vector_product(scalar, vector)
print(result)

# type 2
interation_max = 1000
vector = list(range(interation_max))
scalar = 2
for _ in range(interation_max):
    result = [scalar * value for value in range(interation_max)]
print(result)

# type2가 type1보다 코드가 더 짧고 실행시간이 더 빠르다는 것을 확인할 수 있다.

# enumerate 함수는 주로 딕셔너리형, 인덱스를 키로, 단어를 값으로 하여 쌍으로 묶는다.
#zip 함수는 1개 이상의 리스트 값이 같은 인덱스에 있을 때 병렬로 묶는 함수이다.
alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3']
# {0, (a1, b1)}
for i, (a, b) in enumerate(zip(alist, blist)):
    print(i,a,b)

# 람다는 선언 없는 함수라고 보면된다. 구조는 같고 표현이 다를 뿐이다.
def f(x, y):
    return x + y
print(f(1,4))
f = lambda x, y : x + y
print(f(1,4))
