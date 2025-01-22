# 3425. Longest Special Path
# https://leetcode.com/problems/longest-special-path/description/
    # actually it is a tree
        # I saw "Note that a path may start and end at the same node." and thought it might generate a circle
from typing import List
import functools

# given ans 362ms Beats100.00%
# import sys
# sys.setrecursionlimit(10**7)
class Solution:
    def longestSpecialPath(self, edges, nums):
        n = len(nums)
        adj = [[] for _ in range(n)]
        for u,v,w in edges:
            adj[u].append((v,w))
            adj[v].append((u,w))

        dist = [0]*n
        startIndex = [0]*n
        lastPos = {}
        stack = []
        bestLen = 0
        bestCount = 1
        def dfs(now_p, prev_p):
            nonlocal bestLen, bestCount
            stack.append(now_p)  # stack 會記錄所有經過的點的數字，dp 結束會自動 pop
            idx = len(stack) - 1
            old = lastPos.get(nums[now_p], -1) # old 是上一個一樣 nums 的點的 idx
            lastPos[nums[now_p]] = idx
            if prev_p == -1:
                cal_start = 0
            else:
                # 比較 前一個點的底 與 上一個一樣nums的點的idx 取大的
                    # 前一個點的底 : 之前的點有遇到相同的數字了
                    # 上一個一樣nums的點的idx : 這個點的 num 相衝的點
                cal_start = max(startIndex[prev_p], old + 1 if old != -1 else 0)
            startIndex[now_p] = cal_start # startIndex 用來記錄目前的底在哪裡
            if cal_start <= idx:
                # 這裡是用了類似計算某個區域的 sum 的方法
                L = dist[now_p] - dist[stack[cal_start]]
                cnt = idx - cal_start + 1
            else:
                L = 0
                cnt = 1
            # update
            if L > bestLen:
                bestLen = L
                bestCount = cnt
            elif L == bestLen and cnt < bestCount:
                bestCount = cnt
            # dfs
            for v, w in adj[now_p]:
                if v != prev_p:
                    dist[v] = dist[now_p] + w # dist 是 0 到此點的距離
                    dfs(v, now_p)
            # return to this point
            lastPos[nums[now_p]] = old # 因為 dp 回來了, 最後一個這個顏色的點當然就是此點
            stack.pop()

        dfs(0, -1)
        return [bestLen, bestCount]
    
# # my fail, I thought path is in order...
# from collections import deque
# class Solution:
#     def longestSpecialPath(self, edges: List[List[int]], nums: List[int]) -> List[int]:
#         first_p = edges[0][0]
#         mem = {first_p : [deque(), set([nums[first_p]]), set([first_p]), 0]}
#         ans = [0,0]
#         for n1,n2,w in edges:
#             if nums[n1] == nums[n2] :
#                 # 連續相同的 nums
#                 mem[n2] = [deque(), set([nums[n2]]), set([n2]),0]
#                 continue
            
#             # get mem
#             stack, seen_num, seen_p, s = mem[n1]
#             if n2 in seen_p :
#                 s += w
#                 if s > ans[0] :
#                     ans = [s, len(stack)]
#                 elif s == ans[0] :
#                     ans[1] = min(ans[1], len(stack))
#                 continue

#             # remove invalid node
#             stack = stack.copy()
#             seen_num = seen_num.copy()
#             seen_p = seen_p.copy()
#             while nums[n2] in seen_num :
#                 pop_n, pop_w = stack.popleft()
#                 seen_num.remove(nums[pop_n])
#                 seen_p.remove(pop_n)
#                 s -= pop_w

#             # add new node
#             stack.append([n1, w])
#             seen_num.add(nums[n2])
#             seen_p.add(n2)
#             s += w
#             if s > ans[0] :
#                 ans = [s, len(stack)]
#             elif s == ans[0] :
#                 ans[1] = min(ans[1], len(stack))

#             mem[n2] = [stack, seen_num, seen_p, s]
#             _ = ""

#         ans[1] += 1
#         return ans

s = Solution()
# print("ans :",s.longestSpecialPath(edges = [[0,1,2],[1,2,3],[1,3,5],[1,4,4],[2,5,6]], nums = [2,1,2,1,3,1])) # [6, 2]
# print("ans :",s.longestSpecialPath(edges = [[1,0,8]], nums = [2,2])) # [0, 1]
print("ans :",s.longestSpecialPath(edges = [[1,0,7],[1,2,4]], nums = [1,1,3])) # [4,2]
# print("ans :",s.longestSpecialPath([[2,0,2],[1,2,10]],[1,5,4])) # 
# print("ans :",s.longestSpecialPath([[1,0,1],[1,2,6]], [4,3,5])) # 

# invalid test case
# print("ans :",s.longestSpecialPath(edges = [[0,1,2],[1,2,3],[1,3,5],[1,4,4],[2,5,6],[4,0,2]], nums = [2,1,2,1,3,1])) # [8, 3]
# print("ans :",s.longestSpecialPath(edges = [[0,1,2],[1,4,4],[4,0,2]], nums = [2,1,2,1,3,1])) # [8, 3]


