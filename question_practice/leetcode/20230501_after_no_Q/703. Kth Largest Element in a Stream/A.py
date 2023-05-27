# 703. Kth Largest Element in a Stream
# https://leetcode.com/problems/kth-largest-element-in-a-stream/description/

from typing import List
import functools

# my Beats 13.14%
from sortedcontainers import SortedList
from operator import neg 
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.l = SortedList(nums, key=neg)
        del(self.l[k:])

    def add(self, val: int) -> int:
        self.l.add(val)
        del(self.l[self.k:])
        # print(self.l)
        return self.l[self.k-1]
    
# given ans Beats 51.12%
import heapq
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.l = heapq.nlargest(k, nums)
        heapq.heapify(self.l)

    def add(self, val: int) -> int:
        if len(self.l) < self.k:
            heapq.heappush(self.l, val)
        elif val > self.l[0]:
            heapq.heapreplace(self.l, val)
        return self.l[0]



