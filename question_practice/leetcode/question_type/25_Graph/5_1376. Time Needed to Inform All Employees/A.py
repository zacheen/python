# 1376. Time Needed to Inform All Employees
# https://leetcode.com/problems/time-needed-to-inform-all-employees

from typing import List
from math import inf

from collections import defaultdict
# my 271ms Beats60.25%
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # method 1
        links = defaultdict(list)
        # build
        for em, man in enumerate(manager) :
            links[man].append(em)

        max_time = 0
        def dfs(ma, t):
            nonlocal max_time
            if t > max_time :
                max_time = t
            t += informTime[ma]
            for em in links[ma] :
                dfs(em, t)
        dfs(headID, 0)
        return max_time

# given ans : 132ms Beats94.28%
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        def dfs(i):
            if manager[i] != -1:
                informTime[i] += dfs(manager[i])
                manager[i] = -1
            return informTime[i]
        return max(map(dfs, range(n)))

s = Solution()
print("ans :",s.numOfMinutes(n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0])) # 1



