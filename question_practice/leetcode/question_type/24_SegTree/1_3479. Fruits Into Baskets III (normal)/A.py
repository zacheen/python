# 3479. Fruits Into Baskets III
# https://leetcode.com/problems/fruits-into-baskets-iii

from typing import List
from math import inf
from bisect import bisect_left, bisect_right

# my using template SegTree : 2759ms Beats43.80%
# 此segment tree 負責回傳 區間內最小的indx
class SegTree:
    def __init__(self, nums):
        self.n = len(nums)
        # init
        self.tree = [inf] * 2 * self.n
        for i,n in zip(range(self.n, 2 * self.n) , nums):
            self.tree[i] = n
        for i in range(self.n-1, 0, -1):
            # execute def
            self.tree[i] = min(self.tree[2*i], self.tree[2*i+1])     

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
        res = (inf, inf)
        while left <= right:
            if left & 1 :
                # combine result
                res = min(res, self.tree[left])
                left += 1
            if not (right & 1) :
                # combine result
                res = min(res, self.tree[right])
                right -= 1
            left >>= 1
            right>>= 1
        return res
    
# recursive version : 4525ms Beats23.97%
# class SegTree:
#     def __init__(self, nums):
#         self.default_value = (inf,inf)
#         self.n = len(nums)
#         self.tree = [self.default_value] * (4 * self.n)
#         def build_rec(tree_idx, seg_st, seg_en):
#             if seg_st == seg_en:
#                 self.tree[tree_idx] = nums[seg_st]
#                 return
#             mid = (seg_st + seg_en) >> 1
#             tree_idx_l = tree_idx << 1
#             tree_idx_r = tree_idx_l + 1
#             build_rec(tree_idx_l, seg_st, mid)
#             build_rec(tree_idx_r, mid + 1, seg_en)
#             self._update_node(tree_idx, tree_idx_l, tree_idx_r)
#         build_rec(1, 0, self.n-1)

#     def _update_node(self, tree_idx, tree_idx_l, tree_idx_r) :
#         self.tree[tree_idx] = min(self.tree[tree_idx_l], self.tree[tree_idx_r])

#     def update(self, index, value):
#         def update_rec(tree_idx, seg_st, seg_en):
#             if seg_st == index and index == seg_en:  # Entire segment is target index
#                 self.tree[tree_idx] = value
#             else: # Update nested segments that contain the target index
#                 mid = (seg_st + seg_en) >> 1
#                 tree_idx_l = tree_idx << 1
#                 tree_idx_r = tree_idx_l + 1
#                 if index <= mid:
#                     update_rec(tree_idx_l, seg_st, mid)
#                 else:
#                     update_rec(tree_idx_r, mid + 1, seg_en)
#                 self._update_node(tree_idx, tree_idx_l, tree_idx_r)
#         update_rec(1, 0, self.n - 1)

#     def query(self, q_left, q_right):
#         def query_rec(tree_idx, seg_st, seg_en):
#             if q_right < seg_st or seg_en < q_left :  # No overlap
#                 return self.default_value
#             elif q_left <= seg_st and seg_en <= q_right:  # Full overlap
#                 return self.tree[tree_idx]
#             else:  # Partial overlap
#                 mid = (seg_st + seg_en) >> 1
#                 tree_idx_l = tree_idx << 1
#                 tree_idx_r = tree_idx_l + 1
#                 left_sum = query_rec(tree_idx_l, seg_st, mid)
#                 right_sum = query_rec(tree_idx_r, mid + 1, seg_en)
#                 return min(left_sum , right_sum)
#         return query_rec(1, 0, self.n - 1)

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        sort_b = list((n,i) for i,n in enumerate(baskets))
        sort_b.sort()

        segtree = SegTree(list((b_i,i) for i, (b_amo, b_i) in enumerate(sort_b)))

        # 在可行的範圍內 找到最小的indx
        right_bound = len(baskets)-1 # include
        ans = 0
        for f_amo in fruits :
            left_bound = bisect_right(sort_b, (f_amo, -1))
            min_i, pos_i = segtree.query(left_bound, right_bound)
            if min_i == inf :
                ans += 1
            else :
                segtree.update(pos_i, (inf,inf))
        return ans

# # 雖然比較節省空間，但比較慢 : 3884ms Beats29.76%
# class Solution:
#     def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
#         len_bas = len(baskets)
#         sort_b_i = list(range(len_bas))
#         sort_b_i.sort(key = lambda x : (baskets[x], x))

#         segtree = SegTree(list((b_i,i) for i, b_i in enumerate(sort_b_i)))

#         # 在可行的範圍內 找到最小的indx
#         right_bound = len(baskets)-1 # include
#         ans = 0
#         for f_amo in fruits :
#             left_bound = bisect_left(range(len_bas), True, key = lambda x : baskets[sort_b_i[x]] >= f_amo)
#             min_i, pos_i = segtree.query(left_bound, right_bound)
#             if min_i == inf :
#                 ans += 1
#             else :
#                 segtree.update(pos_i, (inf,inf))
#         return ans

s = Solution()
print("ans :",s.numOfUnplacedFruits(fruits = [4,2,5], baskets = [3,5,4])) # 1
print("ans :",s.numOfUnplacedFruits(fruits = [3,6,1], baskets = [6,4,7])) # 0
# print("ans :",s.numOfUnplacedFruits()) # 



