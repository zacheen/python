# 要使用 陣列第一個值 或是 math.inf

ll = [0]
import time
import math

start = time.time()
for i in range(1000000) :
    ret = ll[0]
end = time.time()
print("第一個值:",end - start)

start = time.time()
for i in range(1000000) :
    ret = math.inf
end = time.time()
print("inf:",end - start)
