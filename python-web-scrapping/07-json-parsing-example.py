#07-json-parsing-example
import json
d = {
'foo': 'bar',
'alice': 1,
    'wonderland': [1, 2, 3]
}
with open('data.json', 'w') as f: json.dump(d, f)
with open('data.json', 'r') as f: d = json.load(f)
print(d)
