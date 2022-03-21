from collections import Counter
## Counter #######################################

# # # <<<語法>>>
# # # <初始化>
# c = Counter()                           # a new, empty counter
# c = Counter('gallahad')                 # a new counter from an iterable
# print(c)
# c = Counter({'red': 4, 'blue': 2})      # a new counter from a mapping
# print(c)
# c = Counter(cats=4, dogs=8)             # a new counter from keyword args
# print(c)

# # <<<<< 各種型態計數 >>>>>>
# # << list >> 會計算 list 裡面的項目
# c = Counter(['eggs', 'eggs', 'ham'])
# print(c)
# # << str >> 計算這個字串中 各個字各有幾個
# s = "aabddeeeffffcdddddddd"
# count = Counter(s)
# print(count)

# # # <<< 語法 >>> <<< 用法 >>> 
# # <新增項目> 同map用法
c = Counter({'red': 4, 'blue': 2})
print(c)
c["orange"] = 1
print(c)

# # <取值> 同map用法 只是如果沒有找到 會回傳0
print(c["purple"])

# # <刪除> 同map用法 
del c["orange"] 
print(c)

# # <取得數量最多的> 參數N 代表 要回傳前幾個多的
print(c.most_common(1))
print(c.most_common(2))





## Counter end #######################################


