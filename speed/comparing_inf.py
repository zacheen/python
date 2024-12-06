# 結論 :
# max 跟 min 執行速度相同
    
# math.inf跟數字 比較慢
#     數字跟數字 比較快

ll = list(range(1000000))

import time

# # max min 一樣快
# start = time.time()
# for i in range(100) :
#     max(ll)
# end = time.time()
# print("max:",end - start)

# start = time.time()
# for i in range(100) :
#     min(ll)
# end = time.time()
# print("min:",end - start)

# inf 比較慢
import math
start = time.time()
for i in range(10000000) :
    max(math.inf, 0)
end = time.time()
print("max inf:",end - start)

start = time.time()
for i in range(10000000) :
    max(1, 0)
end = time.time()
print("min:",end - start)
