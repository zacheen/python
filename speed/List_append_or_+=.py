# extend : 比較快 (extend 跟 += 速度幾乎相同)
# +=     : 比較快
# append : 比較慢

import time
add_l = list(range(10000000))
ll1 = list(range(10000000))
ll2 = list(range(10000000))
ll3 = list(range(10000000))

start = time.time()
ll1 += add_l
end = time.time()
print("+=    :",end - start, len(ll1)) # 0.070

start = time.time()
for item in add_l :
    ll2.append(item)
end = time.time()
print("append:",end - start, "",len(ll2)) # 1.14

start = time.time()
ll3.extend(add_l)
end = time.time()
print("extend:",end - start, len(ll3)) # 0.068