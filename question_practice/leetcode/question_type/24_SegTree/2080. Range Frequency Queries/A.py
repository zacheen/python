# 2080. Range Frequency Queries
# https://leetcode.com/problems/range-frequency-queries/description

from typing import List
from math import inf

# my 1666ms Beats5.37%
import heapq
import bisect
class RangeFreqQuery:
    def __init__(self, arr: List[int]):
        self.n = len(arr)
        # init
        self.tree = [None for _ in range(self.n)] + [[n] for n in arr]
        for i in range(self.n-1, 0, -1):
            self.tree[i] = list(heapq.merge(self.tree[2*i], self.tree[2*i+1]))

    def query(self, left: int, right: int, value: int) -> int:
        # include
        left += self.n
        right += self.n
        res = 0
        while left <= right:
            if left & 1 :
                # combine result
                sort_l = self.tree[left]
                res += bisect.bisect_right(sort_l, value) - bisect.bisect_left(sort_l, value)
                left += 1
            if not (right & 1) :
                # combine result
                sort_l = self.tree[right]
                res += bisect.bisect_right(sort_l, value) - bisect.bisect_left(sort_l, value)
                right -= 1
            left >>= 1
            right>>= 1
        return res

# given ans : 126ms Beats87.60%
from bisect import bisect_left, bisect_right
from collections import defaultdict
class RangeFreqQuery:
    def __init__(self, arr: List[int]):
        self.mem = defaultdict(list)
        for i,n in enumerate(arr) :
            self.mem[n].append(i)
        # no needed
        # for l in self.mem.values() :
        #     l.sort()

    def query(self, left: int, right: int, value: int) -> int:
        if len(self.mem[value]) == 0 : return 0
        sort_l = self.mem[value]
        return bisect_right(sort_l, right) - bisect_left(sort_l, left)

