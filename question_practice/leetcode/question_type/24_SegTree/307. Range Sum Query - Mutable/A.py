# 307. Range Sum Query - Mutable
# https://leetcode.com/problems/range-sum-query-mutable/description

from typing import List
import functools

# my 387ms Beats94.97%
class NumArray:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * 2 * self.n
        for i,n in zip(range(self.n, 2 * self.n) , nums):
            self.tree[i] = n
        for i in range(self.n-1, 0, -1):
            self.tree[i] = self.tree[2*i] + self.tree[2*i+1]

    def update(self, index, val):
        index += self.n
        self.tree[index] = val
        while index > 1:
            # index如果是右 index^1就是對應左邊
            self.tree[index>>1] = self.tree[index] + self.tree[index^1]
            index >>= 1 # index //= 2

    def sumRange(self, left, right):
        left += self.n
        right += self.n
        res = 0
        # binary search
        while left <= right:
            if left & 1 :
                # if left odd:
                res += self.tree[left]
                left += 1
            if not (right & 1) :
                # if right even
                res += self.tree[right]
                right -= 1
            left >>= 1  # left //= 2
            right >>= 1 # right //= 2
        return res

