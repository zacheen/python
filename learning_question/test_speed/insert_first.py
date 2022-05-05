# 如果前面幾個沒有要跑 
    # ll[開始位置:]
    # range(開始位置, 長度)

import time
ll1 = []
ll2 = []

start = time.time()
# 比較快
for i in range(100000) :
    ll1.append(i)
ll1.reverse()
end = time.time()
print("reverse :",end - start)

start = time.time()
# 如果可以不要創造新的list最快
for i in range(100000) :
    ll2.insert(0,i)
end = time.time()
print("insert 0 :",end - start)
