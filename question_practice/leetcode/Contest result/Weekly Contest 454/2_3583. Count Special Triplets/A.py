# 3583. Count Special Triplets
# https://leetcode.com/problems/count-special-triplets

from typing import List
from math import inf
from collections import Counter

# my 821ms Beats43.83%
MOD = 10**9+7
class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        sub_cou = Counter(nums)
        ans_cou = 0
        pre_cou = Counter() # defaultdict(int) would be faster : 767ms Beats62.51%
        for n in nums :
            sub_cou[n] -= 1
            mul2 = n*2
            ans_cou = (ans_cou + pre_cou[mul2] * sub_cou[mul2]) % MOD
            pre_cou[n] += 1
        return ans_cou

s = Solution()
print("ans :",s.specialTriplets([6,3,6])) # 1
print("ans :",s.specialTriplets([0,1,0,0])) # 1
print("ans :",s.specialTriplets([8,4,2,8,4])) # 2



