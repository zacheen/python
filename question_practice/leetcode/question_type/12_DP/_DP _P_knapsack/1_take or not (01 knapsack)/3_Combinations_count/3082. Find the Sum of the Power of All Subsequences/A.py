# 3082. Find the Sum of the Power of All Subsequences
# https://leetcode.com/problems/find-the-sum-of-the-power-of-all-subsequences

from typing import List
from math import inf
from collections import defaultdict, Counter
from copy import deepcopy
MOD = 10**9+7

# my using template knapsack_01_comb v2 : 1152ms Beats16.48%
class Solution:
    def sumOfPower(self, nums: List[int], k: int) -> int:
        mem = defaultdict(Counter)
        mem[0][0] = 1
        for num in nums:
            for s, cnts in deepcopy(mem).items() :
                if (new_s := s+num) <= k :
                    for cnt, amount in cnts.copy().items() :
                        mem[new_s][cnt+1] += amount
        # print(mem)
        ans = 0
        for cnt, amount in mem[k].items() : # cnt 是由幾個組成，amount是有幾種組合
            # print(amount, len(nums)-cnt, amount * 2<<(len(nums)-cnt-1))
            ans += amount * 1<<(len(nums)-cnt)
        return ans % MOD
    
# 這題不能用 complete knapsack 去做
    # 因為 [2,3,3] 這個testcase 會變成 3取一個 以及 3取兩個
    # 但 3取一個 其實應該要算兩種，所以會少算

s = Solution()
# print("ans :",s.sumOfPower(nums = [1,2,3], k = 3)) # 6
# print("ans :",s.sumOfPower(nums = [2,3,3], k = 5)) # 4
# print("ans :",s.sumOfPower(nums = [1,2,3], k = 7)) # 0
print("ans :",s.sumOfPower([2,4,4,2], 4)) # 
print("ans :",s.sumOfPower([1], 1)) # 1



