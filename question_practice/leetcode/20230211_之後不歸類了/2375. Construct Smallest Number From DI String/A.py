# 2375. Construct Smallest Number From DI String
# https://leetcode.com/problems/construct-smallest-number-from-di-string

from typing import List
from math import inf

# my 0ms Beats100.00%
class Solution:
    def smallestNumber(self, pattern: str) -> str:
        ans = [str(i) for i in range(1,len(pattern)+2)]
        rev_s = 0
        for i,c in zip(range(1,len(pattern)+2),pattern+"I") :
            if c == "I" :
                ans[rev_s:i] = reversed(ans[rev_s:i])
                rev_s = i
        return "".join(ans)

# given ans
class Solution:
    def smallestNumber(self, pattern: str) -> str:
        ans = []
        stack = [1]
        for c in pattern+'I':
            maxSorFar = stack[-1]
            if c == 'I':
                while stack:
                    maxSorFar = max(maxSorFar, stack[-1])
                    ans.append(stack.pop())
            stack.append(maxSorFar + 1)
        return ''.join(str(c) for c in ans)

s = Solution()
print("ans :",s.smallestNumber("IIIDIDDD")) # 
print("ans :",s.smallestNumber("DDD")) # 
# print("ans :",s.smallestNumber()) # 



