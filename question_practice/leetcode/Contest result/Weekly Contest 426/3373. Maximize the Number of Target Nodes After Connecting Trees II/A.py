# 3373. Maximize the Number of Target Nodes After Connecting Trees II
# https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-ii/description/

from typing import List
import functools

# my 409ms Beats89.38%
class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        # 1 找出 edge 2 max link point
        node_num_2 = len(edges2)+1
        links = [[] for _ in range(node_num_2)]
        for n1,n2 in edges2 :
            links[n1].append(n2)
            links[n2].append(n1)
        even_count_1 = 0
        even_flag = True
        bfs_stack = [0]
        seen = set()
        while bfs_stack :
            next_round = []
            for each_n in bfs_stack :
                if each_n in seen :
                    continue
                seen.add(each_n)
                if even_flag :
                    even_count_1 += 1
                for each_l in links[each_n] :
                    next_round.append(each_l)
            bfs_stack = next_round
            even_flag = not even_flag
        even_count_1 = max(even_count_1, (node_num_2-even_count_1))
        # print("even_count_1 :",even_count_1)
        
        # 2 找出 edge 1 max link point + max_edge_2
        node_num_1 = len(edges1)+1
        links = [[] for _ in range(node_num_1)]
        for n1,n2 in edges1 :
            links[n1].append(n2)
            links[n2].append(n1)
        even_mem = [None]*node_num_1
        even_flag = True
        bfs_stack = [0]
        while bfs_stack :
            next_round = []
            for each_n in bfs_stack :
                if even_mem[each_n] != None :
                    continue
                if even_flag :
                    even_mem[each_n] = True
                else :
                    even_mem[each_n] = False
                for each_l in links[each_n] :
                    next_round.append(each_l)
            bfs_stack = next_round
            even_flag = not even_flag
        count_even_2 = even_mem.count(True)
        count_odd_2 = node_num_1-count_even_2
        return [(count_even_2 if flag else count_odd_2)+even_count_1 for flag in even_mem]

# given ans

s = Solution()
print("ans :",s.maxTargetNodes(edges1 = [[0,1],[0,2],[2,3],[2,4]], edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]]))
print("ans :",s.maxTargetNodes(edges1 = [[0,1],[0,2],[0,3],[0,4]], edges2 = [[0,1],[1,2],[2,3]]))

