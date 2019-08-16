import json
from konlpy.tag import Okt

with open('./text.json', 'r', encoding="utf-8") as json_file:
	text = json.load(json_file)
print(text)
