# 注意 minheap 不能取出特定 item
import heapq
    # heapq 沒有辦法自訂排序(一定是從小到大)，也沒有辦法 reverse
    # 所以如果要取出最大的，可以把 -item 放進去 (因為加負號最大的就會變最小的)

minheapList = [i for i in range(10,0,-1)]

# 把 此list sort成 minheap
# heapq 永遠是 minheap  如果要 maxheap 就把要比較的項目加負號
heapq.heapify(minheapList)
print("heapify :", minheapList)

# 加入項目      (加到最尾端後 調整那一列的順序)
heapq.heappush(minheapList, 3)
print("heappush 3 :", minheapList)

# 取出最小的項目 (取出最頂點的項目)
print("get smallset item :",heapq.heappop(minheapList))
print("heappop 1 :", minheapList)

# 下面這兩個function 不用先 heapify 就可以使用了
    # 裡面會自動判斷 要用sort 還是用heap
# 取出 前n個 最大的項目
# heapq.nlargest(n, iterable, key=None)
print("max n :",heapq.nlargest(3, minheapList))
print(minheapList)  # 原本的不會動到
# 取出 前n個 最小的項目
# heapq.nsmallest(n, iterable, key=None)
print("min n :",heapq.nsmallest(3, minheapList))  # [2, 3, 3]
print(minheapList)  # 原本的不會動到 # [2, 3, 4, 3, 6, 5, 8, 10, 7, 9]

# heapq 沒有實作 remove
# remove 項目 O(n) (找項目) + O(logn) (刪除項目之後排序)
def remove_num(value):
    rm_indx = minheapList.index(value)
    minheapList[rm_indx] = minheapList[-1]
    minheapList.pop()
    if rm_indx < len(minheapList):
        heapq._siftup(minheapList, rm_indx)
        heapq._siftdown(minheapList, 0, rm_indx)

remove_num(4)
print("remove 4 :",minheapList)  # 原本的不會動到

