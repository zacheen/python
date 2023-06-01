# 如果找不到此值 會做 def_value 回傳東西
from collections import defaultdict
  
# # < 設定 def_value > 
# # 方法1 
# def def_value():
#     return "Not Present"
# d = defaultdict(def_value)
# # 方法2
# d = defaultdict(lambda: "Not Present")

# # 如果是要雙層的 defaultdict
# double_dd = defaultdict(lambda: defaultdict(int))
# print(double_dd[1][1])

# # < 使用方法跟 dict 一樣 >
# d["a"] = 1
# d["b"] = 2
  
# print(d["a"]) # 存在回傳相應值
# print(d["b"])
# print(d["c"]) # < 不存在回傳 def_value 的設定 >


#----------------------------------------------------------
# # < 特殊用法 >
# # <def_value帶入list> == 各自的key會對應一個list 且list會自動初始化
# # Defining a dict
# d = defaultdict(list)
# for i in range(5):
#     d[i].append(i)
# print("Dictionary with values as list:",d)

#----------------------------------------------------------
# # defaultdict 如果用 None 就跟普通的 dict 用法一樣
# # 不會回傳 None ! 反而會跳錯
# # 實驗1 使用 None
# key = "a"
# defaultdict_none = defaultdict(None)
# print("test :",defaultdict_none[key])
# # 實驗的結果等同以下
# key = "a"
# defaultdict_none = {}
# print("same :",defaultdict_none[key])

# # 實驗2 使用 List
# key = "a"
# defaultdict_none = defaultdict(list)
# print("test :",defaultdict_none[key])
# # 實驗的結果等同以下
# defaultdict_none = {}
# if key not in defaultdict_none.keys():
#     defaultdict_none[key] = list()
# print("same :",defaultdict_none[key])

# # 實驗3 使用 bool
# key = "a"
# defaultdict_none = defaultdict(bool)
# print("test :",defaultdict_none[key])
# # 實驗的結果等同以下
# defaultdict_none = {}
# if key not in defaultdict_none.keys():
#     defaultdict_none[key] = bool()
# print("same :",defaultdict_none[key])

