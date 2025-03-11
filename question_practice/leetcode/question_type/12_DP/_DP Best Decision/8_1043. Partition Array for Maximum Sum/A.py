# 1043. Partition Array for Maximum Sum
# https://leetcode.com/problems/partition-array-for-maximum-sum/description/

from typing import List
from math import inf
from functools import cache

# my 207ms Beats94.46%
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        @cache
        def dp(now_i) :
            if now_i >= len(arr) :
                return 0
            max_ret = 0
            max_n = arr[now_i]
            for end_i in range(now_i, min(len(arr), now_i+k)): # end_i is included in this range
                if (new_n:=arr[end_i]) > max_n :
                    max_n = new_n
                max_ret = max(max_ret, (end_i-now_i+1)*max_n + dp(end_i+1))
            return max_ret
        return dp(0)

# my dp for version : 99ms Beats99.01%
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        len_arr = len(arr)
        dp = [0]*len_arr + [0]
        for now_i in range(len_arr-1,-1,-1):
            max_sum = 0
            max_n = 0
            for addi_i in range(0,k):
                end_i = now_i+addi_i
                if end_i >= len_arr :
                    break
                if (new_n:=arr[end_i]) > max_n :
                    max_n = new_n
                new_s = max_n*(addi_i+1)+dp[end_i+1]
                if new_s > max_sum :
                    max_sum = new_s
            dp[now_i] = max_sum
        return dp[0]
            

s = Solution()
print("ans :",s.maxSumAfterPartitioning(arr = [1,15,7,9,2,5,10], k = 3)) # 84
print("ans :",s.maxSumAfterPartitioning(arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4)) # 83
print("ans :",s.maxSumAfterPartitioning(arr = [1], k = 1)) # 1



