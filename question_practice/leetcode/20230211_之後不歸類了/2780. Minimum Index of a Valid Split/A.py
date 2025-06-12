# 2780. Minimum Index of a Valid Split
# https://leetcode.com/problems/minimum-index-of-a-valid-split

from typing import List
from math import inf
from collections import Counter

# my 68ms Beats53.47%
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        # 1. dominant 的數量一定要超過 nums 的一半
        cou = Counter(nums)
        dom_num, dom_cou = cou.most_common(1)[0]
        if dom_cou < len(nums)/2 :
            return -1
        
        len_n = len(nums)
        cou_f = 0
        for i, n in enumerate(nums) :
            if n == dom_num :
                cou_f += 1
                dom_cou -= 1
            if cou_f > (fn:=i+1)/2 and dom_cou > (len_n-fn)/2 :
                return i
        return -1

# given ans : 39ms Beats96.04%
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        # 1. dominant 的數量一定要超過 nums 的一半
        cou = Counter(nums)
        dom, cnt = cou.most_common(1)[0]
        left, cut = 0, 2*cnt - len(nums)
        if cut < 2: 
            return -1

        for i, num in enumerate(nums):
            left+= 2*(num == dom)
            if 1 < left - i <= cut: 
                return i

s = Solution()
print("ans :",s.minimumIndex([1,2,2,2])) # 2
print("ans :",s.minimumIndex([2,1,3,1,1,1,7,1,2,1])) # 4
print("ans :",s.minimumIndex([3,3,3,3,7,2,2])) # -1



