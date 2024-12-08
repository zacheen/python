# 3372. Maximize the Number of Target Nodes After Connecting Trees I
# https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-i/description/

from typing import List
import functools

# my 1499ms Beats96.43%
class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        if k == 0 : # !! or in DFS k might be negative
            return [1]*(len(edges1)+1)
        
        def DFS(links, n, last_n, k):
            if k == 0 :
                return 1
            sum_k = 1
            for each_l in links[n] :
                if each_l == last_n :
                    continue
                sum_k += DFS(links, each_l, n, k-1)
            return sum_k
        
        # 1 找出 edge 2 max link point
        node_num_2 = len(edges2)+1
        links = [[] for _ in range(node_num_2)]
        for n1,n2 in edges2 :
            links[n1].append(n2)
            links[n2].append(n1)
        max_edge_2 = max(DFS(links, i, -1, k-1) for i in range(node_num_2))
        
        # 2 找出 edge 1 max link point + max_edge_2
        node_num_1 = len(edges1)+1
        links = [[] for _ in range(node_num_1)]
        for n1,n2 in edges1 :
            links[n1].append(n2)
            links[n2].append(n1)
        
        return [DFS(links, i, -1, k)+max_edge_2 for i in range(node_num_1)]

s = Solution()
print("ans :",s.maxTargetNodes(
    edges1 = [[0,1],[0,2],[2,3],[2,4]], 
    edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]], k = 2))
print("ans :",s.maxTargetNodes( 
    edges1 = [[0,1],[0,2],[0,3],[0,4]], 
    edges2 = [[0,1],[1,2],[2,3]], k = 1))
# print("ans :",s.maxTargetNodes())



