# 2411. Smallest Subarrays With Maximum Bitwise OR
# https://leetcode.com/problems/smallest-subarrays-with-maximum-bitwise-or

from typing import List
from math import inf

# given ans (basis) : 107ms Beats99.21%
    # O(nlog2MAX_N) 
class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        for i, n in enumerate(nums):
            j = i-1
            while j >= 0 and (nums[j] | n) != nums[j]:
                res[j] = i - j + 1
                nums[j] |= n
                j -= 1
        return res

# my 496ms Beats85.04%
class SegTree:
    def __init__(self, nums):
        self.n = len(nums)
        # init
        self.tree = [0]*self.n + nums
        for i in range(self.n-1, 0, -1):
            # execute def
            self.tree[i] = self.tree[i<<1] | self.tree[(i<<1)+1]

    def query(self, left, right):
        # include
        left += self.n
        right += self.n
        res = 0
        while left <= right:
            if left & 1 :
                # combine result
                res |= self.tree[left]
                left += 1
            if not (right & 1) :
                # combine result
                res |= self.tree[right]
                right -= 1
            left >>= 1
            right>>= 1
        return res

class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        len_n = len(nums)
        max_or_l = [0]*len_n
        now_max_or_l = 0
        for i in range(len_n-1, -1, -1) :
            n = nums[i]
            now_max_or_l |= n
            max_or_l[i] = now_max_or_l
        # print(max_or_l)
        
        segtree = SegTree(nums)
        r = 0
        end_r = len_n-1
        ans = []
        for l, max_or in enumerate(max_or_l):
            while r < end_r and segtree.query(l,r) < max_or :
                r += 1
            ans.append(max(r-l+1, 1))
        return ans

s = Solution()
print("ans :",s.smallestSubarrays([1,0,2,1,3])) # [3, 3, 2, 2, 1]
print("ans :",s.smallestSubarrays([1,2])) # [2, 1]
print("ans :",s.smallestSubarrays([1,2,2,2,4])) # [2, 1]
# print("ans :",s.smallestSubarrays(list(range(128)))) # [2, 1]

# worst case (O(nlog2MAX_N))
s.smallestSubarrays([0]*100000+list((1<<i)-1 for i in range(1,30)))

# edge case
print("ans :",s.smallestSubarrays([1,0])) # [1, 1]



