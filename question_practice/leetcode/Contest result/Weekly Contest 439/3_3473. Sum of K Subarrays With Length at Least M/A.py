# 3473. Sum of K Subarrays With Length at Least M
# https://leetcode.com/problems/sum-of-k-subarrays-with-length-at-least-m/description/

from typing import List
from math import inf
from functools import cache
from itertools import accumulate

# optimized : O(n*k)
# given ans : 2266ms Beats96.46%
class Solution:
    def maxSum(self, nums: List[int], k: int, m: int) -> int:
        len_n = len(nums)
        prefix = [0] + list(accumulate(nums))
        dp = [0] * (len_n + 1) # 在nums[:i]的範圍 最大的subarray結果
        for j in range(1, k + 1):
            discard = inf
            new_dp = [-inf]*(len_n + 1)
            for i in range(j*m, len_n + 1): # 前面得要預留 j*m 的空間
                # 前面被去掉的總和
                discard = min(discard, prefix[i-m] - dp[i-m])
                # don't take : new_dp[i-1]
                # take : 現在的總和 - 最少前面要去掉的總和(每一個for都會更新)
                new_dp[i] = max(new_dp[i-1], prefix[i] - discard)
            dp = new_dp
        return dp[len_n]

# my : 4982ms Beats59.37% : O(n*k*m)
class Solution:
    def maxSum(self, nums: List[int], k: int, m: int) -> int:
        nums_acc = list(accumulate(nums[::-1]))
        nums_acc.reverse()

        @cache
        def dp(now_i, now_k, now_m):
            if now_k < 0 :
                return -inf
            if now_k == 0:
                if now_i >= len(nums):
                    if now_m <= 0 :
                        return 0
                    else :
                        return -inf
            if now_k*m == (len(nums)-now_i) :
                # fast forward
                return nums_acc[now_i]

            now_n = nums[now_i]
            ret = -inf
            if now_m != -1 : # last one isn't dont take
                # continue last subarray
                if (r:=dp(now_i+1, now_k, max(now_m-1, 0))+now_n) > ret :
                    ret = r

            if now_m <= 0 : # can seperate here
                # dont take
                if (r:=dp(now_i+1, now_k, -1)) > ret :
                    ret = r
                # new subarray
                if (r:=dp(now_i+1, now_k-1, m-1)+now_n) > ret :
                    ret = r
            return ret
        ans = dp(0,k,-1)
        dp.cache_clear()
        return ans

s = Solution()
print("ans :",s.maxSum(nums = [1,2,-1,3,3,4], k = 2, m = 2)) # 13, [1,2], [3,3,4] 
print("ans :",s.maxSum(nums = [-10,3,-1,-4], k = 4, m = 1)) # -12, [-10],[3],[-1],[-4]
print("ans :",s.maxSum(nums = [-2,-10,15,12,8,11,5], k = 3, m = 2)) # 41, [-10,15],[12,8],[11,5]
print("ans :",s.maxSum(nums = [-8,1,-8,6,-9,5], k = 1, m = 3)) # 2, [6,-9,5]



