# 3593. Minimum Increments to Equalize Leaf Paths
# https://leetcode.com/problems/minimum-increments-to-equalize-leaf-paths/description/

from typing import List
from math import inf
from collections import defaultdict

# my 227ms Beats96.88%
class Solution:
    def minIncrease(self, n: int, edges: List[List[int]], cost: List[int]) -> int:
        li = [[] for _ in range(n)]
        # build
        for n1,n2 in edges :
            li[n1].append(n2)
            li[n2].append(n1)

        def dfs(root, p_node):
            max_val = 0
            max_cou = 0
            total_cou = 0
            for leaf in li[root] :
                if leaf != p_node :
                    past_max, cou = dfs(leaf, root)
                    if past_max > max_val :
                        max_val = past_max
                        max_cou = 1
                    elif past_max == max_val :
                        max_cou += 1
                    total_cou += cou
            total_cou += len(li[root]) - max_cou - (p_node != -1)
            
            # slow : 752ms Beats5.74%
            # info = [ for leaf in li[root] if leaf != p_node]
            # if len(info) == 0 :
            #     return cost[root], 0
            # max_val = max(i[0] for i in info)
            # total_cou = sum(i[1] for i in info)
            # total_cou += sum(i[0] != max_val for i in info)
            return max_val+cost[root], total_cou
        
        return dfs(0,-1)[1]

s = Solution()
print("ans :",s.minIncrease(n = 3, edges = [[0,1],[0,2]], cost = [2,1,3])) # 
print("ans :",s.minIncrease(n = 3, edges = [[0,1],[1,2]], cost = [5,1,4])) # 0
print("ans :",s.minIncrease(n = 5, edges = [[0,4],[0,1],[1,2],[1,3]], cost = [3,4,1,1,7])) # 1
# print("ans :",s.minIncrease()) # 

