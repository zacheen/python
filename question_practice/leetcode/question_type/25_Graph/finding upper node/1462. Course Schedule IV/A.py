# 1462. Course Schedule IV
# https://leetcode.com/problems/course-schedule-iv/description

from typing import List

from functools import cache
# my 31ms Beats78.82%
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        links = [[] for _ in range(numCourses)]
        for n1,n2 in prerequisites :
            links[n2].append(n1)

        @cache
        def dfs(n) :
            all_prereq = set([n])
            for prereq in links[n] :
                all_prereq |= dfs(prereq)
            return all_prereq
        
        return [n1 in dfs(n2) for n1,n2 in queries]
    
# # combine my and given ans, but slower : 119ms Beats42.77%
# class Solution:
#     def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
#         links = [[] for _ in range(numCourses)]
#         for n1,n2 in prerequisites :
#             links[n2].append(n1)

#         mem_req = [[False]*numCourses for _ in range(numCourses)]
#         # mem_req[n1][n2] : n2 is n1 prereq
#         seen = set()
#         def dfs(n) :
#             if n in seen : return 
#             seen.add(n)
#             this_mem_req = mem_req[n]
#             this_mem_req[n] = True
#             for prereq in links[n] :
#                 dfs(prereq)
#                 for req, res in enumerate(mem_req[prereq]) :
#                     if res :
#                         this_mem_req[req] = True

#         for indx in range(numCourses) :
#             dfs(indx)
#         return [mem_req[n2][n1] for n1,n2 in queries]

# given ans 24ms Beats90.38%
    # because of "if used[v]: continue", 
    # each dfs(i, isPrerequisite[i]) will pass each point only once
        # in my solution, when set|set or "for req, res in enumerate(mem_req[prereq]) :" these are O(n)
        # in conclusion, it turn it into a tree, so every dfs(i, isPrerequisite[i]) at most O(n)
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = [[] for _ in range(numCourses)]
        # isPrerequisite[i][j] := True if course i is a prerequisite of course j.
        isPrerequisite = [[False] * numCourses for _ in range(numCourses)]

        for u, v in prerequisites:
            graph[u].append(v)

        def dfs(u: int, used: list[bool]) -> None:
            for v in graph[u]:
                if used[v]: 
                    continue
                used[v] = True
                dfs(v, used)
        # DFS from every course.
        for i in range(numCourses):
            dfs(i, isPrerequisite[i])

        return [isPrerequisite[u][v] for u, v in queries]

s = Solution()
print("ans :",s.checkIfPrerequisite(numCourses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]])) # [false,true]
print("ans :",s.checkIfPrerequisite(numCourses = 2, prerequisites = [], queries = [[1,0],[0,1]])) # [false,false]
print("ans :",s.checkIfPrerequisite(numCourses = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]])) # [true,true]
# print("ans :",s.checkIfPrerequisite()) # 



