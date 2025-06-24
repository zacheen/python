# 3161. Block Placement Queries
# https://leetcode.com/problems/block-placement-queries

from typing import List
from math import inf

# my modify SegTree template 2 : 6169ms Beats9.06%
class SegTree:
    def __init__(self, len_n):
        self.default_value = [None,None,0]
        self.n = len_n
        self.tree = [self.default_value] * (4 * self.n)
        # def build_rec(tree_idx, seg_st, seg_en):
        #     if seg_st == seg_en:
        #         # self.tree[tree_idx] = [None,None,0]
        #         return
        #     mid = (seg_st + seg_en) >> 1
        #     tree_idx_l = tree_idx << 1
        #     tree_idx_r = tree_idx_l + 1
        #     build_rec(tree_idx_l, seg_st, mid)
        #     build_rec(tree_idx_r, mid + 1, seg_en)
        #     self._update_node(tree_idx, tree_idx_l, tree_idx_r)
        # build_rec(1, 0, self.n-1)

    def _update_node(self, tree_idx, tree_idx_l, tree_idx_r) :
        l_l, l_r, l_max = self.tree[tree_idx_l]
        r_l, r_r, r_max = self.tree[tree_idx_r]
        new_max = max(l_max, r_max)
        if l_r and r_l :
            new_max = max(new_max, r_l - l_r)
        self.tree[tree_idx] = [
            l_l if l_l else r_l,
            r_r if r_r else l_r,
            new_max
        ]

    def update(self, index):
        def update_rec(tree_idx, seg_st, seg_en):
            if seg_st == index and index == seg_en:  # Entire segment is target index
                self.tree[tree_idx] = [seg_st,seg_st,0]
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

    def query(self, q_right): # include both q_left, q_right
        q_left = 0
        def query_rec(tree_idx, seg_st, seg_en):
            if q_right < seg_st :  # No overlap
                return [q_right,q_right,0]
            if seg_en < q_left :  # No overlap
                return [q_left,q_left,0]
            elif q_left <= seg_st and seg_en <= q_right:  # Full overlap
                return self.tree[tree_idx]
            else:  # Partial overlap
                mid = (seg_st + seg_en) >> 1
                tree_idx_l = tree_idx << 1
                tree_idx_r = tree_idx_l + 1
                l_l, l_r, l_max = query_rec(tree_idx_l, seg_st, mid)
                r_l, r_r, r_max = query_rec(tree_idx_r, mid + 1, seg_en)
                new_max = max(l_max, r_max)
                if l_r and r_l :
                    new_max = max(new_max, r_l - l_r)
                ret = [
                    l_l if l_l else r_l,
                    r_r if r_r else l_r,
                    new_max
                ]
                return ret
        return query_rec(1, 0, self.n-1)

class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        len_n = max(q[1] for q in queries)+1
        segtree = SegTree(len_n)
        ans = []
        for q in queries :
            if q[0] == 1 :
                segtree.update(q[1])
            else :
                if q[2] > q[1] :
                    ans.append(False)
                    continue
                ret = segtree.query(q[1])
                if ret[0] == None :
                    max_len = q[1]
                else :
                    max_len = max(ret[0], q[1]-ret[1], ret[2])
                ans.append(max_len >= q[2])
        return ans

# my, inspire by given ans : 3555ms Beats31.23%
class SegTree_Max:
    def __init__(self, len_n):
        self.n = len_n
        # init
        self.tree = [0] * 2 * self.n

    def update(self, index, val):
        index += self.n
        self.tree[index] = val
        while index > 1:
            # update node
            self.tree[index>>1] = max(self.tree[index], self.tree[index^1])
            index >>= 1

    def query(self, left, right):
        left += self.n
        right += self.n
        res = 0
        while left <= right:
            if left & 1 :
                # combine result
                res = max(res, self.tree[left])
                left += 1
            if not (right & 1) :
                # combine result
                res = max(res, self.tree[right])
                right -= 1
            left >>= 1
            right>>= 1
        return res

from sortedcontainers import SortedList
class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        len_n = max(q[1] for q in queries)+1
        segtree = SegTree_Max(len_n)
        mem_len = SortedList()
        segtree.update(0, inf)
        mem_len.add(0)
        ans = []
        for q in queries :
            if q[0] == 1 :
                ret_i = mem_len.bisect_right(q[1])-1
                left_bound = mem_len[ret_i]
                segtree.update(left_bound, q[1]-left_bound)
                if ret_i+1 < len(mem_len) :
                    right_bound = mem_len[ret_i+1]
                    segtree.update(q[1], right_bound-q[1])
                else :
                    segtree.update(q[1], inf)
                mem_len.add(q[1])
            else :
                if q[2] > q[1] :
                    ans.append(False)
                    continue
                ret_i = mem_len.bisect_right(q[1])-1
                left_bound = mem_len[ret_i]
                max_len = segtree.query(0,left_bound-1)
                max_len = max(max_len, q[1]-left_bound)
                ans.append(max_len >= q[2])
        return ans

s = Solution()
print("ans :",s.getResults([[1,2],[2,3,3],[2,3,1],[2,2,2]])) # FTT
print("ans :",s.getResults([[1,7],[2,7,6],[1,2],[2,7,5],[2,7,6]])) # TTF
print("ans :",s.getResults([[2,1,2]])) # F 超出範圍 0
print("ans :",s.getResults([[1,4],[2,1,2]])) # F 超出範圍 0
print("ans :",s.getResults([[1,3],[2,4,2]])) # T 
print("ans :",s.getResults([[1,2],[2,7,6]])) # F
print("ans :",s.getResults([[2,11,5],[1,2],[2,7,6]])) # TF
print("ans :",s.getResults([[1,2],[2,7,6]])) # F



