# 3479. Fruits Into Baskets III
# https://leetcode.com/problems/fruits-into-baskets-iii

from typing import List
from math import inf
from bisect import bisect_left, bisect_right

# query 的同時，recursive backward 時更新 segment tree
    # 其實這個比較像二分法，每次都會走到最底 (只是 segment tree 提供了資訊要往左或右)
# my using SegTree template 2: 2407ms Beats55.08%
class SegTree:
    def __init__(self, nums):
        self.default_value = -1
        self.n = len(nums)
        self.tree = [self.default_value] * (4 * self.n)
        def build_rec(tree_idx, seg_st, seg_en):
            if seg_st == seg_en:
                self.tree[tree_idx] = nums[seg_st]
                return
            mid = (seg_st + seg_en) >> 1
            tree_idx_l = tree_idx << 1
            tree_idx_r = tree_idx_l + 1
            build_rec(tree_idx_l, seg_st, mid)
            build_rec(tree_idx_r, mid + 1, seg_en)
            self._update_node(tree_idx, tree_idx_l, tree_idx_r)
        build_rec(1, 0, self.n-1)

    def _update_node(self, tree_idx, tree_idx_l, tree_idx_r) :
        self.tree[tree_idx] = max(self.tree[tree_idx_l], self.tree[tree_idx_r])

    def query(self, q_left, q_right, limit = None): # include both q_left, q_right
        def query_rec(tree_idx, seg_st, seg_en):
            if self.tree[tree_idx] < limit :
                return -1
            if seg_st == seg_en :
                self.tree[tree_idx] = -1
                return seg_st
            mid = (seg_st + seg_en) >> 1
            tree_idx_l = tree_idx << 1
            tree_idx_r = tree_idx_l + 1
            left_ret = query_rec(tree_idx_l, seg_st, mid)
            if left_ret != -1 :
                self._update_node(tree_idx, tree_idx_l, tree_idx_r)
                return left_ret
            right_ret = query_rec(tree_idx_r, mid + 1, seg_en)
            self._update_node(tree_idx, tree_idx_l, tree_idx_r)
            return right_ret
        return query_rec(1, 0, self.n-1)

# my using SegTree template 3: 2855ms Beats37.29%
class SegTree:
    def __init__(self, nums):
        self.default_value = 0 # 預設是沒有空間的
        self.n = len(nums)
        class Node(object):
            def __init__(self, start, end, val = self.default_value):
                # self.start = start
                # self.end = end
                self.value = val
                self.left = None
                self.right = None

        def build_(seg_st, seg_en):
            if seg_st == seg_en:
                return Node(seg_st, seg_en, nums[seg_st])
            mid = (seg_st + seg_en) >> 1
            root = Node(seg_st, seg_en)
            root.left = build_(seg_st, mid)
            root.right = build_(mid + 1, seg_en)
            self._update_node(root)
            return root
        self.root = build_(0, self.n-1)

    def _update_node(self, root) :
        root.value = max(root.left.value, root.right.value)

    def query(self, q_left, q_right, limit):
        def query_(root, seg_st, seg_en):
            if root.value >= limit :
                if seg_st == seg_en :
                    root.value = -1 # 已經取出 更新數值
                    return seg_st
                mid = (seg_st + seg_en) >> 1
                left_ret = query_(root.left, seg_st, mid)
                if left_ret >= 0 :
                    self._update_node(root) # 因為底下有更新，所以這裡同時更新
                    return left_ret
                else :
                    right_ret = query_(root.right, mid + 1, seg_en)
                    self._update_node(root)
                    return right_ret
            else :
                return -1
        return query_(self.root, 0, self.n - 1)

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        segtree = SegTree(baskets)

        # 在可行的範圍內 找到最小的indx
        left_bound = 0
        right_bound = len(baskets)-1 # include
        ans = 0
        for f_amo in fruits :
            ret = segtree.query(left_bound, right_bound, f_amo)
            if ret == -1 :
                ans += 1
            else :
                # print(f_amo, ret)
                pass
        return ans

s = Solution()
print("ans :",s.numOfUnplacedFruits(fruits = [4,2,5], baskets = [3,5,4])) # 1
print("ans :",s.numOfUnplacedFruits(fruits = [3,6,1], baskets = [6,4,7])) # 0
# print("ans :",s.numOfUnplacedFruits()) # 



