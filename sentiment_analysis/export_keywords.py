import json
import re
import os
from konlpy.tag import Okt
from collections import Counter

workDir = os.path.abspath('./news/')
filename_list = []
contents = []
for dirpath, dirnames, filenames in os.walk(workDir):
	#for dirname in dirnames:
	#	print('\t', dirname)
	for filename in filenames:
		filename_list.append('./news/'+filename)
for filename in filename_list:
	with open(filename, 'r', encoding='utf-8') as json_file:
		text = json.load(json_file)
		content = text["detail"]["CONTENT"]
		content = re.sub('<.+?>', '', content, 0).strip()
		contents.append(content)

print(contents)

'''
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
