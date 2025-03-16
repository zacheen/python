# 2250. Count Number of Rectangles Containing Each Point
# https://leetcode.com/problems/count-number-of-rectangles-containing-each-point/description/

from typing import List
from math import inf
from sortedcontainers import SortedList

# given ans 166ms Beats97.04%
class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        mem = []
        for l, h in rectangles :
            while len(mem) <= h :
                mem.append([])
            mem[h].append(l)

        l_list = SortedList()
        p_order = list(range(len(points)))
        p_order.sort(key = lambda x : points[x][1], reverse = True)
        ans = [None]*len(points)
        now_add_h = len(mem)
        for p_i in p_order :
            p_l, p_h = points[p_i]
            while p_h < now_add_h :
                now_add_h -= 1
                for l in mem[now_add_h] :
                    l_list.add(l)
            ret_i = l_list.bisect_left(p_l)
            ans[p_i] = len(l_list) - ret_i
        return ans

# my 2049ms Beats29.41%
class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        mem = []
        for l, h in rectangles :
            while len(mem) <= h :
                mem.append(SortedList())
            mem[h].add(l)

        ans = []
        for pl, ph in points :
            cou = 0
            for poss_ph in range(ph, len(mem)) :
                cou += len(mem[poss_ph]) - mem[poss_ph].bisect_left(pl)
            ans.append(cou)
        return ans

s = Solution()
print("ans :",s.countRectangles(rectangles = [[1,2],[2,3],[2,5]], points = [[2,1],[1,4]])) # [2, 1]
print("ans :",s.countRectangles(rectangles = [[1,1],[2,2],[3,3]], points = [[1,3],[1,1]])) # [1, 3]



