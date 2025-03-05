# 1964. Find the Longest Valid Obstacle Course at Each Position
# https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position/

from typing import List
import functools

# my practice again : 131ms Beats86.54%
from bisect import bisect_right
class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        stack = []
        ans = []
        for n in obstacles :
            ret = bisect_right(stack,n)
            ans.append(ret+1)
            if ret == len(stack) :
                stack.append(n)
            else :
                stack[ret] = n
        return ans

# given ans Beats 100%
from bisect import bisect_right
class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        ans = []
        # tail[i] := the minimum tail of all increasing subseqs having length i + 1
        # it's easy to see that tail must be an increasing array
        tail = []

        for obstacle in obstacles:
            if not tail or obstacle >= tail[-1]:
                tail.append(obstacle)
                ans.append(len(tail))
            else:
                # 每次都把相對位置的數字替換成現在最小的數字
                index = bisect_right(tail, obstacle)
                tail[index] = obstacle
                ans.append(index + 1)
            # print(tail)
        return ans

s = Solution()
# print(s.longestObstacleCourseAtEachPosition([1,2,3,2]))
# print(s.longestObstacleCourseAtEachPosition([2,2,1]))
print(s.longestObstacleCourseAtEachPosition([3,1,5,6,4,2]))



