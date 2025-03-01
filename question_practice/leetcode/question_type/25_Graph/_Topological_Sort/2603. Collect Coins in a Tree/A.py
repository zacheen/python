# 2603. Collect Coins in a Tree
# https://leetcode.com/problems/collect-coins-in-a-tree/description/

from typing import List
from math import inf

# my 155ms Beats91.11%
class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        len_n = len(edges)+1
        li = [set() for _ in range(len_n)]
        for n1,n2 in edges :
            li[n1].add(n2)
            li[n2].add(n1)
        
        end_points = [i for i, nei in enumerate(li) if len(nei) == 1]
        step_cou = [0]*len_n
        seen_cou = 0
        while end_points :
            now_n = end_points.pop()
            seen_cou += 1
            step = step_cou[now_n]
            now_is_coin = False
            if coins[now_n] :
                now_is_coin = True
                coins[now_n] = 0
                step += 1
            for nei_n in li[now_n] :
                if now_is_coin :
                    coins[nei_n] = 1
                    step_cou[nei_n] = max(step_cou[nei_n], step)
                li[nei_n].remove(now_n)
                if len(li[nei_n]) == 1 and step_cou[nei_n] < 2 :
                        end_points.append(nei_n)

        # Have to go through each point to get all coins (, and it is tree)
        return max((len_n - seen_cou - 1)*2, 0)

s = Solution()
print("ans :",s.collectTheCoins(coins = [1,0,0,0,0,1], edges = [[0,1],[1,2],[2,3],[3,4],[4,5]])) # 2
print("ans :",s.collectTheCoins(coins = [0,0,0,1,1,0,0,1], edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[5,6],[5,7]])) # 2
print("ans :",s.collectTheCoins(coins = [1,0,0,1,1,0,0,0,0,1,0,0], edges = [[0,1],[1,2],[1,3],[2,4],[4,5],[5,6],[5,7],[4,8],[7,9],[7,10],[10,11]])) # 4



