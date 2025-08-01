# 1824. Minimum Sideway Jumps
# https://leetcode.com/problems/minimum-sideway-jumps/description/

from typing import List
from math import inf
from itertools import pairwise

# my 837ms Beats82.24%
class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        obstacles = list(n-1 for n in obstacles)
        min_move = [1,0,1]
        for obs_pos1, obs_pos2 in pairwise(obstacles) :
            if obs_pos2 == -1 : # 不需要移動
                continue
            # 前面有石頭，只能跳到 obs_pos1 沒有石頭的位置
            new_min_move = [inf, inf, inf]
            for next_pos in range(3):
                if next_pos != obs_pos1 and next_pos != obs_pos2 :
                    if min_move[next_pos] != inf :
                        new_min_move[next_pos] = min_move[next_pos]
                    else :
                        new_min_move[next_pos] = min(n for i,n in enumerate(min_move) if i != next_pos) +1
            min_move = new_min_move
        return min(min_move)

s = Solution()
print("ans :",s.minSideJumps([0,1,2,3,0])) # 2
print("ans :",s.minSideJumps([0,1,1,3,3,0])) # 0
print("ans :",s.minSideJumps([0,2,1,0,3,0])) # 2



