from urllib.parse import urlparse, parse_qs, parse_qsl

urls = 'https://www.python.org/?field1=value1&field2=value2&field3=value3'
result = urlparse(urls)
print(result.query)
a = parse_qs(result.query)
print(a)
b = parse_qsl(result.query)
print(b)
