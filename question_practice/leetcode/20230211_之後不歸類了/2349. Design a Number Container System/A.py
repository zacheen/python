# 2349. Design a Number Container System
# https://leetcode.com/problems/design-a-number-container-system/description

from typing import List
from math import inf
import bisect
from collections import defaultdict

# my 
class NumberContainers:
    def __init__(self):
        self.mem = defaultdict(list)
        self.indx_to_num = {}

    def change(self, index: int, number: int) -> None:
        # remove pre
        if index in self.indx_to_num :
            pre_n = self.indx_to_num[index]
            i = bisect.bisect_left(self.mem[pre_n], index)
            del(self.mem[pre_n][i])
        # update
        self.indx_to_num[index] = number
        i = bisect.bisect_right(self.mem[number], index)
        self.mem[number].insert(i, index)

    def find(self, number: int) -> int:
        l = self.mem[number]
        return -1 if len(l) == 0 else l[0]

import heapq
# given ans : 97ms Beats91.18%
# find always get the smallest indx and check whether it is valid
class NumberContainers:
    def __init__(self):
        self.mem = defaultdict(list)
        self.indx_to_num = {}

    def change(self, index: int, number: int) -> None:
        # update
        self.indx_to_num[index] = number
        heapq.heappush(self.mem[number], index)

    def find(self, number: int) -> int:
        l = self.mem[number]
        while l :
            indx = l[0]
            if self.indx_to_num[indx] == number :
                return indx
            heapq.heappop(l)
        return -1 






