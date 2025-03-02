# for n in [:]      Faster
# for i in range(): Slower

import time
ll = list(range(100000000))

start = time.time()
for n in ll[:len(ll)//3] :
    n = n*2
end = time.time()
print("slice :",end - start) # 3.01

start = time.time()
for i in range(len(ll)//3) :
    n = ll[i]*2
end = time.time()
print("range :",end - start) # 4.16