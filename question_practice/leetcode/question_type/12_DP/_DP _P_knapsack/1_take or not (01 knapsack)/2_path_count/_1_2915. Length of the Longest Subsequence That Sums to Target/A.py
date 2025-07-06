# 2915. Length of the Longest Subsequence That Sums to Target
# https://leetcode.com/problems/length-of-the-longest-subsequence-that-sums-to-target

from typing import List
from math import inf
from collections import defaultdict

# my using template v1 : 2071ms Beats77.78%
def knapsack_01_max_cnt(nums, target):
    dp = [0] + [-inf]*(target)
    for num in nums:
        for i in range(target, num-1, -1): # 從大到小
            dp[i] = max(dp[i], dp[i-num]+1)
    return dp[-1] if dp[-1] != -inf else -1

# my using template v2 (if sparse) : 1119ms Beats95.35%
def knapsack_01_max_cnt(nums, target):
    mem = defaultdict(int)
    mem[0] = 0
    for num in nums:
        for s, l in mem.copy().items() :
            if (new_s := s+num) <= target :
                if (new_l := l+1) > mem[new_s] :
                    mem[new_s] = new_l
    if target in mem :
        return mem[target]
    else :
        return -1

class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        return knapsack_01_max_cnt(nums, target)

s = Solution()
print("ans :",s.lengthOfLongestSubsequence(nums = [1,2,3,4,5], target = 9)) # 3
print("ans :",s.lengthOfLongestSubsequence(nums = [4,1,3,2,1,5], target = 7)) # 4
print("ans :",s.lengthOfLongestSubsequence(nums = [1,1,5,4,5], target = 3)) # -1



