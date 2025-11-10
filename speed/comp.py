# > 跟 >= 差別
# 速度相同
# 時間差不多 應該是誤差

pos1 = 3
pos2 = 2

import time
n = 30000000

start = time.time()
for i in range(n) :
    ret = pos1 > pos2
end = time.time()
print("> :", end - start)

start = time.time()
for i in range(n) :
    ret = pos1 >= pos2
end = time.time()
print(">=:",end - start)

start = time.time()
for i in range(n) :
    ret = pos1 < pos2
end = time.time()
print("< :",end - start)

start = time.time()
for i in range(n) :
    ret = pos1 <= pos2
end = time.time()
print("<=:",end - start)
