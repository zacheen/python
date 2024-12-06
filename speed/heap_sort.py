# 結論 :
# 1 排序
    # heap : O(n) 快
    # sort : O(nlogn)
# 2 插入
    # heap : O(logn) 快
    # sort : O(nlogn) 主要是因為 list insert 很花時間
# 3 取出所有項目 (不會更改順序)
    # heap : O(logn)
    # sort : O(1) 快

import random
import time
import heapq
import bisect

N = 2000000
heap_list = [random.randint(0,N) for _ in range(N)]
sort_list = heap_list.copy()

# 1 排序 ############################################################
start = time.time()
heapq.heapify(heap_list)
end = time.time()
print("heap order :",end - start)

start = time.time()
sort_list.sort()
end = time.time()
print("sort order :",end - start)

# 2 插入 ############################################################
insert_list = [random.randint(0,N) for _ in range(N//1000)]

start = time.time()
for n in insert_list :
    heapq.heappush(heap_list, n)
end = time.time()
print("heap insert :",end - start)

start = time.time()
for n in insert_list :
    sort_list.insert(bisect.bisect_right(sort_list, n), n)
end = time.time()
print("sort insert :",end - start)

# 單純 insert 跟上面時間差不多 代表時間大部分的確花在這裡
start = time.time()
for n in insert_list :
    sort_list.insert(N//2, n)
end = time.time()
print("list insert :",end - start)

# 3 取出所有項目 (不會更改順序) #############################################
insert_list = [random.randint(0,N) for _ in range(N//200)]

start = time.time()
for _ in range(N) :
    heapq.heappop(heap_list)
end = time.time()
print("heap pop :",end - start)

start = time.time()
for _ in range(N) :
    sort_list.pop()
end = time.time()
print("sort pop :",end - start)