# 3380. Maximum Area Rectangle With Point Constraints I
# https://leetcode.com/problems/maximum-area-rectangle-with-point-constraints-i/description/

from typing import List
import functools

# my 0ms Beats100.00%
from itertools import pairwise
class Solution:
    def maxRectangleArea(self, points: List[List[int]]) -> int:
        def check_no_inside(xs,xe,ys,ye):
            # print("check :", xs,xe,ys,ye)
            c = 0
            for px,py in points :
                if xs <= px and px <= xe and ys <= py and py <= ye :
                    c += 1
                    if c > 4 :
                        return False
            return True
        
        points.sort()
        links = []
        ans = -1
        for (x1,x2),(y1,y2) in pairwise(points) :
            if x1 == y1 :
                for l1,(l1s, l1e) in links :
                    if l1s == x2 and l1e == y2 :
                        if check_no_inside(l1, x1, l1s, l1e) :
                            ans = max(ans, (l1e-l1s)*(x1-l1) )
                links.append((x1,(x2,y2)))
        return ans

# given ans

s = Solution()
print(s.maxRectangleArea(points = [[1,1],[1,3],[3,1],[3,3]])) #4
print(s.maxRectangleArea(points = [[1,1],[1,3],[3,1],[3,3],[2,2]])) #-1
print(s.maxRectangleArea([[1,1],[1,3],[3,1],[3,3],[1,2],[3,2]])) #2
print(s.maxRectangleArea([[1,50],[86,99],[1,99],[86,50],[24,96]]))



