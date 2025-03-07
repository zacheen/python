# 1964. Find the Longest Valid Obstacle Course at Each Position
# https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position/

from typing import List
import functools

# my practice again : 127ms Beats93.48%
    # using template LIS_nonstrict
from bisect import bisect_right
from math import inf
class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles):
        stack = [inf]
        ans = []
        for n in obstacles :
            if n >= stack[-1] :
                stack.append(n)
                ans.append(len(stack))
            else :
                ins_i = bisect_right(stack,n)
                stack[ins_i] = n
                ans.append(ins_i+1)
        return ans

s = Solution()
# print(s.longestObstacleCourseAtEachPosition([1,2,3,2]))
# print(s.longestObstacleCourseAtEachPosition([2,2,1]))
print(s.longestObstacleCourseAtEachPosition([3,1,5,6,4,2]))



