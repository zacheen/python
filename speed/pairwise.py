# pairwise
    # 如果是真的需要取前後值出來 : pairwise 比較快
        # EX: for di, dj in pairwise(dir_list) :
    # 但如果有 2D list : 從 2D list 取值比較快
        # EX: for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]: 

import time
from itertools import pairwise
n = 5000000

# direction ####################################
start = time.time()
for _ in range(n) :
    for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]: 
        ret = di + dj
end = time.time()
print("normal   :",end - start) # 3.6

start = time.time()
for _ in range(n) :
    for di, dj in pairwise([0,1,0,-1,0]): 
        ret = di + dj
end = time.time()
print("pairwise :",end - start) # 5.2

start = time.time()
for _ in range(n) :
    dir_list = [0,1,0,-1,0]
    for di, dj in pairwise(dir_list): 
        ret = di + dj
end = time.time()
print("pairwise2:",end - start) # 5.5 (!!竟然比上面的慢)

# get value ####################################
l = list(range(10000000))
l2D = [(n1,n2) for n1,n2 in zip(range(9999999), range(1,10000000))]

start = time.time()
for i in range(1,len(l)) :
    temp = l[i] + l[i-1]
end = time.time()
print("normal   :",end - start) # 1.99

start = time.time()
for n1,n2 in l2D :
    temp = n1+n2
end = time.time()
print("normal 2D:",end - start) # 1.32

start = time.time()
for n1,n2 in pairwise(l) :
    temp = n1+n2
end = time.time()
print("pairwise :",end - start) # 1.44