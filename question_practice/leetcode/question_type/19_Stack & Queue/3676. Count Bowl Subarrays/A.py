# 3676. Count Bowl Subarrays
# https://leetcode.com/problems/count-bowl-subarrays/

from typing import List
from math import inf

# my : 73ms Beats99.22%
# fail once that I want to count the decrease part and multiply with increasing part
    # but for example [5,4,3,2,1,2,3] is not a valid answer
class Solution:
    def bowlSubarrays(self, nums: List[int]) -> int:
        stack_decreasing = []
        ans = 0
        for n in nums :
            # since all the previous point is below the last point, I only have to check the final one
            while stack_decreasing and stack_decreasing[-1] < n :
                stack_decreasing.pop()
                if stack_decreasing :
                    ans += 1
            stack_decreasing.append(n)
        return ans


s = Solution()
print("ans :",s.bowlSubarrays([2,5,3,1,4])) # 
print("ans :",s.bowlSubarrays([5,1,2,3,4])) # 
# print("ans :",s.bowlSubarrays()) # 



