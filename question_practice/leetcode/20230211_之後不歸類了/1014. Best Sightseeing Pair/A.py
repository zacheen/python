# 1014. Best Sightseeing Pair
# https://leetcode.com/problems/best-sightseeing-pair/description

from typing import List
import functools

# my 63ms Beats78.05%
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_l = 0
        max_ans = 0
        for indx, v in enumerate(values) :
            max_ans = max(max_ans, max_l + v - indx )
            max_l = max(max_l, indx + v)
        return max_ans

# given ans 59ms Beats83.66%
# by using -1 to trace the distance
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_l = 0
        max_ans = 0
        for v in values :
            max_ans = max(max_ans, max_l + v)
            max_l = max(max_l, v) -1
        return max_ans

s = Solution()
print("ans :",s.maxScoreSightseeingPair()) # 



