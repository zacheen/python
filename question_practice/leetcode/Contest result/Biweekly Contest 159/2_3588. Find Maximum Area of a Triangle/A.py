# 3588. Find Maximum Area of a Triangle
# https://leetcode.com/problems/find-maximum-area-of-a-triangle/description/

from typing import List
from math import inf
from collections import defaultdict

# my 295ms Beats97.36% 
class Solution:
    def maxArea(self, coords: List[List[int]]) -> int:
        def find_max_tri(coords) :
            same_n1 = defaultdict(list)
            for n1,n2 in coords :
                same_n1[n1].append(n2)
            max_ret = -1
            if len(same_n1.keys()) < 2 :
                return -1
            r_poss_n1 = max(same_n1.keys())
            l_poss_n1 = min(same_n1.keys())
            for n1, poss_n2_li in same_n1.items() :
                if len(poss_n2_li) >= 2 :
                    max_diff = max(poss_n2_li)-min(poss_n2_li)
                    max_otherside = max(r_poss_n1-n1, n1-l_poss_n1)
                    if (new_area := max_otherside*max_diff) > max_ret :
                        max_ret = new_area
            return max_ret
        ret1 = find_max_tri(coords)
        ret2 = find_max_tri((n2,n1) for n1,n2 in coords)
        return max(ret1, ret2)

MAX = ((10**4)*5)+1
fac = [[] for _ in range(MAX)]
for i in range(1, MAX):
    for j in range(i, MAX, i):
        fac[j].append(i)
fac[1].append(1)
fac[1].append(1)

class SegTree:
    def __init__(self, nums):
        self.n = len(nums)
        # init
        self.tree = [None] * 2 * self.n
        for i,n in zip(range(self.n, 2 * self.n) , nums):
            if n == 0 :
                self.tree[i] = (0, inf, 0) # [max, min, cnt] 
            else :
                self.tree[i] = (n, n, 1)
        for i in range(self.n-1, 0, -1):
            # execute def
            self.tree[i] = OP(self.tree[i<<1], self.tree[i<<1+1])

    def OP(val1, val2):
        return [
            max(val1[0], val2[0]),
            min(val1[1], val2[1]),
            val1[2]+val2[2]
        ]

    def query(self, left, right):
        # include
        left += self.n
        right += self.n
        res = (0, inf, 0)
        while left <= right:
            if left & 1 :
                # combine result
                res = OP(res, self.tree[left])
                left += 1
            if not (right & 1) :
                # combine result
                res = OP(res, self.tree[right])
                right -= 1
            left >>= 1
            right>>= 1
        return res

s = Solution()
print("ans :",s.maxArea([[1,1],[1,2],[3,2],[3,3]])) # 1
print("ans :",s.maxArea([[1,1],[2,2],[3,3]])) # -1
print("ans :",s.maxArea([[3,7],[7,1],[2,2],[2,1]])) # 



