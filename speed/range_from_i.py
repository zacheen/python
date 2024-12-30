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

## 前面幾個沒有要跑 ###################

# s_indx = 1
s_indx = len(ll) // 2

start = time.time()
# 比較快
for _ in range(500):
    for i in ll[s_indx:] :
        ret = i
end = time.time()
print("slice :", end - start)

start = time.time()
# 比較慢
for _ in range(500):
    for i in range(s_indx,len(ll)) :
        ret = ll[i]
end = time.time()
print("index :", end - start)

## 一定要取 indx ###################

s_indx = len(ll) // 2 - 100

start = time.time()
# 比較快
for _ in range(500):
    for i in range(s_indx,s_indx*2) :
        ret = ll[i]
end = time.time()
print("add outside :", end - start)

start = time.time()
# 比較慢
for _ in range(500):
    for i in range(s_indx) :
        ret = ll[i+s_indx]
end = time.time()
print("add inside :", end - start)
