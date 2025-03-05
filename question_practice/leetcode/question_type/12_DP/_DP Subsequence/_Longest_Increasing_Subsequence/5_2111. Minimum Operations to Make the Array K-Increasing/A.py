# 2111. Minimum Operations to Make the Array K-Increasing
# https://leetcode.com/problems/minimum-operations-to-make-the-array-k-increasing/description/

from typing import List
from math import inf
from bisect import bisect_right

# my 83ms Beats88.61%
def LIS_nonstrict(nums):
    stack = [inf]
    for n in nums :
        if n >= stack[-1] :
            stack.append(n)
        else :
            stack[bisect_right(stack,n)] = n
    return len(stack)

class Solution:
    def kIncreasing(self, arr: List[int], k: int) -> int:
        ans = len(arr)
        for start_i in range(k):
            picked_arr = arr[start_i::k]
            ans -= LIS_nonstrict(picked_arr)
        return ans

# given ans


s = Solution()
print("ans :",s.kIncreasing(arr = [5,4,3,2,1], k = 1)) # 4
print("ans :",s.kIncreasing(arr = [4,1,5,2,6,2], k = 2)) # 0
print("ans :",s.kIncreasing(arr = [4,1,5,2,6,2], k = 3)) # 2



