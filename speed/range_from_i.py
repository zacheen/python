# 如果前面幾個沒有要跑 
    # ll[開始位置:] 比較快
    # range(開始位置, 長度) 比較慢

import time
ll = list(range(100000))

start = time.time()
for i in ll :
    ret = i
end = time.time()
print(end - start)

start = time.time()
# 比較快
for _ in range(500):
    for i in ll[1:] :
        ret = i
end = time.time()
print(end - start)

start = time.time()
# 比較慢
for _ in range(500):
    for i in range(1,len(ll)) :
        ret = ll[i]
end = time.time()
print(end - start)
