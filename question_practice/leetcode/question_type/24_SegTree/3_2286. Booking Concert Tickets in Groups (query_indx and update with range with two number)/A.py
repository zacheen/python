# 2286. Booking Concert Tickets in Groups
# https://leetcode.com/problems/booking-concert-tickets-in-groups

from typing import List
from math import inf

# my, modify Segtree template 3: 773ms Beats88.00%
class SegTree:
    def __init__(self, n, m):
        self.default_value = 0
        self.n = n
        self.m = m
        class Node(object):
            def __init__(self, start, end, val = self.default_value):
                self.start = start
                self.end = end
                self.max_value = val
                self.sum = val
                self.left = None
                self.right = None

        def build_(seg_st, seg_en):
            if seg_st == seg_en:
                return Node(seg_st, seg_en, self.m)
            mid = (seg_st + seg_en) >> 1
            root = Node(seg_st, seg_en)
            root.left = build_(seg_st, mid)
            root.right = build_(mid + 1, seg_en)
            self._update_node(root)
            return root
        self.root = build_(0, self.n-1)

    def _update_node(self, root) :
        root.max_value = max(root.left.max_value, root.right.max_value)
        root.sum = root.left.sum + root.right.sum

    def update(self, index, value):
        def update_(root, seg_st, seg_en):
            if seg_st == seg_en:  # Entire segment is target index
                root.max_value = value
            else: # Update nested segments that contain the target index
                mid = (seg_st + seg_en) >> 1
                if index <= mid:
                    update_(root.left, seg_st, mid)
                else:
                    update_(root.right, mid + 1, seg_en)
                self._update_node(root)
        update_(self.root, 0, self.n - 1)

    def query_gather(self, q_right, limit):
        # print("query_gather", limit ,"seats, before row", q_right)
        def query_(root, seg_st, seg_en):
            if q_right < seg_st : # No overlap
                return -1
            if root.max_value < limit : # 此點以下的數值都不夠大
                return -1
            if seg_st == seg_en :
                ret = (seg_st, self.m - root.max_value)
                root.max_value -= limit
                root.sum -= limit
                # print("remain seats", root.max_value, seg_st)
                return ret
            mid = (seg_st + seg_en) >> 1
            left_ret = query_(root.left, seg_st, mid)
            if left_ret != -1 :
                self._update_node(root)
                return left_ret 
            right_ret = query_(root.right, mid + 1, seg_en)
            self._update_node(root)
            return right_ret
        return query_(self.root, 0, self.n-1)

    def query_scatter(self, q_right, limit):
        # print("query_scatter", limit ,"seats, before row", q_right)
        def query_(root, seg_st, seg_en):
            if root.sum == 0 :
                return 0
            if q_right < seg_st : # No overlap
                return 0
            if seg_en <= q_right:  # Full overlap
                return root.sum
            else:  # Partial overlap
                mid = (seg_st + seg_en) >> 1
                left_ret = query_(root.left, seg_st, mid)
                right_ret = query_(root.right, mid + 1, seg_en)
                # print(seg_st, seg_en, left_ret + right_ret)
                return left_ret + right_ret
        ret = query_(self.root, 0, self.n-1)
        # print("query total seats", ret)
        if ret >= limit :
            def update_front(root, seg_st, seg_en):
                nonlocal limit
                if q_right < seg_st : # No overlap
                    return
                if root.sum <= limit :
                    # print("eliminate :",root.max_value, root.sum, limit, seg_st, seg_en)
                    limit -= root.sum
                    root.max_value = 0
                    root.sum = 0
                    return
                if seg_st == seg_en :
                    # print("end node :",root.max_value, root.sum, limit)
                    root.max_value -= limit
                    root.sum -= limit
                    limit = 0
                    return
                mid = (seg_st + seg_en) >> 1
                update_front(root.left, seg_st, mid)
                if limit > 0 :
                    update_front(root.right, mid + 1, seg_en)
                self._update_node(root)
            update_front(self.root, 0, self.n-1)
            return True
        else :
            return False

class BookMyShow:
    def __init__(self, n: int, m: int):
        self.segtree = SegTree(n,m)

    def gather(self, k: int, maxRow: int) -> List[int]:
        ret = self.segtree.query_gather(maxRow, k)
        if ret == -1 :
            return []
        else :
            return ret

    def scatter(self, k: int, maxRow: int) -> bool:
        return self.segtree.query_scatter(maxRow, k)



