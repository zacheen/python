# ll[::-1] vs ll.reverse()
# ll.reverse() 比較快

import time
ll = list(i for i in range(20000000))

### ll.reverse() #######################
start = time.time()
ll.reverse()
for n in ll :
    if n == 0 :
        n = 1
end = time.time()
print("reverse   :",end - start)

### ll[::-1] #######################
start = time.time()
for n in ll[::-1] :
    if n == 0 :
        n = 1
end = time.time()
print("list back :",end - start)


