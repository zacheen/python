# 3351. Sum of Good Subsequences
# https://leetcode.com/problems/sum-of-good-subsequences/

from typing import List
from math import inf
from collections import Counter, defaultdict

# my 451ms Beats77.78%
    # given ans using list instead of dict : 222ms
MOD = 10**9 + 7
class Solution:
    def sumOfGoodSubsequences(self, nums: List[int]) -> int:
        past_n_sum = defaultdict(int)
        past_n_cnt = defaultdict(int)
        for n in nums :
            follow_cnt = past_n_cnt[n-1] + past_n_cnt[n+1] + 1
            past_n_cnt[n] = (past_n_cnt[n] + follow_cnt) % MOD
            past_n_sum[n] = (past_n_sum[n-1] + past_n_sum[n+1] + n*follow_cnt + past_n_sum[n]) % MOD
            
            # print("past_n_cnt",past_n_cnt)
            # print("past_n_sum",past_n_sum)
        return sum(past_n_sum.values()) % MOD
        


s = Solution()
print("ans :",s.sumOfGoodSubsequences([1,2,1])) # 14
print("ans :",s.sumOfGoodSubsequences([3,4,5])) # 40
print("ans :",s.sumOfGoodSubsequences([3,4,5,3])) # 

