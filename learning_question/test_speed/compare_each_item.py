# 結論 :
# zip 比較快
# 但因為沒有任何操作是 O(n) 的 
    # 所以數量加倍 執行速度也只是加倍 不會等比上升

import time

ll1 = list(range(10000000)) + [0] + list(range(1000000))
ll2 = list(range(10000000)) + [1] + list(range(1000000))
# zip
start = time.time()
for i1, i2 in zip(ll1, ll2) : 
    if i1 != i2 :
        print(i1, i2)
        break
end = time.time()
print("zip :",end - start)

# for i
start = time.time()
for i in range(len(ll1)) : 
    if ll1[i] != ll2[i] :
        print(ll1[i], ll2[i])
        break
end = time.time()
print("for i :",end - start)

