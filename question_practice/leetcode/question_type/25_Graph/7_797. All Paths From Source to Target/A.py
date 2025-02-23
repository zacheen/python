# 797. All Paths From Source to Target
# https://leetcode.com/problems/all-paths-from-source-to-target

from typing import List
from math import inf

from functools import cache
# my 0ms Beats100.00%
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        end_p = len(graph)-1
        @cache
        def dfs(this_n) :
            if this_n == end_p :
                return [[end_p]]
            all_path = []
            for next_n in graph[this_n] :
                ret = dfs(next_n)
                for path in ret :
                    all_path.append([this_n] + path)
            return all_path
        return dfs(0)

s = Solution()
print("ans :",s.allPathsSourceTarget([[1,2],[3],[3],[]])) # [[0,1,3],[0,2,3]]
print("ans :",s.allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]])) # [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]



