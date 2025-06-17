# 使用 if X in set 先檢查再 add :
#                不檢查直接 add : 

import time
from functools import reduce
import operator


start = time.time()
ll = set()
for i in range(1000000):
    if i not in ll:
        ll.add(i)
for i in range(1000000):
    if i not in ll:
        ll.add(i)
end = time.time()
print("check   :",end - start) # 0.25

start = time.time()
ll = set()
for i in range(1000000):
    ll.add(i)
for i in range(1000000):
    ll.add(i)
end = time.time()
print("nothing :",end - start) # 0.22