# 307. Range Sum Query - Mutable
# https://leetcode.com/problems/range-sum-query-mutable/description

from typing import List
import functools

# my 387ms Beats94.97%
class NumArray:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * 2 * self.n
        for i,n in zip(range(self.n, 2 * self.n) , nums):
            self.tree[i] = n
        for i in range(self.n-1, 0, -1):
            self.tree[i] = self.tree[2*i] + self.tree[2*i+1]

    def update(self, index, val):
        index += self.n
        self.tree[index] = val
        while index > 1:
            # index如果是右 index^1就是對應左邊
            self.tree[index>>1] = self.tree[index] + self.tree[index^1]
            index >>= 1 # index //= 2

    def sumRange(self, left, right):
        left += self.n
        right += self.n
        res = 0
        # binary search
        while left <= right:
            if left & 1 :
                # if left odd:
                res += self.tree[left]
                left += 1
            if not (right & 1) :
                # if right even
                res += self.tree[right]
                right -= 1
            left >>= 1  # left //= 2
            right >>= 1 # right //= 2
        return res

# my template 2 - top down version (array) : 1089ms Beats18.18%
class SegTree_sum:
    def __init__(self, nums):
        self.default_value = 0
        self.n = len(nums)
        self.tree = [self.default_value] * (4 * self.n)
        def _build(tree_idx, seg_st, seg_en):
            if seg_st == seg_en:
                self.tree[tree_idx] = nums[seg_st]
                return
            mid = (seg_st + seg_en) >> 1
            tree_idx_l = tree_idx << 1
            tree_idx_r = tree_idx_l + 1
            _build(tree_idx_l, seg_st, mid)
            _build(tree_idx_r, mid + 1, seg_en)
            self.tree[tree_idx] = self.tree[tree_idx_l] + self.tree[tree_idx_r]
        _build(1, 0, self.n-1)

    def update(self, index, value):
        def _update(tree_idx, seg_st, seg_en):
            if seg_st == index and index == seg_en:  # Entire segment is target index
                self.tree[tree_idx] = value
            else: # Update nested segments that contain the target index
                mid = (seg_st + seg_en) >> 1
                tree_idx_l = tree_idx << 1
                tree_idx_r = tree_idx_l + 1
                if index <= mid:
                    _update(tree_idx_l, seg_st, mid)
                else:
                    _update(tree_idx_r, mid + 1, seg_en)
                self.tree[tree_idx] = self.tree[tree_idx_l] + self.tree[tree_idx_r]
        _update(1, 0, self.n - 1)

    def query(self, q_left, q_right):
        def _query(tree_idx, seg_st, seg_en):
            if q_right < seg_st or seg_en < q_left :  # No overlap
                return self.default_value
            elif q_left <= seg_st and seg_en <= q_right:  # Full overlap
                return self.tree[tree_idx]
            else:  # Partial overlap
                mid = (seg_st + seg_en) >> 1
                tree_idx_l = tree_idx << 1
                tree_idx_r = tree_idx_l + 1
                left_sum = _query(tree_idx_l, seg_st, mid)
                right_sum = _query(tree_idx_r, mid + 1, seg_en)
                return left_sum + right_sum
        return _query(1, 0, self.n - 1)

# my template 3 - top down version (node) : 1135ms Beats14.95%
class SegTree_sum:
    def __init__(self, nums):
        self.default_value = 0
        self.n = len(nums)
        class Node(object):
            def __init__(self, start, end, val = self.default_value):
                self.start = start
                self.end = end
                self.value = val
                self.left = None
                self.right = None

        def _build(seg_st, seg_en):
            if seg_st == seg_en:
                return Node(seg_st, seg_en, nums[seg_st])
            mid = (seg_st + seg_en) >> 1
            root = Node(seg_st, seg_en)
            root.left = _build(seg_st, mid)
            root.right = _build(mid + 1, seg_en)
            root.value = root.left.value + root.right.value
            return root
        self.root = _build(0, self.n-1)

    def update(self, index, value):
        def _update(root, seg_st, seg_en):
            if seg_st == seg_en:  # Entire segment is target index
                root.value = value
            else: # Update nested segments that contain the target index
                mid = (seg_st + seg_en) >> 1
                if index <= mid:
                    _update(root.left, seg_st, mid)
                else:
                    _update(root.right, mid + 1, seg_en)
                root.value = root.left.value + root.right.value
        _update(self.root, 0, self.n - 1)

    def query(self, q_left, q_right):
        def _query(root, seg_st, seg_en):
            if q_right < seg_st or seg_en < q_left :  # No overlap
                return self.default_value
            if q_left <= seg_st and seg_en <= q_right:  # Full overlap
                return root.value
            else:  # Partial overlap
                mid = (seg_st + seg_en) >> 1
                left_sum = _query(root.left, seg_st, mid)
                right_sum = _query(root.right, mid + 1, seg_en)
                return left_sum + right_sum
        return _query(self.root, 0, self.n - 1)

class NumArray:
    # O(n) time | O(n) space
    def __init__(self, nums: List[int]):
        self.segtree = SegTree_sum(nums)
    
    # O(logn) time | O(logn) space
    def update(self, index: int, val: int) -> None:
        self.segtree.update(index, val)
    
    # O(logn) time | O(logn) space
    def sumRange(self, left: int, right: int) -> int:
        return self.segtree.query(left, right)