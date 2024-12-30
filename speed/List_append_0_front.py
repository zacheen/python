# ll.insert(0, 0) : 快
# [0] + [ll]      : 慢

import time
from collections import deque

ll = list(range(100000))
# 1. insert
start = time.time()
for i in range(10000) : 
    ll.insert(0, 0) 
end = time.time()
print("insert :",end - start)

ll = list(range(100000))
# 2. slice
start = time.time()
for i in range(10000) : 
    ll = [0]+ll
end = time.time()
print("slice  :",end - start)


