# 3615. Longest Palindromic Path in Graph
# https://leetcode.com/problems/longest-palindromic-path-in-graph/

from typing import List
from math import inf
from functools import cache
from collections import defaultdict

# my inspire by 
    # https://youtu.be/PEtBl6mJv-g?si=ah6UCNeiu2_aS1dS
    # 但這個舉例是錯誤的 "b - a - b 延伸到 c" 跟 "h - f - h 延伸到 c" 是不一樣的
        # 因為 c 可以再從 b 或 h 延伸回來
    # d - c - b - a - b - c - e
    # e /   \ h - f - h /   \ g
# but optimized : 295ms Beats ??%
max = lambda x, y: x if x > y else y
class Solution:
    def maxLen(self, n: int, edges: List[List[int]], label: str) -> int:
        len_n = n
        li = [defaultdict(list) for _ in range(len_n)]
        # build
        for n1,n2 in edges :
            li[n1][label[n2]].append(n2)
            li[n2][label[n1]].append(n1)
        
        @cache
        def dp(n1, n2, vis):
            max_ret = 0
            for n1_next_w, n1_next_w_lable in li[n1].items():
                n2_next_w_lable = li[n2][n1_next_w]
                n1_next_w_lable = [n for n in n1_next_w_lable if (vis >> n) & 1 == 0]
                n2_next_w_lable = [n for n in n2_next_w_lable if (vis >> n) & 1 == 0]
                for n1_next in n1_next_w_lable:
                    for n2_next in n2_next_w_lable:
                        if n1_next == n2_next : continue
                        if n1_next > n2_next :
                            n1_next, n2_next = n2_next, n1_next
                        max_ret = max(max_ret, 2 + dp(n1_next, n2_next, vis|(1<<n1_next)|(1<<n2_next)))
            return max_ret
        
        max_ans = 1
        for st_node in range(len_n) :
            max_ans = max(dp(st_node, st_node, 1<<st_node)+1, max_ans)
            if max_ans == n : return n
            # two node start (n1 should be smaller than n2)
            for st_node2 in li[st_node][label[st_node]]:
                if st_node < st_node2:
                    max_ans = max(dp(st_node, st_node2, (1<<st_node)|(1<<st_node2))+2, max_ans)
                    if max_ans == n : return n
        return max_ans

s = Solution()
print("ans :",s.maxLen(n = 3, edges = [[0,1],[1,2]], label = "aba")) # 3
print("ans :",s.maxLen(n = 3, edges = [[0,1],[0,2]], label = "abc")) # 1
print("ans :",s.maxLen(n = 4, edges = [[0,2],[0,3],[3,1]], label = "bbac")) # 3
print("ans :",s.maxLen(n = 3, edges = [[1,0],[2,1],[0,2]], label = "hjj")) # 3



