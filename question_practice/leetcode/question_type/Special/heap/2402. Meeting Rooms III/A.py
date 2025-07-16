# 2402. Meeting Rooms III
# https://leetcode.com/problems/meeting-rooms-iii

from typing import List
from math import inf
from collections import deque
from heapq import heapify, heappop, heappush

# my using heap to optimize : 160ms Beats88.50%
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key = lambda x : x[0])
        room_cnt = [0]*n
        room_fin = []
        ava = list(range(n))
        heapify(ava)

        q = deque()
        for st, en in meetings :
            while q and room_fin and room_fin[0][0] <= st:
                # 這些取出來之後 又會馬上使用
                fin_t, i = heappop(room_fin)
                room_cnt[i] += 1
                heappush(room_fin, (fin_t+q.popleft(), i))
            while room_fin and room_fin[0][0] <= st: 
                # 這些房間已經空閒
                fin_t, i = heappop(room_fin)
                heappush(ava, i)
            if ava :
                min_i = heappop(ava)
                room_cnt[min_i] += 1
                heappush(room_fin, (en, min_i))
            else :
                q.append(en - st)
        
        # 等全部的會議結束
        while q :
            # 這些取出來之後 又會馬上使用
            fin_t, i = heappop(room_fin)
            room_cnt[i] += 1
            heappush(room_fin, (fin_t+q.popleft(), i))
        
        min_i = 0
        max_cnt = 0
        for i, c in enumerate(room_cnt) :
            if c > max_cnt :
                min_i = i
                max_cnt = c
        return min_i

# # my : 691ms Beats8.37%
# class Solution:
#     def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
#         meetings.sort(key = lambda x : x[0])
#         room_cnt = [0]*n
#         room_fin = [0]*n
#         def find_near(now_t):
#             min_i = -1
#             min_t = now_t+1
#             for i, t in enumerate(room_fin) :
#                 if t < min_t :
#                     min_i = i
#                     min_t = t
#             return min_i, min_t
#         def find_ava(now_t):
#             for i, t in enumerate(room_fin) :
#                 if t <= now_t :
#                     return i
#             return -1

#         q = deque()
#         for st, en in meetings :
#             while q :
#                 min_i, fin_t = find_near(st)
#                 if min_i != -1 :
#                     room_cnt[min_i] += 1
#                     room_fin[min_i] = fin_t + q.popleft()
#                 else :
#                     break
#             if q :
#                 q.append(en - st)
#             else :
#                 if (min_i := find_ava(st)) != -1:
#                     room_cnt[min_i] += 1
#                     room_fin[min_i] = en
#                 else :
#                     q.append(en - st)
#         # 等全部的會議結束
#         while q :
#             min_i, fin_t = find_near(inf)
#             if min_i != -1 :
#                 room_cnt[min_i] += 1
#                 room_fin[min_i] = fin_t + q.popleft()
        
#         min_i = 0
#         max_cnt = 0
#         # print(room_cnt)
#         for i, c in enumerate(room_cnt) :
#             if c > max_cnt :
#                 min_i = i
#                 max_cnt = c
#         return min_i

# # my v2 using segtree to optimize : 805ms Beats6.13% (slower...)
# # replace find_near : return the smallest available time and its index
# class SegTree:
#     def __init__(self, n):
#         self.default_value = [-1, -1] # [index, available time]
#         self.n = n
#         self.tree = [self.default_value] * (4 * self.n)
#         def build_rec(tree_idx, seg_st, seg_en):
#             if seg_st == seg_en:
#                 self.tree[tree_idx] = [seg_st, 0]
#                 return
#             mid = (seg_st + seg_en) >> 1
#             tree_idx_l = tree_idx << 1
#             tree_idx_r = tree_idx_l + 1
#             build_rec(tree_idx_l, seg_st, mid)
#             build_rec(tree_idx_r, mid + 1, seg_en)
#             self._update_node(tree_idx, tree_idx_l, tree_idx_r)
#         build_rec(1, 0, self.n-1)

#     def _merge_val(self, l, r):
#         if r[1] < l[1] :
#             return r
#         return l
    
#     def _update_node(self, tree_idx, tree_idx_l, tree_idx_r) :
#         self.tree[tree_idx] = self._merge_val(self.tree[tree_idx_l], self.tree[tree_idx_r])

#     def update(self, index, value):
#         def update_rec(tree_idx, seg_st, seg_en):
#             if seg_st == index and index == seg_en:  # Entire segment is target index
#                 self.tree[tree_idx][1] = value
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

#     def query_near(self): # include both q_left, q_right
#         return self.tree[1]

# class Solution:
#     def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
#         segtree = SegTree(n)
#         meetings.sort(key = lambda x : x[0])
#         room_cnt = [0]*n
#         room_fin = [0]*n
#         def find_ava(now_t):
#             for i, t in enumerate(room_fin) :
#                 if t <= now_t :
#                     return i
#             return -1

#         q = deque()
#         for st, en in meetings :
#             while q :
#                 min_i, fin_t = segtree.query_near()
#                 if fin_t <= st :
#                     room_cnt[min_i] += 1
#                     new_fin = fin_t + q.popleft()
#                     segtree.update(min_i, new_fin)
#                     room_fin[min_i] = new_fin
#                 else :
#                     break
#             if q :
#                 q.append(en - st)
#             else :
#                 if (min_i := find_ava(st)) != -1:
#                     room_cnt[min_i] += 1
#                     segtree.update(min_i, en)
#                     room_fin[min_i] = en
#                 else :
#                     q.append(en - st)
#         # 等全部的會議結束
#         while q :
#             min_i, fin_t = segtree.query_near()
#             room_cnt[min_i] += 1
#             new_fin = fin_t + q.popleft()
#             segtree.update(min_i, new_fin)
#             room_fin[min_i] = new_fin
        
#         min_i = 0
#         max_cnt = 0
#         for i, c in enumerate(room_cnt) :
#             if c > max_cnt :
#                 min_i = i
#                 max_cnt = c
#         return min_i

s = Solution()
print("ans :",s.mostBooked(n = 2, meetings = [[0,10],[1,5],[2,7],[3,4]])) # 0
print("ans :",s.mostBooked(n = 3, meetings = [[1,20],[2,10],[3,5],[4,9],[6,8]])) # 1
print("ans :",s.mostBooked(n = 100, meetings = [[0,1]])) # 0

