# 不管 shift 幾位數，速度都差不多

import time

start = time.time()
for _ in range(10000000) :
    _ = 100000 << 1
end = time.time()
print("<< 1   :",end - start) # 0.54677

start = time.time()
for _ in range(10000000) :
    _ = 100000 << 100
end = time.time()
print("<< 100 :",end - start) # 0.54608