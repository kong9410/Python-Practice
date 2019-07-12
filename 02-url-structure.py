#python url parsing 하기
#url 구조
#scheme:[//user:password@]host[:port][/]#path[?query[#fragment]]

from urllib.parse import urlparse
result = urlparse('https://username:password@www.python.org:8080/doc/;parameter?q=example#hoge')
print('geturl', result.geturl())
print('scheme', result.scheme)
print('netloc', result.netloc)
print('username', result.username)
print('password', result.password)
print('hostname', result.hostname)
print('port', result.port)
print('path', result.path)
print('parameter', result.params)
print('query', result.query)
print('fragment', result.fragment)
print(result.index('https'))
print(result.count('https'))
