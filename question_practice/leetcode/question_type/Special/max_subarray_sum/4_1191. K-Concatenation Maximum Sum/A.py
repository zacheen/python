# 1191. K-Concatenation Maximum Sum
# https://leetcode.com/problems/k-concatenation-maximum-sum/description/

from typing import List
from math import inf

# my 23ms Beats99.39%
MOD = 10**9+7
class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        s = sum(arr)
        
        if k > 1 :
            arr *= 2

        total_s = 0
        max_s = 0
        for n in arr :
            total_s += n
            if total_s < 0 :
                total_s = 0
            elif total_s > max_s :
                max_s = total_s

        if s > 0 and k > 2:
            max_s += (s % MOD)*(k-2)
        return max_s % MOD

s = Solution()
print("ans :",s.kConcatenationMaxSum(arr = [1,2], k = 3)) # 9
print("ans :",s.kConcatenationMaxSum(arr = [1,-2,1], k = 5)) # 2
print("ans :",s.kConcatenationMaxSum(arr = [-1,-2], k = 7)) # 0



