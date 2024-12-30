# 2872. Maximum Number of K-Divisible Components
# https://leetcode.com/problems/maximum-number-of-k-divisible-components/description/

from typing import List
import functools

# my 115ms Beats81.71%
from collections import defaultdict
class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        links = defaultdict(list)
        for n1,n2 in edges :
            links[n1].append(n2)
            links[n2].append(n1)
        ans_cou = 0
        def DFS(now_n, prev_n):
            nonlocal ans_cou
            total_rem = values[now_n]
            for next_n in links[now_n] :
                if next_n != prev_n :
                    total_rem += DFS(next_n, now_n)
            total_rem = total_rem % k
            if total_rem == 0 :
                ans_cou += 1
            return total_rem
        DFS(0, -1)
        return ans_cou

# given ans
# the same, but using [[] for _ in range(n)] instead of defaultdict(list)

s = Solution()
print("ans :",s.maxKDivisibleComponents(n = 5, edges = [[0,2],[1,2],[1,3],[2,4]], values = [1,8,1,4,4], k = 6)) #2
print("ans :",s.maxKDivisibleComponents(n = 7, edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]], values = [3,0,6,1,5,2,1], k = 3)) #3



