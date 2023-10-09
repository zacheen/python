# -*- coding: utf-8 -*-
import json

test_file_path = r'./test_json.json'

# 把 str 轉成 dict
str1 = '{"id": 123, "Name": "wsrsw", "Email": "wsrsw@example.com"}'
json_2_dict = json.loads(str1)
print("json to dict : ",type(json_2_dict))
print(json_2_dict)

# 把 dict 轉成 json 
dict_2_json = json.dumps([json_2_dict, json_2_dict])
print("dict to json : ",type(dict_2_json))
print(dict_2_json)

# dict 轉成 json 可以使用 indent 讓 str 更易讀
dict_2_json = json.dumps(json_2_dict, indent = 4)
print("dict to json : ",type(dict_2_json))
print(dict_2_json)

# json 寫入 txt 
    # 當然也可以轉成 str，再用寫 str 的方式寫入 txt
with open(test_file_path, 'w') as fw:
    json.dump(json_2_dict, fw, indent = 4)

# ensure_ascii=False 可以解決寫入時中文變成編碼的問題
with open(test_file_path, 'w', encoding='UTF-8') as fw:
    json.dump(json_2_dict, fw, indent = 4, ensure_ascii=False)

# 從 txt 讀取 json
with open(test_file_path, encoding='UTF-8') as fr:
    read_json = json.load(fr)
    print("read from json txt : ",type(read_json))
    print(read_json)

input("wait")

import os
os.remove(test_file_path)



