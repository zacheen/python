# 3424. Minimum Cost to Make Arrays Identical
# https://leetcode.com/problems/minimum-cost-to-make-arrays-identical/description/

from typing import List
import functools

# fail : didn't see "into any number" ...
# my 229ms Beats100.00%
class Solution:
    def minCost(self, arr: List[int], brr: List[int], k: int) -> int:
        ans = sum(abs(n1-n2) for n1,n2 in zip(arr, brr))
        arr.sort()
        brr.sort()
        ans2 = sum(abs(n1-n2) for n1,n2 in zip(arr, brr)) + k
        return min(ans, ans2)

s = Solution()
print("ans :",s.minCost(arr = [-7,9,5], brr = [7,-2,-5], k = 2)) # 13



