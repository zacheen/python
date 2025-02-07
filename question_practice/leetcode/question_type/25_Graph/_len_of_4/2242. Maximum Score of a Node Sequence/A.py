# 2242. Maximum Score of a Node Sequence
# https://leetcode.com/problems/maximum-score-of-a-node-sequence/description/

from typing import List
import functools

# opt : 405ms Beats77.53%
    # given ans's upper part is faster
    #          my lower part is faster

# my ref solution : 455ms Beats60.67%
from collections import defaultdict
import heapq
from math import inf
class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        links = defaultdict(list)
        for n1,n2 in edges :
            heapq.heappush(links[n1], (scores[n2], n2))
            if len(links[n1]) > 4 :
                heapq.heappop(links[n1])
            heapq.heappush(links[n2], (scores[n1], n1))
            if len(links[n2]) > 4 :
                heapq.heappop(links[n2])

        for i in range(len(scores)) :
            links[i].sort(reverse=True)

        def find_best(n_f, n_s):
            seen = {n1,n2}
            # n_f first find
            n_f_best = -inf
            for p, link in links[n_f] :
                if link not in seen:
                    n_f_best = p
                    seen.add(link)
                    break
            for p, link in links[n_s] :
                if link not in seen:
                    return n_f_best + p
            return -inf

        max_ans = -1
        for n1,n2 in edges :
            s = scores[n1]+scores[n2] 
            max_ans = max(max_ans, s + max(find_best(n1,n2), find_best(n2,n1)))
        return max_ans
            
# given ans 438ms Beats68.54%
class Solution:
    def maximumScore(self, scores: list[int], edges: list[list[int]]) -> int:
        n = len(scores)
        ans = -1
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append((scores[v], v))
            graph[v].append((scores[u], u))

        for i in range(n):
            graph[i] = heapq.nlargest(3, graph[i])

        # To find the target sequence: a - u - v - b, enumerate each edge (u, v),
        # and find a (u's child) and b (v's child). That's why we find the 3
        # children that have the highest scores because one of the 3 children is
        # guaranteed to be valid.
        for u, v in edges:
            s = scores[u] + scores[v]
            for scoreA, a in graph[u]:
                s_and_A = scoreA + s
                for scoreB, b in graph[v]:
                    if a != b and a != v and b != u:
                        ans = max(ans, s_and_A + scoreB)
        return ans
    
s = Solution()
# print("ans :",s.maximumScore(scores = [5,2,9,8,4], 
#     edges = [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]])) # 24
# print("ans :",s.maximumScore(scores = [9,20,6,4,11,12], 
#     edges = [[0,3],[5,3],[2,4],[1,3]])) # -1
print("ans :",s.maximumScore([18,6,4,9,8,2],
    [[0,1],[0,2],[0,3],[0,4],[0,5],[1,2],[1,3],[1,4],[1,5],[2,3],[2,4],[2,5],[3,4],[3,5],[4,5]])) # 41


