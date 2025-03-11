# 3471. Find the Largest Almost Missing Integer
# https://leetcode.com/problems/find-the-largest-almost-missing-integer/description/

from typing import List
from math import inf
from collections import Counter

# my 
class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        cou = Counter()
        for st in range(len(nums)-k+1):
            # print(nums[st:st+k])
            cou += Counter(set(nums[st:st+k]))
        poss_n = [n for n,c in cou.items() if c == 1]
        return -1 if len(poss_n) == 0 else max(poss_n)

# my optimize ver : 2ms Beats82.30%
class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        if len(nums) == k :
            return max(nums)
        if k == 1 :
            cou = Counter(nums)
            poss_n = [n for n,c in cou.items() if c == 1]
            return -1 if len(poss_n) == 0 else max(poss_n)

        poss_1 = nums[0]
        poss_2 = nums[-1]
        if poss_1 == poss_2 :
            return -1
        else :
            if poss_1 < poss_2 :
                poss_1, poss_2 = poss_2, poss_1
            cou = Counter(nums)
            if cou[poss_1] == 1 :
                return poss_1
            elif cou[poss_2] == 1 :
                return poss_2
            else :
                return -1


s = Solution()
print("ans :",s.largestInteger(nums = [3,9,2,1,7], k = 3)) # 7
print("ans :",s.largestInteger(nums = [3,9,7,2,1,7], k = 4)) # 3 
print("ans :",s.largestInteger(nums = [0,0], k = 1)) # -1
print("ans :",s.largestInteger(nums = [0,0], k = 2)) # 0



