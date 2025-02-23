# 1615. Maximal Network Rank
# https://leetcode.com/problems/maximal-network-rank

from typing import List
from math import inf

import heapq
from collections import defaultdict
# my 2ms Beats99.55%
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        li = defaultdict(set)
        for n1,n2 in roads :
            li[n1].add(n2)
            li[n2].add(n1)
        mem = [ (-len(s),n) for n,s in li.items()]
        heapq.heapify(mem)

        if len(mem) < 2 :
            return 0
        t1,n1 = heapq.heappop(mem)
        t2,n2 = heapq.heappop(mem)
        if n2 not in li[n1] :
            return -(t1+t2)
        if t1 == t2 :
            rep = {n1,n2}
        else :
            rep = {n1}
        
        while mem and mem[0][0] == t2 :
            _, new_p = heapq.heappop(mem)
            if any( new_p not in li[pre] for pre in rep ) :
                return -(t1+t2)
            if len(rep) >= 2 :
                rep.add(new_p)
        return -(t1+t2) -1
        # worst case : all nodes have the same out degree, and are all connected together
            # O(n*n*logn) logn : heappop

# given ans : 22ms Beats90.85%
    # slower, but speed is more stable
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        li = [set() for _ in range(n)]
        for n1,n2 in roads :
            li[n1].add(n2)
            li[n2].add(n1)

        max_ans = 0
        for n1, n1l in enumerate(li) :
            for n2, n2l in enumerate(li[:n1]) :
                if (t := len(n1l)+len(n2l)-(n2 in n1l)) > max_ans :
                    max_ans = t
        # worst case : O(n*n)
        return max_ans

s = Solution()
# print("ans :",s.maximalNetworkRank(n = 8, roads = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]])) # 5 > 2 & 5
# print("ans :",s.maximalNetworkRank(n = 2, roads = [])) # 0
print("ans :",s.maximalNetworkRank(n = 5, roads = [[2,3],[0,3],[0,4],[4,1]])) # 0



