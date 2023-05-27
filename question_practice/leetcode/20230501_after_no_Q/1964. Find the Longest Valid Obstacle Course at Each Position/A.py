# 1964. Find the Longest Valid Obstacle Course at Each Position
# https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position/

from typing import List
import functools

# my 沒想到
class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        pass
        # 如果限制是 n，我可以使用 n-1 的結果去判斷 n 最長的長度嗎?
            # 不行 133332 3
        # 

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



