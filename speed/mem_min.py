# 紀錄極值
    # if 新<舊   : 較快
    # min(新,舊) : 較慢

import time
ll = list(range(10000000))

# single val ##################################################
min_n = 10000000
start = time.time()
for i, n in enumerate(ll) :
    if n < min_n :
        min_n = n
end = time.time()
print("if :",end - start) # 1.22

min_l = [10000000]*5
start = time.time()
for i, n in enumerate(ll) :
    min_n = min(min_n ,n)
end = time.time()
print("min:",end - start) # 2.82

# cal ##########################
min_n = 10000000
start = time.time()
for i, n in enumerate(ll) :
    cal = n*2
    if cal < min_n :
        min_n = cal
end = time.time()
print("if :",end - start) # 1.73

min_l = [10000000]*5
start = time.time()
for i, n in enumerate(ll) :
    min_n = min(min_n ,n*2)
end = time.time()
print("min:",end - start) # 3.28

# array ##########################
min_l = [10000000]*5
start = time.time()
for i, n in enumerate(ll) :
    if n < min_l[i%5] :
        min_l[i%5] = n
end = time.time()
print("if :",end - start) # 1.69

min_l = [10000000]*5
start = time.time()
for i, n in enumerate(ll) :
    min_l[i%5] = min(min_l[i%5] ,n)
end = time.time()
print("min:",end - start) # 3.89

