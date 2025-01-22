# product vs 兩個 for
    # 純取出組合
        # product : 較快
        # for     : 較慢
    # 要處理結果
        # product : 較慢
        # for     : 較快

import time
from itertools import product

n = 6000
ll = list(range(n))
ll2 = list(range(n))

# 先做一次抵銷創建空間的時間
comb = list( (n1,n2) for n1 in ll for n2 in ll2)

# 純取出組合
start = time.time()
comb = list(product(ll,ll2))
end = time.time()
print("product:",end - start) # 較快 # 28.04

start = time.time()
comb = list( (n1,n2) for n1 in ll for n2 in ll2)
end = time.time()
print("for    :",end - start) # 較慢 # 52.05

# 要處理結果
start = time.time()
comb = list( n1+n2 for n1,n2 in product(ll,ll2))
end = time.time()
print("product:",end - start) # 較慢 # 15.23

start = time.time()
comb = list( n1+n2 for n1 in ll for n2 in ll2)
end = time.time()
print("for    :",end - start) # 較快 # 9.44