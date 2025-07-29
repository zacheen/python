# 2044. Count Number of Maximum Bitwise-OR Subsets
# https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets

from typing import List
from math import inf
from functools import reduce
from collections import defaultdict

# my 1ms Beats100.00%
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = reduce(lambda n1,n2 : n1|n2, nums)
        comb = defaultdict(int) # comb[i] actually i would be sparse
        for n in nums :
            for last_or, last_comb in list(comb.items()) :
                comb[ last_or|n ] += last_comb
            comb[ n ] += 1
        return comb[max_or]

s = Solution()
print("ans :",s.countMaxOrSubsets([3,1])) # 2
print("ans :",s.countMaxOrSubsets([2,2,2])) # 7
print("ans :",s.countMaxOrSubsets([3,2,1,5])) # 



