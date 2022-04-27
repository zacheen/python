# 如果前面幾個沒有要跑 
    # ll[開始位置:]
    # range(開始位置, 長度)

import time
ll = list(range(100000))

start = time.time()
# 如果可以不要創造新的list最快
for i in ll :
    ret = i
end = time.time()
print(end - start)

start = time.time()
# 比較快
for i in ll[1:] :
    ret = i
end = time.time()
print(end - start)

start = time.time()
# 比較慢
for i in range(1,len(ll)) :
    ret = ll[i]
end = time.time()
print(end - start)
