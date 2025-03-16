# 2258. Escape the Spreading Fire
# https://leetcode.com/problems/escape-the-spreading-fire/description/

from typing import List
from math import inf
from collections import defaultdict

# my 71ms Beats98.04%
class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        len_g1 = len(grid)
        len_g2 = len(grid[0])

        fire_q = []
        for i1,l in enumerate(grid) :
            for i2,n in enumerate(l) :
                if n == 1 : 
                    grid[i1][i2] = 0
                    fire_q.append((i1,i2))

        num_cou = defaultdict(int)
        dir_list = [(0,1),(1,0),(0,-1),(-1,0)]
        queue = [(0,0)]
        reach_end = 0
        cou = -1
        ans = 10**9
        while queue or fire_q:
            # 1. people bfs to house
            new_q = []
            for p1,p2 in queue :
                if grid[p1][p2] != 0 :
                    continue
                grid[p1][p2] = cou
                num_cou[cou] += 1
                for d1, d2 in dir_list :
                    nei1 = p1+d1
                    if nei1 < 0 or nei1 >= len_g1 :
                        continue
                    nei2 = p2+d2
                    if nei2 < 0 or nei2 >= len_g2 :
                        continue
                    new_q.append((nei1, nei2))
            if reach_end == 0 and grid[-1][-1] < 0 :
                reach_end = cou
                new_q = []
            queue = new_q

            # 2. fire spread
            new_fq = []
            for p1,p2 in fire_q :
                if grid[p1][p2] > 0 :
                    continue
                past_step = grid[p1][p2]
                grid[p1][p2] = 1
                num_cou[past_step] -= 1
                if num_cou[past_step] == 0 :
                    if past_step == reach_end :
                        # 例外狀況 : 火追到人的時候是在終點 結果+1
                        ans = min(ans, past_step-cou) 
                    elif past_step == cou :
                        # 如果此點是正在走的點
                        return -1
                    else :
                        # 如果此點是過去的點
                        ans = min(ans, past_step-cou-1)
                for d1, d2 in dir_list :
                    nei1 = p1+d1
                    if nei1 < 0 or nei1 >= len_g1 :
                        continue
                    nei2 = p2+d2
                    if nei2 < 0 or nei2 >= len_g2 :
                        continue
                    new_fq.append((nei1, nei2))
            if grid[-1][-1] == 1 :
                if reach_end :
                    return ans
                else :
                    return -1
            fire_q = new_fq
            cou -= 1

        if reach_end : # 火 跟 人 都被 圍住了
            return ans
        else :
            return -1

s = Solution()
print("ans :",s.maximumMinutes([
    [0,2,0,0,0,0,0],
    [0,0,0,2,2,1,0],
    [0,2,0,0,1,2,0],
    [0,0,2,2,2,0,2],
    [0,0,0,0,0,0,0]])) # 3
print("ans :",s.maximumMinutes([[0,0,0,0],
                                [0,1,2,0],
                                [0,2,0,0]])) # -1
print("ans :",s.maximumMinutes([[0,0,0],
                                [2,2,0],
                                [1,2,0]])) # 10**9
print("ans :",s.maximumMinutes([[0,2,0,0,1],
                                [0,2,0,2,2],
                                [0,2,0,0,0],
                                [0,0,2,2,0],
                                [0,0,0,0,0]])) # 0
print("ans :",s.maximumMinutes([[0,2,1,1,0],
                                [1,2,0,0,1],
                                [2,2,1,1,0]])) # -1
print("ans :",s.maximumMinutes([[0,0,0,0,0],
                                [0,2,0,2,0],
                                [0,2,0,2,0],
                                [0,2,1,2,0],
                                [0,2,2,2,0],
                                [0,0,0,0,0]])) # 1



