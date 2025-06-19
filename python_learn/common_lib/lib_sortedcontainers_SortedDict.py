from sortedcontainers import SortedDict
# 存進去時就會自動排序好
from operator import neg 

## SortedDict #######################################
# # <初始化>
ll = {1:"d",2:"a",3:"z",4:"y"}
sd = SortedDict(ll)
print("key從小到大 :",sd)
# <相反方向> 
    # 沒有 reverses 或 key 參數
from functools import cmp_to_key
def reverse_cmp(a, b):
    return b - a  # 讓大的排前面（降序）
sd = SortedDict(cmp_to_key(reverse_cmp))
sd.update(ll)
print("key從大到小 :",sd)

ll = {1:"d",2:"a",3:"z",4:"y"}
sd = SortedDict(ll)
# # <<< 語法 >>> <<< 用法 >>> 
# <新增項目>
sd[5] = "e"
print("after adding :",sd)
# # <取值> 同 dict 用法
print("sd[3] :",sd[3])

# # <刪除> 同 dict 用法
del sd[3]
print("after del :",sd)

