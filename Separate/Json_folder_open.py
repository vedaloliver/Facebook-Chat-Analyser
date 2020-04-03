import json
import pdb
import random
from collections import Counter
from datetime import datetime
from nltk import ngrams
import os.path
from pathlib import Path

path_dir = os.path.join("JSON_Files","Sam")
json_files = [pos_json for pos_json in os.listdir(path_dir) if pos_json.endswith('json')]
print (json_files)

json_text_list = []

for index, js in enumerate(json_files):
    with open(os.path.join(path_dir, js), "r") as json_data:
        json_text_list.append(json.load(json_data))


#with open('message_1.json') as json_data:


jsondata2 = []
for i in range(len(json_text_list)):
    jsondata2 +=(json_text_list[i]['messages'])


print(len(jsondata2))
