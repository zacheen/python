# 997. Find the Town Judge
# https://leetcode.com/problems/find-the-town-judge/description

from typing import List
from math import inf

# my v1 : 7ms Beats91.48%
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        out_degree = [0]*(n+1)
        in_degree = [0]*(n+1)
        for p1,p2 in trust :
            out_degree[p1] += 1
            in_degree[p2] += 1
        
        other_n = n-1
        for i, (out_n,in_n) in enumerate(zip(out_degree, in_degree)) :
            if i == 0 : continue
            if out_n == 0 and in_n == other_n :
                return i
        return -1
    
# my v2 : 8ms Beats86.08%
    # I thought it would be faster, but not
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        out_degree = set(range(n+1))
        out_degree.discard(0)
        in_degree = [0]*(n+1)
        for p1,p2 in trust :
            out_degree.discard(p1)
            in_degree[p2] += 1
        
        other_n = n-1
        for poss_i in out_degree :
            if in_degree[poss_i] == other_n :
                return poss_i
        return -1

s = Solution()
print("ans :",s.findJudge(n = 2, trust = [[1,2]])) # 2



