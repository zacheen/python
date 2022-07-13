# 加號與減號速度差別

pos1 = 3
pos2 = 2

import time

start = time.time()
for i in range(1000000) :
    ret = pos1 - pos2
end = time.time()
print("減法:",end - start)

start = time.time()
for i in range(1000000) :
    ret = pos1 + pos2
end = time.time()
print("加法:",end - start)

start = time.time()
for i in range(1000000) :
    ret = -pos2
end = time.time()
print("負號:",end - start)

start = time.time()
for i in range(1000000) :
    ret = pos1 + (-pos2)
end = time.time()
print("先負號 再相加:",end - start)
