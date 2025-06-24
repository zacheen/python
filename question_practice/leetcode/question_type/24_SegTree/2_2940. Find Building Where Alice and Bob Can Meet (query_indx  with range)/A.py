# 2940. Find Building Where Alice and Bob Can Meet
# https://leetcode.com/problems/find-building-where-alice-and-bob-can-meet/description

from typing import List
import functools

# my using SegTree template 2 : 1123ms Beats11.96%
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

    def query(self, q_left, limit = None): # include both q_left
        def query_rec(tree_idx, seg_st, seg_en):
            if seg_en < q_left : # seg_st ~ seg_en 不包含限制的範圍
                return -1
            if self.tree[tree_idx] <= limit : # 此點以下的數值都不夠大
                return -1
            if seg_st == seg_en :
                return seg_st
            mid = (seg_st + seg_en) >> 1
            tree_idx_l = tree_idx << 1
            tree_idx_r = tree_idx_l + 1
            left_ret = query_rec(tree_idx_l, seg_st, mid)
            if left_ret != -1 :
                return left_ret
            right_ret = query_rec(tree_idx_r, mid + 1, seg_en)
            return right_ret
        return query_rec(1, 0, self.n-1)

class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        segtree = SegTree(heights)
        ans = []
        for q1, q2 in queries :
            if q1 == q2 :
                ans.append(q1)
                continue
            if q1 > q2 : # 讓 q1 永遠都在 q2 前面
                q1, q2 = q2, q1
            h1 = heights[q1]
            h2 = heights[q2]
            if h2 > h1 :
                ans.append(q2)
            else :
                ans.append(segtree.query(q2+1, h1))
        return ans

s = Solution()
# print("ans :",s.leftmostBuildingQueries(heights = [6,4,8,5,2,7], queries = [[0,1],[0,3],[2,4],[3,4],[2,2]])) # [2,5,-1,5,2] 
# print("ans :",s.leftmostBuildingQueries(heights = [5,3,8,2,6,1,4,6], queries = [[0,7],[3,5],[5,2],[3,0],[1,6]])) # [7,6,-1,4,6]
print("ans :",s.leftmostBuildingQueries(heights = [5,3,8,2,6,1,4,6], queries = [[2,5],[5,2],[3,0],[1,6]])) # [-1,-1,4,6]
# print("ans :",s.leftmostBuildingQueries(heights = [3,4,1,2], queries = [[0,0],[0,1],[0,2],[0,3],[1,0],[1,1],[1,2],[1,3],[2,0],[2,1],[2,2],[2,3],[3,0],[3,1],[3,2],[3,3]])) 
# print("ans :",s.leftmostBuildingQueries(heights = [3,4,1,2], queries = [[0,2]])) 



