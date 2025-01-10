# 2779. Maximum Beauty of an Array After Applying Operation
# https://leetcode.com/problems/maximum-beauty-of-an-array-after-applying-operation/description

from typing import List
import functools

# my 323ms Beats 28.20%
from collections import Counter
class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        c = Counter(nums)
        c = [(n, cou) for n, cou in c.items()]
        c.sort()
        # print(c)
        now_t = 0
        max_t = 0
        k2 = 2*k
        left = 0
        for n, cou in c :
            now_t += cou
            # print(de[0][0], k2, n)
            while c[left][0] + k2 < n :
                now_t -= c[left][1]
                left += 1
            max_t = max(max_t, now_t)
        return max_t

# my opt 155ms Beats89.32%
    # O(n)
class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        max_n = max(nums)
        c = [0]*(max_n+1)
        for n in nums :
            c[n] += 1
        # print(c)
        now_t = 0
        max_t = 0
        k2P1 = 2*k+1
        for n, cou in zip(range(max_n+1), c) :
            l = n-k2P1
            if l >= 0 :
                now_t -= c[l]
            if cou > 0 :
                now_t += cou
                max_t = max(max_t, now_t)
        return max_t

# given ans
# 122ms Beats95.73%
    # I thought it would be slower because O(nlogn)...
class Solution:
    def maximumBeauty(self, nums: list[int], k: int) -> int:
        nums.sort()
        # l and r track the maximum window instead of the valid window.
        l = 0
        for r in range(len(nums)):
            if nums[r] - nums[l] > 2 * k:
                l += 1
        return r - l + 1

s = Solution()
# print("ans :",s.maximumBeauty(nums = [4,6,1,2], k = 2))
# print("ans :",s.maximumBeauty(nums = [1,1,1,1], k = 10))
print("ans :",s.maximumBeauty(nums = [1], k = 0))
# print("ans :",s.maximumBeauty())



