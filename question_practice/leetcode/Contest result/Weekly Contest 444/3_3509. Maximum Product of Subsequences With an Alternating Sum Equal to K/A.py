# 3509. Maximum Product of Subsequences With an Alternating Sum Equal to K
# https://leetcode.com/problems/maximum-product-of-subsequences-with-an-alternating-sum-equal-to-k

from typing import List
from functools import cache

# my inspire by given ans 3927ms Beats47.45%
class Solution:
    def maxProduct(self, nums: List[int], k: int, limit: int) -> int:
        # 505ms Beats80.61%
        len_n = len(nums)
        max_n = max(nums)
        if k >= 0 and k > (len_n+1)//2*max_n:
            return -1
        elif -k > len_n//2*max_n :
            return -1
        
        # path = []
        max_ans = -1
        @cache
        def dfs(now_i, now_s, now_mul, add_f):
            if now_i == len_n : return

            # don't take
            dfs(now_i+1, now_s, now_mul, add_f)
            
            # take
            now_n = nums[now_i]
            if add_f :
                now_s += now_n
            else :
                now_s -= now_n

            now_mul *= now_n
            if now_mul > limit or now_mul < 0:
                now_mul = -1

            nonlocal max_ans
            # path.append(now_n)
            if now_s == k :
                max_ans = max(max_ans, now_mul)
            dfs(now_i+1, now_s, now_mul, not add_f)
            # path.pop()
        dfs(0, 0, 1, True)
        dfs.cache_clear()
        return max_ans

# given ans
s = Solution()
print("ans :",s.maxProduct(nums = [1,2,3], k = 2, limit = 10)) # 6 
print("ans :",s.maxProduct(nums = [0,2,3], k = -5, limit = 12)) # -1
print("ans :",s.maxProduct(nums = [2,2,3,3], k = 0, limit = 9)) # 9
print("ans :",s.maxProduct(nums = [10,10,9,0], k = 1, limit = 20)) # 0



