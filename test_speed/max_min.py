# 加號與減號速度差別

ll = list(range(1000000))

import time

# # max min 一樣快
# start = time.time()
# max(ll)
# end = time.time()
# print("max:",end - start)

# start = time.time()
# min(ll)
# end = time.time()
# print("min:",end - start)

# inf 比較慢
import math
start = time.time()
for i in range(1000000) :
    max(-math.inf, 0)
end = time.time()
print("max inf:",end - start)

start = time.time()
for i in range(1000000) :
    max(-1, 0)
end = time.time()
print("min:",end - start)
