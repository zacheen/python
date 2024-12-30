# 原本就要跑 for 迴圈
    # 另外一個 [ for ] : 看起來比較快
    # 每次 append : 不知道為什麼 leetcode 這個比較快
    

import time
ll = list([i, i] for i in range(20000000))

### 另外一個 [ for ]  #######################
start = time.time()
for n in ll :
    n[0] = 1
ano_list =list( n[0] for n in ll )
end = time.time()
print("new li :",end - start, len(ano_list))

### 每次 append  #######################
start = time.time()
ano_list = []
for n in ll :
    n[0] = 1
    ano_list.append(n[1])
end = time.time()
print("in for :",end - start, len(ano_list))




