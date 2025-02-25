# += vs append
    # += 比較快

import time
add_l = list(range(10000000))
ll1 = list(range(10000000))
ll2 = list(range(10000000))

start = time.time()
ll1 += add_l
end = time.time()
print("+=    :",end - start) # 0.14

start = time.time()
for item in add_l :
    ll2.append(item)
end = time.time()
print("append:",end - start) # 2.405