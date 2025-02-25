# add vs append
    # 使用 append : 只有稍微快一點
    # 使用 add    : 慢一點

import time
ll = list(range(50000000))

start = time.time()
l = []
for i in ll :
    l.append(i)
end = time.time()
print("append :",end - start) # 4.16

start = time.time()
s = set()
for i in ll :
    s.add(i)
end = time.time()
print("add    :",end - start) # 4.98