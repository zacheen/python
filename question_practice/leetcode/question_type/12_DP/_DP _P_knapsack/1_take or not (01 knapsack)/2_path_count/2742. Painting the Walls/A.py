# 2742. Painting the Walls
# https://leetcode.com/problems/painting-the-walls

from typing import List
from math import inf
from collections import defaultdict

# my using template knapsack_01_max_cnt v2 : 573ms Beats97.49%
class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        # time愈多 cost愈少 愈好
        mem = defaultdict(lambda : inf) # mem[漆i面牆] 最少的cost是多少
        mem[0] = 0
        for t, c in zip(time, cost):
            for last_w, last_c in mem.copy().items() :
                new_w = min(len(cost), last_w +1 +t) # +1(paid painter) +t(free)
                new_c = last_c + c
                if mem[new_w] > new_c :
                    mem[new_w] = new_c
        return mem[len(cost)]

s = Solution()
print("ans :",s.paintWalls(cost = [1,2,3,2], time = [1,2,3,2])) # 3
print("ans :",s.paintWalls(cost = [1,2,3,2], time = [3,2,3,2])) # 1
print("ans :",s.paintWalls(cost = [2,3,4,2], time = [1,1,1,1])) # 4
# print("ans :",s.paintWalls()) # 



