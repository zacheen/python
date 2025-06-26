# 2407. Longest Increasing Subsequence II
# https://leetcode.com/problems/longest-increasing-subsequence-ii

from typing import List
from math import inf

# my using SetTree template 2 : 4144ms Beats7.73%
class SegTree:
    def __init__(self, len_n):
        self.default_value = 0
        self.n = len_n
        self.tree = [self.default_value] * (4 * self.n)
        def build_rec(tree_idx, seg_st, seg_en):
            if seg_st == seg_en:
                # self.tree[tree_idx] = TODO nums[seg_st] 
                return
            mid = (seg_st + seg_en) >> 1
            tree_idx_l = tree_idx << 1
            tree_idx_r = tree_idx_l + 1
            build_rec(tree_idx_l, seg_st, mid)
            build_rec(tree_idx_r, mid + 1, seg_en)
            # self._update_node(tree_idx, tree_idx_l, tree_idx_r)
        build_rec(1, 0, self.n-1)

    def _merge_val(self, l, r):
        return max(l,r)
    
    def _update_node(self, tree_idx, tree_idx_l, tree_idx_r) :
        self.tree[tree_idx] = self._merge_val(self.tree[tree_idx_l], self.tree[tree_idx_r])

    def update(self, index, value):
        def update_rec(tree_idx, seg_st, seg_en):
            if seg_st == index and index == seg_en:  # Entire segment is target index
                self.tree[tree_idx] = value
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

    def query(self, q_left = None, q_right = None): # include both q_left, q_right
        if q_left == None : 
            q_left, q_right = 0, self.n-1
        def query_rec(tree_idx, seg_st, seg_en):
            if q_right < seg_st or seg_en < q_left :  # No overlap
                return 0
            elif q_left <= seg_st and seg_en <= q_right:  # Full overlap
                return self.tree[tree_idx]
            else:  # Partial overlap
                mid = (seg_st + seg_en) >> 1
                tree_idx_l = tree_idx << 1
                tree_idx_r = tree_idx_l + 1
                left_ret = query_rec(tree_idx_l, seg_st, mid)
                right_ret = query_rec(tree_idx_r, mid + 1, seg_en)
                return self._merge_val(left_ret, right_ret)
        return query_rec(1, 0, self.n-1)

class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        segtree = SegTree(max(nums)+2) # segtree.query(最小的可行值, 最大的可行值) = 最長的長度
        for n in nums :
            past_len = segtree.query(n-k, n-1)
            segtree.update(n, past_len+1)
        return segtree.query()

s = Solution()
print("ans :",s.lengthOfLIS(nums = [4,2,1,4,3,4,5,8,15], k = 3)) # [1,3,4,5,8]
print("ans :",s.lengthOfLIS(nums = [7,4,5,1,8,12,4,7], k = 5)) # [4,5,8,12]
print("ans :",s.lengthOfLIS(nums = [1,5], k = 1)) # [1] or [5]
