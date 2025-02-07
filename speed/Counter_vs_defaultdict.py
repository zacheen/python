# 要計數
    # defaultdict(int) : 較快
    # Counter          : 較慢 (笑死)

import time
from collections import Counter, defaultdict
from random import randint

len_n = 5000000
ll = list(randint(0, len_n//4) for _ in range(len_n))

start = time.time()
cou = Counter()
for n in ll :
    cou[n] += 1
end = time.time()
print("Counter    :",end - start) # 2.62

start = time.time()
cou = defaultdict(int)
for n in ll :
    cou[n] += 1
end = time.time()
print("defaultdict:",end - start) # 2.14

start = time.time()
cou = Counter()
for n in ll :
    cou[n] += 1
end = time.time()
print("Counter    :",end - start) # 2.69
