# 2438. Range Product Queries of Powers
# https://leetcode.com/problems/range-product-queries-of-powers

from typing import List
from math import inf
from functools import cache
from itertools import accumulate

# segment tree is slower
# class SegTree_Sum:

# my 32ms Beats86.96%
MOD = 10**9+7

@cache
def get_pow(pow_sum) :
    return pow(2, pow_sum, mod = MOD)

class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        powers = []
        pow_n = 0
        while n :
            if n & 1 :
                powers.append(pow_n)
            n >>= 1
            pow_n += 1

        sum_power = list(accumulate(powers, initial = 0))
        ans = []
        for st, en in queries :
            pow_sum = sum_power[en+1] - sum_power[st]
            ans.append(get_pow(pow_sum))
        return ans

s = Solution()
print("ans :",s.productQueries(n = 15, queries = [[0,1],[2,2],[0,3]])) # [2, 4, 64]
print("ans :",s.productQueries(n = 2, queries = [[0,0]])) # [2]
