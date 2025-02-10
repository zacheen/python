# 2364. Count Number of Bad Pairs
# https://leetcode.com/problems/count-number-of-bad-pairs/description

from typing import List
from math import inf

from collections import Counter
import math
# my 144ms Beats7.62%
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        # good pair : i2-i1 = n2-n1 > i2-n2 = i1-n1
        cou = Counter()
        ans = math.comb(len(nums),2)
        for indx,n in enumerate(nums) :
            diff = indx-n
            ans -= cou[diff]
            cou[diff] += 1
        return ans

# given ans
    # Optimized
        # My : (x,y) only count once
        # Opt : (x,y) and (y,x) Count both and //2
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        count = Counter([num - i for i, num in enumerate(nums)])
        n = len(nums)
        return (n * (n - 1) - sum(v * (v - 1) for v in count.values() if v > 1)) // 2

s = Solution()
print("ans :",s.countBadPairs([4,1,3,3])) # 5 : beside (1,3)
print("ans :",s.countBadPairs([1,2,3,4,5])) # 0



