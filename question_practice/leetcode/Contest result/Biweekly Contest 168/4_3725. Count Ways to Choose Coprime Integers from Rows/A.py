# 3725. Count Ways to Choose Coprime Integers from Rows
# https://leetcode.com/problems/count-ways-to-choose-coprime-integers-from-rows

from typing import List
from math import inf
from collections import defaultdict, Counter
from math import gcd
from functools import cache, lru_cache

# still have a quicker method : 倍數融斥
    # https://youtu.be/y6HAGc8URxQ?si=H-vniLrHngfp46HE&t=1172

# given ans : 1051ms Beats84.97%
MOD = 10**9+7
class Solution:
    def countCoprime(self, mat: List[List[int]]) -> int:
        @lru_cache(None)
        def dp(row_i, now_cd): # return count
            # walk through until end, if now_cd == i then fit the condition return 1
            if row_i < 0 :
                return 1 if now_cd == 1 else 0
            return sum(dp(row_i-1, gcd(now_cd, new_n)) for new_n in mat[row_i]) % MOD
        return dp(len(mat)-1, 0)

# my 1286ms Beats74.36%
MOD = 10**9+7
class Solution:
    def countCoprime(self, mat: List[List[int]]) -> int:
        cnt = defaultdict(int) # prevent empty mat
        cnt[0] = 1 # gcd 0 with other int is int itself
        for row_i, each_row in enumerate(mat) :
            new_cnt = defaultdict(int)
            # since 1 <= mat[i][j] <= 150, actually in the dict there is at most 150 key value
            for each_key, c in cnt.items() :
                for each_num in each_row :
                    com_div = gcd(each_key, each_num)
                    new_cnt[com_div] = (new_cnt[com_div] + c) % MOD
            cnt = new_cnt
        return cnt[1]



s = Solution()
print("ans :",s.countCoprime([[1,2],[3,4]])) # 3
print("ans :",s.countCoprime([[2,2],[2,2]])) # 0

