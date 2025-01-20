# 1473. Paint House III
# https://leetcode.com/problems/paint-house-iii/description/

from typing import List
import functools

# my 1476ms Beats18.49%
    # actually most of the route cannot reach the final result, so most of the time are wasted
from collections import defaultdict
from math import inf
class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        mem = {-1: [0]+[inf]*target} # [last_indx][nei_cou] : cost
        for h,c in zip(houses, cost):
            new_mem = defaultdict(lambda : [inf]*(target+1))
            if h == 0 :
                for new_col, new_cost in enumerate(c) :
                    new_col += 1
                    for last_c, tar_cost in mem.items():
                        for tar, past_cost in enumerate(tar_cost) :
                            if last_c == new_col :
                                new_mem[new_col][tar] = min(new_mem[new_col][tar], past_cost+new_cost)
                            else :
                                tar += 1
                                if tar > target :
                                    continue
                                new_mem[new_col][tar] = min(new_mem[new_col][tar], past_cost+new_cost)
            else :  
                for last_c, tar_cost in mem.items():
                    for tar, past_cost in enumerate(tar_cost) :
                        if last_c == h :
                            new_mem[h][tar] = min(new_mem[h][tar], past_cost)
                        else :
                            tar += 1
                            if tar > target :
                                continue
                            new_mem[h][tar] = min(new_mem[h][tar], past_cost)
            mem = new_mem
        ret = min(tar_cost[target] for last_c, tar_cost in mem.items())
        return ret if ret != inf else -1

# given ans : 172ms Beats90.07%
class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        # maps (i, t, p) -> the minimum cost to paint houses i <= h < m with t neighborhoods, where house i - 1 is color p
        dp = {}
        
		# You can use this functools line instead of dp to make it faster, but I cache 
		# manually because I don't want to abstract the caching away from the reader.
        @functools.lru_cache(None)
        def dfs(i, t, p):
            if i == len(houses) or t < 0 or m - i < t:
                # base case - we're trying to color 0 houses. Only i == len(houses) is necessary
				# to check here, but it prunes a bit of the search space to make things faster.
                return 0 if t == 0 and i == len(houses) else float('inf')
            
            if houses[i] == 0:
                return min(dfs(i + 1, t - (nc != p), nc) + cost[i][nc - 1] for nc in range(1, n + 1))
            else:
                return dfs(i + 1, t - (houses[i] != p), houses[i])
        ret = dfs(0, target, -1)
        # if ret is infinity, then we failed every case because there were too many neighborhoods
        # to start. If we could paint over houses that were previously painted, we could remedy that,
        # but the problem doesn't allow that. so, we return -1 in that case.
        return ret if ret < float('inf') else -1

s = Solution()
# print("ans :",s.minCost(houses = [0,2,1,2,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3)) # (10 + 1) = 11
# print("ans :",s.minCost(houses = [2,1,2,0], cost = [[10,1],[10,1],[1,10],[5,1]], m = 4, n = 2, target = 3)) # 1
print("ans :",s.minCost(houses = [3,1,2,3], cost = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]], m = 4, n = 3, target = 3)) # -1



