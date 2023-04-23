from queue import PriorityQueue
# from sortedcontainers import SortedList 比較好用

## SortedXX 系列的語法完全相同
## SortedList #######################################
ll = [3,5,1,2,7,6,4]
# # <初始化>
pq = PriorityQueue()

# 放入項目
pq.put(5)
pq.put(3)
pq.put(1)
pq.put(4)
pq.put(2)

# 取出項目 一定會從最小的開始取
print(pq.get())
print(pq.get())

pq.put(1)
pq.put(5)
print(pq.get())
print(pq.get())