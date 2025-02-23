# 207. Course Schedule
# https://leetcode.com/problems/course-schedule

from typing import List
from math import inf

# my v1 "has_cycle" : 3ms Beats89.25%
def link(relation, len_n):
    links = [[] for _ in range(len_n)]
    # build
    for n1,n2 in relation :
        links[n1].append(n2)
    return links

def has_cycle(links, len_n):
    li = link(links, len_n)
    color = [0] * len_n
    def dfs(x):
        if color[x] == 2 :
            return False
        color[x] = 1
        for next_n in li[x]:
            if color[next_n] == 1 or dfs(next_n):
                return True
        color[x] = 2
        return False
    return any(dfs(n) for n in range(len_n))

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        return not has_cycle(prerequisites, numCourses)

# my v2 "cut_all_branch"
    # "has_cycle" 應該還是會快一些，因為會中途結束
def link(relation, len_n = -1):
    links = [[] for _ in range(len_n)]

    # build
    for n1,n2 in relation :
        links[n1].append(n2)
    return links

def cut_all_branch(links, len_n):
    deg = [0] * len_n
    for n1,n2 in links:
        deg[n2] += 1  # 統計基環樹每個節點的入度
    li = link(links, len_n)
    max_depth = [-1] * len_n
    end_point = [i for i, d in enumerate(deg) if d == 0]
    # print("end_point", end_point)
    while end_point:  # 拓樸排序，剪掉圖上所有樹枝
        now_n = end_point.pop()
        for nei_n in li[now_n] :
            if max_depth[now_n] == -1 :
                max_depth[now_n] = 1
            max_depth[nei_n] = max_depth[now_n] + 1
            deg[nei_n] -= 1
            if deg[nei_n] == 0:
                end_point.append(nei_n)

    # return circle (回傳全部形成 circle 的點)
    return [i for i, l in enumerate(deg) if l > 0]

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        return len(cut_all_branch(prerequisites, numCourses)) == 0


s = Solution()
print("ans :",s.canFinish()) # 



