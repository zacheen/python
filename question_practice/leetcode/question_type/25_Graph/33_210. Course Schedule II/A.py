# 210. Course Schedule II
# https://leetcode.com/problems/course-schedule-ii

from typing import List
from math import inf

# my (cut_all_branch) 1ms Beats86.29%
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # revise from cut_all_branch
        ans = []
        li = [[] for _ in range(numCourses)]
        # build
        for n1,n2 in prerequisites :
            li[n2].append(n1)

        deg = [0] * numCourses
        for n1,n2 in prerequisites:
            deg[n1] += 1  # 統計基環樹每個節點的入度
        end_point = [i for i, d in enumerate(deg) if d == 0]
        while end_point:  # 拓樸排序，剪掉圖上所有樹枝
            now_n = end_point.pop()
            ans.append(now_n)
            for nei_n in li[now_n] :
                deg[nei_n] -= 1
                if deg[nei_n] == 0:
                    end_point.append(nei_n)

        if len(ans) == numCourses :
            return ans
        else:
            return []

# given ans


s = Solution()
print("ans :",s.findOrder(numCourses = 2, prerequisites = [[1,0]])) # [0,1]
print("ans :",s.findOrder(numCourses = 2, prerequisites = [[1,0],[0,1]])) # []
print("ans :",s.findOrder(numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]])) # [0,2,1,3]
print("ans :",s.findOrder(numCourses = 1, prerequisites = [])) # [0]



