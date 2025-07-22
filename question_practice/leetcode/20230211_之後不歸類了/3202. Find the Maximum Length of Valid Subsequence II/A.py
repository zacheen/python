# 3202. Find the Maximum Length of Valid Subsequence II
# https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-ii

from typing import List
from math import inf

# my : 807ms Beats92.62%
class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        # dp[n1][n2] : 到目前位置 上一個餘數為n1 這一個餘數為n2 最長的長度
        dp = [[0]*k for _ in range(k)]
        for n in nums :
            rem = n % k
            for poss_n2 in range(k):
                dp[rem][poss_n2] = dp[poss_n2][rem]+1
        return max(max(res) for res in dp)

s = Solution()
print("ans :",s.maximumLength(nums = [1,2,3,4,5], k = 2)) # 5
print("ans :",s.maximumLength(nums = [1,4,2,3,1,4], k = 3)) # 4
# print("ans :",s.maximumLength()) # 



