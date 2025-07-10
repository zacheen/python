# 3605. Minimum Stability Factor of Array
# https://leetcode.com/problems/minimum-stability-factor-of-array/description/

from typing import List
from math import inf, gcd
from functools import cache

# my 692ms Beats93.20%
class SegTree:
    def __init__(self, nums):
        self.n = len(nums)
        # init
        self.tree = [0] * 2 * self.n
        for i,n in zip(range(self.n, 2 * self.n) , nums):
            self.tree[i] = n
        for i in range(self.n-1, 0, -1):
            # execute def
            self.tree[i] = gcd(self.tree[i<<1], self.tree[(i<<1)+1])

    def query(self, left, right):
        # include
        left += self.n
        right += self.n
        res = None
        while left <= right:
            if left & 1 :
                # combine result
                res = gcd(res,self.tree[left]) if res != None else self.tree[left]
                left += 1
            if not (right & 1) :
                # combine result
                res = gcd(res,self.tree[right]) if res != None else self.tree[right]
                right -= 1
            left >>= 1
            right>>= 1
        return res
class Solution:
    def minStable(self, nums: List[int], maxC: int) -> int:
        if maxC >= (len(nums)-sum(n == 1 for n in nums)) : return 0
        
        segtree = SegTree(nums)
        @cache
        def check(limit_len): # limit_len is available
            if limit_len == 1 : return True
            now_i = 0
            end_i = len(nums)-limit_len
            rem_ch = maxC
            while now_i <= end_i :
                if segtree.query(now_i, now_i+limit_len-1) >= 2 :
                    rem_ch -= 1
                    if rem_ch < 0 :
                        return True
                    now_i += limit_len
                    continue
                now_i += 1
            return False
        
        left, right = 1, len(nums)//(maxC+1) # right 通常會超出界線(因為執行的時候不會執行到這個數字) # 但是最後 l 有可能會超出範圍
        while left < right:
            mid = (left + right) >> 1
            if check(mid) : # 條件 (如果 == target 的情況 要是 False)
                # 沒通過 或 數字應該要往大的方向跑(目標沒有在 left 跟 mid 之間)
                left = mid + 1 # 需注意 left 不會停留在 mid !
            else:
                # 通過(包含 == target 的情況)
                right = mid 

        # # 如果要找的是上界 (=找到第一個超出的位置 -1)
        if check(left) : return left
        else : return left-1

s = Solution()
print("ans :",s.minStable(nums = [3,5,10], maxC = 1)) # 1
print("ans :",s.minStable(nums = [2,6,8], maxC = 2)) # 1
print("ans :",s.minStable(nums = [2,4,9,6], maxC = 1)) # 2
print("ans :",s.minStable(nums = [2,4,9,6], maxC = 0)) # 2
print("ans :",s.minStable(nums = [4,5,4], maxC = 0)) # 1
print("ans :",s.minStable(nums = [6,5], maxC = 2)) # 1



