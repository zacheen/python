# 354. Russian Doll Envelopes
# https://leetcode.com/problems/russian-doll-envelopes/description/

from typing import List
from math import inf
from bisect import bisect_left

# my 
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort( key=lambda x: (x[0], -x[1]) )
        # print(envelopes)

        # template LIS
        stack = [inf]
        for n1,n2 in envelopes :
            if n2 > stack[-1] :
                stack.append(n2)
            else :
                stack[bisect_left(stack,n2)] = n2
        return len(stack)

s = Solution()
print("ans :",s.maxEnvelopes([[5,4],[6,4],[6,7],[2,3]])) # 3
print("ans :",s.maxEnvelopes([[1,1],[1,1],[1,1]])) # 1
print("ans :",s.maxEnvelopes([[4,5],[4,6],[6,7],[2,3],[1,1]])) # 4



