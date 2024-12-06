# https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-i/description

from typing import List
import functools

# my 38ms Beats88.16%
class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        ans = 0
        now_sum = 0
        for i in range(1, n+1):
            if not (i in banned) :
                now_sum += i
                if now_sum > maxSum :
                    return ans
                ans += 1
        return ans

# given ans
# same and I believe mine is faster

s = Solution()
print("ans :",s.maxCount(banned = [1,6,5], n = 5, maxSum = 6))



