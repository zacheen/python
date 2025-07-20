# 3624. Number of Integers With Popcount-Depth Equal to K II
# https://leetcode.com/problems/number-of-integers-with-popcount-depth-equal-to-k-ii/

from typing import List
from math import inf
from collections import Counter

# my 
class SegTree:
    def __init__(self, nums):
        self.n = len(nums)
        # init
        self.tree = [None] * 2 * self.n
        for i,n in zip(range(self.n, 2 * self.n) , nums):
            self.tree[i] = Counter([n])
        for i in range(self.n-1, 0, -1):
            # execute def
            self.tree[i] = self.tree[i<<1] + self.tree[(i<<1)+1]

    def update(self, index, val):
        index += self.n
        self.tree[index] = Counter([val])
        while index > 1:
            # update node
            self.tree[index>>1] = self.tree[index] + self.tree[index^1]
            index >>= 1

    def query(self, left, right):
        # include
        left += self.n
        right += self.n
        res = Counter()
        while left <= right:
            if left & 1 :
                # combine result
                res += self.tree[left]
                left += 1
            if not (right & 1) :
                # combine result
                res += self.tree[right]
                right -= 1
            left >>= 1
            right>>= 1
        return res

class Solution:
    def popcountDepth(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        def popcount(n):
            ret = 0
            while n > 1 :
                n = n.bit_count()
                ret += 1
                if ret > 5 :
                    return -1
            return ret

        nums = list(popcount(n) for n in nums)
        segtree = SegTree(nums)

        ans = []
        for q in queries :
            if len(q) == 4 :
                _, l, r, k = q
                ans.append(segtree.query(l, r)[k])
            else :
                _, idx, val = q
                segtree.update(idx, popcount(val))
        return ans

s = Solution()
print("ans :",s.popcountDepth(nums = [2,4], queries = [[1,0,1,1],[2,1,1],[1,0,1,0]])) # [2, 1]
print("ans :",s.popcountDepth(nums = [3,5,6], queries = [[1,0,2,2],[2,1,4],[1,1,2,1],[1,0,1,0]])) # [3, 1, 0]
print("ans :",s.popcountDepth(nums = [1,2], queries = [[1,0,1,1],[2,0,3],[1,0,0,1],[1,0,0,2]])) #  [1, 0, 1]

