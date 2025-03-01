# 1462. Course Schedule IV
# https://leetcode.com/problems/course-schedule-iv/description

from typing import List
from functools import cache

# using my template <find_lower> : 11ms Beats99.10%
# O(n)
    # because of "if seen[next_lower]:continue", 
    # dfs will pass each point only once
def link(relation, len_n = -1):
    li = [[] for _ in range(len_n)]

    # build
    for n1,n2 in relation :
        li[n1].append(n2)
    return li

def find_lower(upper_rela, len_n):
    li = link(upper_rela, len_n)
    @cache
    def dfs(now_n):
        low_rela = set([now_n])
        for next_lower in li[now_n]:
            if next_lower in low_rela: 
                continue
            low_rela |= dfs(next_lower)
        return low_rela
    return [dfs(i) for i in range(len_n)]

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        lower_rela = find_lower(prerequisites, numCourses)
        return [n2 in lower_rela[n1] for n1,n2 in queries]
    
# using my template <cut_all_branch> : 26ms Beats88.58%
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        len_n = numCourses
        li = [[] for _ in range(len_n)]
        deg = [0] * len_n
        for n1,n2 in prerequisites:
            deg[n2] += 1  # 統計基環樹每個節點的入度
            li[n1].append(n2)
        end_point = [i for i, d in enumerate(deg) if d == 0]
        rel_mem = [set([i]) for i in range(len_n)]
        while end_point:  # 拓樸排序，剪掉圖上所有樹枝
            now_n = end_point.pop()
            for nei_n in li[now_n] :
                rel_mem[nei_n] |= rel_mem[now_n]
                deg[nei_n] -= 1
                if deg[nei_n] == 0:
                    end_point.append(nei_n)
        return [n1 in rel_mem[n2] for n1,n2 in queries]

s = Solution()
# print("ans :",s.checkIfPrerequisite(numCourses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]])) # [false,true]
# print("ans :",s.checkIfPrerequisite(numCourses = 2, prerequisites = [], queries = [[1,0],[0,1]])) # [false,false]
# print("ans :",s.checkIfPrerequisite(numCourses = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]])) # [true,true]
# print("ans :",s.checkIfPrerequisite()) # 



