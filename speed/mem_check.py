# 快
# using List : 2.1711947917938232
    # 即使加了兩個判斷 : 2.2689096927642822
# 慢
# using Set  : 2.3597166538238525

import time
import random

n = 3000000

# using List
start = time.time()
mem = [False]*(n+1)
for _ in range(n):
    mem[random.randint(0, n)] = True
    # # 即使加了兩個判斷還是比較快
    # if _ == 1 :
    #     mem[random.randint(0, n)] = True
    # elif _ > 100000 : 
    #     mem[random.randint(0, n)] = False
    # else :
    #     mem[random.randint(0, n)] = True
end = time.time()
print("mem list:",end - start)

# using Set
start = time.time()
mem = set()
for _ in range(n):
    mem.add(random.randint(0, n))
end = time.time()
print("mem set :",end - start)