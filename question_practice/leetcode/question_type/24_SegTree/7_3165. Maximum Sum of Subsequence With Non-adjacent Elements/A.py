# 3165. Maximum Sum of Subsequence With Non-adjacent Elements
# https://leetcode.com/problems/maximum-sum-of-subsequence-with-non-adjacent-elements

from typing import List
from math import inf

# # my 4160ms Beats67.50%
class SegTree:
    def __init__(self, nums):
        self.default_value = None
        self.n = len(nums)
        self.tree = [self.default_value] * (4 * self.n)
        def build_rec(tree_idx, seg_st, seg_en):
            if seg_st == seg_en:
                self.tree[tree_idx] = (0, -inf, -inf, nums[seg_st]) # 兩邊都沒取, 取左, 取右, 兩邊都取
                return
            mid = (seg_st + seg_en) >> 1
            tree_idx_l = tree_idx << 1
            tree_idx_r = tree_idx_l + 1
            build_rec(tree_idx_l, seg_st, mid)
            build_rec(tree_idx_r, mid + 1, seg_en)
            self._update_node(tree_idx, tree_idx_l, tree_idx_r)
        build_rec(1, 0, self.n-1)

    def _merge_val(self,l,r):
        xx1, ox1, xo1, oo1 = l
        xx2, ox2, xo2, oo2 = r
        return ( # 後來結果左邊 (中間 xo,ox,xx 的搭配) 後來結果右邊
            max(xx1+ox2, xo1+xx2, xx1+xx2),
            max(ox1+ox2, oo1+xx2, ox1+xx2),
            max(xx1+oo2, xo1+xo2, xx1+xo2),
            max(ox1+oo2, oo1+xo2, ox1+xo2),
        )
    
    def _update_node(self, tree_idx, tree_idx_l, tree_idx_r) :
        self.tree[tree_idx] = self._merge_val(self.tree[tree_idx_l], self.tree[tree_idx_r])

    def update(self, index, value):
        def update_rec(tree_idx, seg_st, seg_en):
            if seg_st == index and index == seg_en:  # Entire segment is target index
                self.tree[tree_idx] = (0, -inf, -inf, value)
            else: # Update nested segments that contain the target index
                mid = (seg_st + seg_en) >> 1
                tree_idx_l = tree_idx << 1
                tree_idx_r = tree_idx_l + 1
                if index <= mid:
                    update_rec(tree_idx_l, seg_st, mid)
                else:
                    update_rec(tree_idx_r, mid + 1, seg_en)
                self._update_node(tree_idx, tree_idx_l, tree_idx_r)
        update_rec(1, 0, self.n - 1)

    def query(self): # include both q_left, q_right
        q_left, q_right = 0, self.n-1
        def query_rec(tree_idx, seg_st, seg_en):
            # if q_right < seg_st or seg_en < q_left :  # No overlap
            #     return self.default_value
            if q_left <= seg_st and seg_en <= q_right:  # Full overlap
                return self.tree[tree_idx]
            else:  # Partial overlap
                mid = (seg_st + seg_en) >> 1
                tree_idx_l = tree_idx << 1
                tree_idx_r = tree_idx_l + 1
                left_ret = query_rec(tree_idx_l, seg_st, mid)
                right_ret = query_rec(tree_idx_r, mid + 1, seg_en)
                return self._merge_val(left_ret, right_ret)
        return query_rec(1, 0, self.n-1)

# # still slower
# class SegTree:
#     def __init__(self, nums):
#         self.default_value = None
#         self.n = len(nums)
#         class Node(object):
#             def __init__(self, seg_st, seg_en, val = self.default_value):
#                 self.value = val
#                 self.seg_st = seg_st
#                 self.seg_en = seg_en
#                 # self.left = None
#                 # self.right = None

#         def build_(seg_st, seg_en):
#             if seg_st == seg_en:
#                 return Node(seg_st, seg_en, [0, -inf, -inf, nums[seg_st]])
#             mid = (seg_st + seg_en) >> 1
#             root = Node(seg_st, seg_en)
#             root.left = build_(seg_st, mid)
#             root.right = build_(mid + 1, seg_en)
#             self._update_node(root)
#             return root
#         self.root = build_(0, self.n-1)

#     def _merge_val(self, l, r):
#         xx1, ox1, xo1, oo1 = l
#         xx2, ox2, xo2, oo2 = r
#         return ( # 後來結果左邊 (中間 xo,ox,xx 的搭配) 後來結果右邊
#             max(xx1+ox2, xo1+xx2, xx1+xx2),
#             max(ox1+ox2, oo1+xx2, ox1+xx2),
#             max(xx1+oo2, xo1+xo2, xx1+xo2),
#             max(ox1+oo2, oo1+xo2, ox1+xo2),
#         )
    
#     def _update_node(self, root) :
#         root.value = self._merge_val(root.left.value, root.right.value)

#     def update(self, index, value):
#         def update_(root):
#             if root.seg_st == root.seg_en:  # Entire segment is target index
#                 root.value = [0, -inf, -inf, value]
#             else: # Update nested segments that contain the target index
#                 mid = (root.seg_st + root.seg_en) >> 1
#                 if index <= mid:
#                     update_(root.left)
#                 else:
#                     update_(root.right)
#                 self._update_node(root)
#         update_(self.root)

#     def query(self):
#         q_left, q_right = 0, self.n-1
#         def query_(root):
#             if root.seg_en < q_left or q_right < root.seg_st : # No overlap
#                 return self.default_value
#             if q_left <= root.seg_st and root.seg_en <= q_right:  # Full overlap
#                 return root.value
#             else:  # Partial overlap
#                 mid = (root.seg_st + root.seg_en) >> 1
#                 left_ret = query_(root.left)
#                 right_ret = query_(root.right)
#                 return self._merge_val(left_ret + right_ret)
#         return query_(self.root)

MOD = 10**9+7
class Solution:
    def maximumSumSubsequence(self, nums: List[int], queries: List[List[int]]) -> int:
        segtree = SegTree(nums)
        ans = 0
        for i, v in queries :
            segtree.update(i,v)
            ans += max(segtree.query())
        return ans % MOD
        # # (slower)
        #     ans = (ans + max(segtree.query())) % MOD
        # return ans

s = Solution()
print("ans :",s.maximumSumSubsequence(nums = [3,5,9], queries = [[1,-2],[0,-3]])) # 
print("ans :",s.maximumSumSubsequence(nums = [0,-1], queries = [[0,-5]])) # 
# print("ans :",s.maximumSumSubsequence()) # 



