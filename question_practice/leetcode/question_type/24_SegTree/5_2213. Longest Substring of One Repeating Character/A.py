# 2213. Longest Substring of One Repeating Character
# https://leetcode.com/problems/longest-substring-of-one-repeating-character

from typing import List
from math import inf

# my, modify SegTree template 2 : 5148ms Beats29.55%
class SegTree:
    def __init__(self, nums):
        self.default_value = None
        self.n = len(nums)
        self.tree = [self.default_value] * (4 * self.n)
        def build_rec(tree_idx, seg_st, seg_en):
            if seg_st == seg_en:
                self.tree[tree_idx] = (True, (nums[seg_st], 1), (nums[seg_st], 1), 1)
                return
            mid = (seg_st + seg_en) >> 1
            tree_idx_l = tree_idx << 1
            tree_idx_r = tree_idx_l + 1
            build_rec(tree_idx_l, seg_st, mid)
            build_rec(tree_idx_r, mid + 1, seg_en)
            self._update_node(tree_idx, tree_idx_l, tree_idx_r)
        build_rec(1, 0, self.n-1)

    def merge_res(self, l, r):
        l_con, l_l, l_r, l_max = l
        r_con, r_l, r_r, r_max = r

        new_con = l_con and r_con
        new_max = max(l_max, r_max)
        if (link := l_r[0] == r_l[0]) :
            new_max = max(new_max, l_r[1] + r_l[1]) 
        else :
            new_max = max(new_max, l_r[1], r_l[1])
            new_con = False
        
        return (
            new_con,
            (l_l[0], l_r[1] + r_l[1]) if l_con and link else l_l,
            (r_r[0], l_r[1] + r_l[1]) if r_con and link else r_r,
            new_max,
        )
    
    def _update_node(self, tree_idx, tree_idx_l, tree_idx_r) :
        self.tree[tree_idx] = self.merge_res(self.tree[tree_idx_l], self.tree[tree_idx_r])
    
    def update(self, index, value):
        def update_rec(tree_idx, seg_st, seg_en):
            if seg_st == index and index == seg_en:  # Entire segment is target index
                self.tree[tree_idx] = (True, (value, 1), (value, 1), 1)
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
        q_left = 0
        q_right = self.n-1
        def query_rec(tree_idx, seg_st, seg_en):
            if q_right < seg_st or seg_en < q_left :  # No overlap
                return (False, ("",0), ("",0), 0)
            elif q_left <= seg_st and seg_en <= q_right:  # Full overlap
                return self.tree[tree_idx]
            else:  # Partial overlap
                mid = (seg_st + seg_en) >> 1
                tree_idx_l = tree_idx << 1
                tree_idx_r = tree_idx_l + 1
                left_ret = query_rec(tree_idx_l, seg_st, mid)
                right_ret = query_rec(tree_idx_r, mid + 1, seg_en)
                return self.merge_res(left_ret, right_ret)
        return query_rec(1, 0, self.n-1)

# # my, modify SegTree template 3 : 5964ms Beats13.64%
class SegTree:
    def __init__(self, nums):
        self.default_value = None
        self.n = len(nums)
        class Node(object):
            def __init__(self, val = self.default_value):
                self.value = val
                # self.left = None
                # self.right = None

        def build_(seg_st, seg_en):
            if seg_st == seg_en:
                return Node((True, (nums[seg_st], 1), (nums[seg_st], 1), 1))
            mid = (seg_st + seg_en) >> 1
            root = Node()
            root.left = build_(seg_st, mid)
            root.right = build_(mid + 1, seg_en)
            self._update_node(root)
            return root
        self.root = build_(0, self.n-1)

    def merge_val(self, l, r):
        l_con, l_l, l_r, l_max = l
        r_con, r_l, r_r, r_max = r

        new_con = l_con and r_con
        new_max = max(l_max, r_max)
        if (link := l_r[0] == r_l[0]) :
            new_max = max(new_max, l_r[1] + r_l[1]) 
        else :
            new_max = max(new_max, l_r[1], r_l[1])
            new_con = False
        
        return (
            new_con,
            (l_l[0], l_r[1] + r_l[1]) if l_con and link else l_l,
            (r_r[0], l_r[1] + r_l[1]) if r_con and link else r_r,
            new_max,
        )

    def _update_node(self, root) :
        root.value = self.merge_val(root.left.value, root.right.value)

    def update(self, index, value):
        def update_(root, seg_st, seg_en):
            if seg_st == seg_en:  # Entire segment is target index
                root.value = (True, (value, 1), (value, 1), 1)
            else: # Update nested segments that contain the target index
                mid = (seg_st + seg_en) >> 1
                if index <= mid:
                    update_(root.left, seg_st, mid)
                else:
                    update_(root.right, mid + 1, seg_en)
                self._update_node(root)
        update_(self.root, 0, self.n - 1)

    def query(self):
        q_left, q_right = 0, self.n-1
        def query_(root, seg_st, seg_en):
            if seg_en < q_left or q_right < seg_st : # No overlap
                return self.default_value
            if q_left <= seg_st and seg_en <= q_right:  # Full overlap
                return root.value
            else:  # Partial overlap
                mid = (seg_st + seg_en) >> 1
                left_ret = query_(root.left, seg_st, mid)
                right_ret = query_(root.right, mid + 1, seg_en)
                return self.merge_val(left_ret + right_ret)
        return query_(self.root, 0, self.n-1)

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        segtree = SegTree(s)
        _ = segtree.query()
        _ = ""
        ans = []
        for q_c, q_i in zip(queryCharacters, queryIndices):
            segtree.update(q_i, q_c)
            ret = segtree.query()
            ans.append(max(ret[1][1], ret[2][1], ret[3]))
        return ans

# given ans


s = Solution()
print("ans :",s.longestRepeating(s = "babacc", queryCharacters = "bcb", queryIndices = [1,3,3])) # [3,3,4]
print("ans :",s.longestRepeating(s = "abyzz", queryCharacters = "aa", queryIndices = [2,1])) # [2,3]



