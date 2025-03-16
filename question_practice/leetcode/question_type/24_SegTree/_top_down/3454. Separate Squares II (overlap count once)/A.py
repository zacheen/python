# 3454. Separate Squares II
# https://leetcode.com/problems/separate-squares-ii/description/

from typing import List
from math import inf

# my 2902ms Beats60.28%
class SegTree:
    def __init__(self, nums):
        self.nums = nums
        self.n = len(nums)
        self.tree = [0]*(4*self.n)
        self.cover_cou = [0]*(4*self.n)

    def update(self, q_left, q_right, value):
        def _update(tree_idx, seg_st, seg_en):
            mid = (seg_st + seg_en) >> 1
            tree_idx_l = tree_idx << 1
            tree_idx_r = tree_idx_l + 1
            if q_right <= seg_st or seg_en <= q_left :  # No overlap
                return
            elif q_left <= seg_st and seg_en <= q_right:  # Full overlap
                self.cover_cou[tree_idx] += value
            else :
                _update(tree_idx_l, seg_st, mid)
                _update(tree_idx_r, mid, seg_en)
            
            if self.cover_cou[tree_idx] > 0 :
                self.tree[tree_idx] = self.nums[seg_en] - self.nums[seg_st]
            else :
                if seg_en - seg_st == 1 : # last leaf
                    self.tree[tree_idx] = 0
                else :
                    self.tree[tree_idx] = self.tree[tree_idx_l] + self.tree[tree_idx_r]
        _update(1, 0, self.n - 1)

from sortedcontainers import SortedList 
from bisect import bisect_left
class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        squares.sort(key = lambda x : x[1])
        squares.append([0,2*(10**9)+1,0])
        
        poss_x = set()
        for x,y,l in squares :
            poss_x.add(x)
            poss_x.add(x+l)
        poss_x = sorted(poss_x)
        x2i = {n:i for i,n in enumerate(poss_x)}
        x_seg = SegTree(poss_x)

        # cal total_area, half_area
        total_area = 0
        stack_y = SortedList()
        last_pos = squares[0][1]
        history = []
        for x,y,l in squares :
            # 先排除超過範圍的
            while stack_y and stack_y[0][0] <= y :
                end_y, pre_x, pre_x_end = stack_y.pop(0)
                history.append((total_area, last_pos, x_seg.tree[1]))
                pop_area = (end_y-last_pos)*x_seg.tree[1]
                total_area += pop_area
                last_pos = end_y
                x_seg.update(pre_x, pre_x_end, -1)

            # 計算範圍內的
            history.append((total_area, last_pos, x_seg.tree[1]))
            pop_area = (y-last_pos)*x_seg.tree[1]
            total_area += pop_area
            last_pos = y
            
            # 加入此 squ 進 stack_y
            x_st_i = x2i[x]
            x_end_i = x2i[x+l]
            x_seg.update(x_st_i, x_end_i, 1)
            stack_y.add((y+l, x_st_i, x_end_i))

        half_area = total_area/2
        ins_i = bisect_left(history, half_area, key = lambda x : x[0])-1
        acc_area, last_pos, x_len = history[ins_i]
        if x_len == 0 :
            return last_pos
        else :
            return last_pos + ((half_area-acc_area)/x_len)

import bisect
# given ans : 2201ms Beats83.07%
class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        events = []
        xs_set = set()
        for x, y, l in squares:
            events.append((y, 1, x, x + l))
            events.append((y + l, -1, x, x + l))
            xs_set.add(x)
            xs_set.add(x + l)
        xs = sorted(xs_set)
        xs2i = {n:i for i,n in enumerate(xs)}
        n = len(xs) - 1
        cover = [0] * (4 * n)
        seglen = [0] * (4 * n)

        def process(idx, l_idx, r_idx, ql, qr, val):
            if ql >= r_idx or qr <= l_idx:
                return
            if ql <= l_idx and r_idx <= qr:
                cover[idx] += val
            else:
                mid = (l_idx + r_idx) // 2
                process(idx * 2, l_idx, mid, ql, qr, val)
                process(idx * 2 + 1, mid, r_idx, ql, qr, val)
            
            if cover[idx] > 0:
                seglen[idx] = xs[r_idx] - xs[l_idx]
            else:
                if r_idx - l_idx == 1:
                    seglen[idx] = 0
                else:
                    seglen[idx] = seglen[idx * 2] + seglen[idx * 2 + 1]

        events.sort(key=lambda e: e[0])
        segments = []
        current_y = events[0][0]
        union_x = 0
        i = 0
        m = len(events)
        while i < m:
            y = events[i][0]
            if y != current_y:
                segments.append((current_y, y, union_x))
                current_y = y
            while i < m and events[i][0] == y:
                _, typ, x1, x2 = events[i]
                process(1, 0, n, xs2i[x1], xs2i[x2], typ)
                i += 1
            union_x = seglen[1]

        total_area = 0
        seg_areas = []
        for y0, y1, L in segments:
            area_seg = L * (y1 - y0)
            seg_areas.append(area_seg)
            total_area += area_seg

        if total_area == 0:
            return 0.0

        cum = [0]
        for area_seg in seg_areas:
            cum.append(cum[-1] + area_seg)

        target = total_area / 2.0

        for i, (y0, y1, L) in enumerate(segments):
            prev_area = cum[i]
            if cum[i+1] >= target:
                if L == 0:
                    return float(y0)
                extra = target - prev_area
                y_ans = y0 + extra / L
                return y_ans

        return segments[-1][1]

s = Solution()
print("ans :",s.separateSquares([[0,0,1],[2,2,1]])) # 1.0
print("ans :",s.separateSquares([[0,0,2],[1,1,1]])) # 1.0
print("ans :",s.separateSquares([[9,28,3],[7,19,1],[13,18,2]]))
print("ans :",s.separateSquares([[0,0,3],[1,2,5],[2,4,2]])) 
print("ans :",s.separateSquares([[0,0,6],[1,2,5],[2,4,2]]))
print("ans :",s.separateSquares([[15,21,2],[19,21,3]])) # 22.3

# 這個 case 全部正方形都沒有重複，主要是測 其實數字會到 2*10**9
# print("ans :",s.separateSquares([[999892931,999974790,6788622],[319710671,963660807,5518783],[623736653,934759633,4248549],[234214719,848813522,417010],[154771654,645515409,9370045],[965571354,998982755,10809560],[338822522,550588284,12471651],[168193362,682286828,5173004],[459856474,778674604,5635628],[806653114,860720237,1444683]])) # 21.83333





