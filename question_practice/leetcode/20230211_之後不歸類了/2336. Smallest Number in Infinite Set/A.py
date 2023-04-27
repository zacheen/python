from typing import List
import functools

# my Beats 24.45%
# 我的想法是 紀錄已經拿出什麼數字
    # 但是 sort 就是比 heap 慢
from sortedcontainers import SortedSet
class SmallestInfiniteSet:
    def __init__(self):
        self.popitem = SortedSet([0])

    def popSmallest(self) -> int:
        left = 0
        right = len(self.popitem)
        while left < right:
            mid = (left + right) >> 1
            if self.popitem[mid] <= mid: # 條件 (如果 == target 的情況 要是 False)
                # 沒通過 或 數字應該要往大的方向跑(目標沒有在 left 跟 mid 之間)
                left = mid + 1
            else:
                # 通過(包含 == target 的情況)
                right = mid 
        
        self.popitem.add(left)
        return left

    def addBack(self, num: int) -> None:
        self.popitem.discard(num)

# given ans Beats 91.48%
# 一樣是正著做 只不過紀錄了目前最大值 超出範圍就擴大界線
    # 正著做才可以用 tree
import heapq
class SmallestInfiniteSet:
    def __init__(self):
        self.curr = 1
        self.added = []
        self.added_set = set()

    def popSmallest(self) -> int:
        if not self.added :
            self.curr+=1
            return self.curr-1
        min = heapq.heappop(self.added)
        self.added_set.remove(min)
        return min

    def addBack(self, num: int) -> None:
        if (num < self.curr) :
            if num not in self.added_set :
                heapq.heappush(self.added, num)
                self.added_set.add(num)

# s = Solution()
# print(s.())



