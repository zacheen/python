# priority queue : 通常使用heap實現
# 注意 minheap 不能取出特定 item
import heapq
    # heapq 沒有辦法自訂排序(一定是從小到大)，也沒有辦法 reverse
    # 所以如果要取出最大的，可以把 -item 放進去 (因為加負號最大的就會變最小的)

    # Building heap takes O(n) time complexity

minheapList = [i for i in range(10,0,-1)]

# 把 此list sort成 minheap
# heapq 永遠是 minheap  如果要 maxheap 就把要比較的項目加負號
heapq.heapify(minheapList)
print("heapify :", minheapList)

# 加入項目      (加到最尾端後 調整那一列的順序)
heapq.heappush(minheapList, 3)
print("heappush 3 :", minheapList)

# 取出最小的項目 (取出最頂點的項目)
# [0] 永遠會是最小的項目
print("smallest     [0] :", minheapList[0])
print("minheapList :", minheapList)
# 取出最小的項目 同時pop
print("smallest heappop :",heapq.heappop(minheapList))
print("minheapList :", minheapList)

# 先存進一個新的項目 再取出最小的項目 (跟 heapreplace 順序相反)
print("heappushpop :",heapq.heappushpop(minheapList, -2))
print("minheapList :", minheapList)
print("heappushpop :",heapq.heappushpop(minheapList, 8))
print("minheapList :", minheapList)

# 先取出最小的項目 再存進一個新的項目 (跟 heappushpop 順序相反)
print("heapreplace :",heapq.heapreplace(minheapList, -2)) # 不會回傳 -2 因為這個時候 list 裡面還沒有 -2
print("minheapList :", minheapList)
print("heapreplace :",heapq.heapreplace(minheapList, 8))
print("minheapList :", minheapList)

# 下面這兩個function 不用先 heapify 就可以使用了
    # 裡面會自動判斷 要用sort 還是用heap
# 取出 前n個 最大的項目
    # !! # 如果是 Counter 可以呼叫 most_common 替代(底層也是呼叫 nlargest)
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
print("remove 4 :", minheapList)

## <heapq.merge> #########################################
# merge 兩個 sorted list
# 時間複雜度是 O(n)
l1 = [1,3,5,8]
l2 = [2,4,9,10]
l3 = [0,6,7,11]
print("heapq.merge :", list(heapq.merge(l1,l2,l3)))