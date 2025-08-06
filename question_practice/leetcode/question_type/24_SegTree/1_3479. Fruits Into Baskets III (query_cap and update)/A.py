# 3479. Fruits Into Baskets III
# https://leetcode.com/problems/fruits-into-baskets-iii

from typing import List
from math import inf
from bisect import bisect_left, bisect_right

# my using template segment tree : 1958ms Beats78.52%
    # SegTree trace each capacities minimum indx, query(fruit, max_val) > update(val, next_pos)
class SegTree:
    def __init__(self, nums):
        self.n = len(nums)
        # init
        self.tree = [inf] * 2 * self.n
        for i,n in zip(range(self.n, 2 * self.n) , nums):
            self.tree[i] = n
        for i in range(self.n-1, 0, -1):
            # execute def
            self.tree[i] = min(self.tree[i<<1], self.tree[(i<<1)+1])  

    def update(self, index, val):
        index += self.n
        self.tree[index] = val
        while index > 1:
            # update node
            self.tree[index>>1] = min(self.tree[index], self.tree[index^1])
            index >>= 1

    def query(self, left, right):
        # include
        left += self.n
        right += self.n
        min_res = inf
        while left <= right:
            if left & 1 :
                # combine result
                min_res = min(min_res, self.tree[left])
                left += 1
            if not (right & 1) :
                # combine result
                min_res = min(min_res, self.tree[right])
                right -= 1
            left >>= 1
            right>>= 1
        return min_res

from collections import defaultdict , deque
from bisect import bisect_left
class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        cap2i = defaultdict(deque)
        for i, cap in enumerate(baskets):
            cap2i[cap].append(i)
        
        discrete = list(cap2i.keys())
        discrete.sort()

        init_segtree = []
        for cap in discrete :
            cap_l = cap2i[cap]
            init_segtree.append(cap_l.popleft())

        seg = SegTree(init_segtree)
        ans = 0
        for f in fruits :
            seg_l = bisect_left(discrete, f)
            if seg_l == len(discrete) :
                ans += 1
                continue
            ret = seg.query(seg_l, seg.n-1)
            if ret == inf :
                ans += 1
            else :
                fit_cap = baskets[ret]
                li = cap2i[fit_cap]
                disc_i = bisect_left(discrete, fit_cap)
                if li :
                    seg.update(disc_i, li.popleft())
                else :
                    seg.update(disc_i, inf)
        return ans

s = Solution()
print("ans :",s.numOfUnplacedFruits(fruits = [4,2,5], baskets = [3,5,4])) # 1
print("ans :",s.numOfUnplacedFruits(fruits = [3,6,1], baskets = [6,4,7])) # 0
# print("ans :",s.numOfUnplacedFruits()) # 



