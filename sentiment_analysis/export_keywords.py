import json
import re
from konlpy.tag import Okt
from collections import Counter

with open('./text.json', 'r', encoding="utf-8") as json_file:
	text = json.load(json_file)

# 제목이랑 내용 가져오기
title = text["detail"]["TITLE"]
content = text["detail"]["CONTENT"]

# 태그 없애기
content = re.sub('<.+?>', '', content, 0).strip()
okt = Okt()
nouns = okt.pos(content)
print(nouns)
'''
count = Counter(nouns)

tag_count = []
tags = []
print(content)
for n, c in count.most_common(30):
	dics = {'tag':n, 'count':c}
	if dics['count'] <= 2:
		break
	if len(dics['tag']) >= 2 and len(tags) <= 49:
		tag_count.append(dics)
		tags.append(dics['tag'])

for tag in tag_count:
	print(tag)
'''
