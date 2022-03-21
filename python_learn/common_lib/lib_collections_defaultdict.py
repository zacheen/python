# 如果找不到此值 會做 def_value 回傳東西
from collections import defaultdict
  
# # < 設定 def_value > 
# # 方法1 
# def def_value():
#     return "Not Present"
# d = defaultdict(def_value)
# # 方法2
# d = defaultdict(lambda: "Not Present")

# # < 使用方法跟 dict 一樣 >
# d["a"] = 1
# d["b"] = 2
  
# print(d["a"]) # 存在回傳相應值
# print(d["b"])
# print(d["c"]) # < 不存在回傳 def_value 的設定 >


#----------------------------------------------------------
# < 特殊用法 >
# <def_value帶入list> == 各自的key會對應一個list 且list會自動初始化
# Defining a dict
d = defaultdict(list)
for i in range(5):
    d[i].append(i)
print("Dictionary with values as list:",d)
