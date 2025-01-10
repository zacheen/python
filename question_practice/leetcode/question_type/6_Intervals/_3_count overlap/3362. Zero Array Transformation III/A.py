# https://leetcode.com/problems/zero-array-transformation-iii/description/

from typing import List
import functools

# # my Time Limit Exceeded
# from itertools import accumulate
# class Solution:
#     def maxRemoval(self, nums: list[int], queries: list[list[int]]) -> int: 
#         interval = [0]*(len(nums) + 1)
#         for sta, end in queries :
#             interval[sta] += 1
#             interval[end+1] -= 1

#         remain = [aff-n for n, aff in zip(nums, accumulate(interval))]
#         # print("remain :",remain)   
#         if not all(re>=0 for re in remain) :
#             return -1

#         def hash_value(item):
#             return (item[1], -item[0])
#         queries = sorted(queries, key=hash_value)
#         # print("queries :",queries)

#         que_indx_mem = 0
#         ans_count = 0
#         for indx, re in enumerate(remain) :
#             while True:
#                 if re <= 0 or que_indx_mem >= len(queries) or indx < queries[que_indx_mem][1] :
#                     break
#                 if all(remain[i] for i in range(queries[que_indx_mem][0], queries[que_indx_mem][1]+1)) :
#                     for i in range(queries[que_indx_mem][0], queries[que_indx_mem][1]+1) :
#                         remain[i] -= 1
#                     ans_count += 1
#                 que_indx_mem += 1
#         return ans_count

# given ans 680ms Beats 23.75%
# 用 SortedList 比較好理解變化
from sortedcontainers import SortedList
from collections import deque
class Solution:
    def maxRemoval(self, nums: list[int], queries: list[list[int]]) -> int:
        q = deque(sorted(queries))
        available = SortedList()    # available `r`s
        running = SortedList()    # running `r`s

        for i, num in enumerate(nums):
            while q and q[0][0] <= i:
                available.add(q.popleft()[1])
            while running and running[0] < i:
                running.pop(0)
            while num > len(running):
                if not available or available[-1] < i:
                    return -1
                running.add(available.pop())
            # print("running :",running)
            # print("available :",available)
        return len(available)
   
# my opt ver1
# 270ms Beats77.97% / 58.65MB Beats78.83%
from sortedcontainers import SortedList
from collections import deque
import heapq
class Solution:
    def maxRemoval(self, nums: list[int], queries: list[list[int]]) -> int:
        q = deque(sorted(queries))
        available = []
        # available 同時記錄了 現在這個位置的重疊次數 以及尾端
        # 為了可以每次都取到 最大的尾端(效益最大) 所以才需要 heapq
        running = []
        # running 記錄了"已取用"的區間尾端 == 個數就是interval重疊次數

        for i, num in enumerate(nums):
            while q and q[0][0] <= i: # 加入從i開頭的 queries
                heapq.heappush(available, -q.popleft()[1])
            while running and running[0] < i: # 更新已經超出範圍的數字
                heapq.heappop(running)
            while num > len(running): # 如果目前取用的區間不到 num
                if not available or -available[0] < i:
                    return -1
                heapq.heappush(running, -heapq.heappop(available)) # 新增一個效益最大的queries
        return len(available)


# # my opt ver2
# # 415ms Beats39.59% / 47.46MB Beats99.66%
# # building heap : n, sorting : nlog(n)
# # but poping items, heapify : N*log(n), sort : N*1
# # because queries no needed to be modify, thus it get benefit from heap
# import heapq
# class Solution:
#     def maxRemoval(self, nums: list[int], queries: list[list[int]]) -> int:
#         heapq.heapify(queries)
#         available = []
#         # available 同時記錄了 現在這個位置的重疊次數 以及尾端
#         # 為了可以每次都取到 最大的尾端(效益最大) 所以才需要 heapq
#         running = []
#         # running 記錄了"已取用"的區間尾端 == 個數就是interval重疊次數

#         for i, num in enumerate(nums):
#             while queries and queries[0][0] <= i: # 加入從i開頭的 queries
#                 heapq.heappush(available, -heapq.heappop(queries)[1])
#             while running and running[0] < i: # 更新已經超出範圍的數字
#                 heapq.heappop(running)
#             while num > len(running): # 如果目前取用的區間不到 num
#                 if not available or -available[0] < i:
#                     return -1
#                 heapq.heappush(running, -heapq.heappop(available)) # 新增一個效益最大的queries
#         return len(available)

s = Solution()
# print("ans :",s.maxRemoval(nums = [2,0,2], queries = [[0,2],[0,2],[1,1]]))
print("ans :",s.maxRemoval(nums = [2,0,2,0], queries = [[0,2],[0,2],[1,1]]))
# print("ans :",s.maxRemoval(nums = [2,3,2], queries = [[0,2],[0,2],[1,1]]))
# print("ans :",s.maxRemoval(nums = [1,1,1,1], queries = [[1,3],[0,2],[1,3],[1,2]]))
# print("ans :",s.maxRemoval(nums = [1,2,3,4], queries = [[0,3],[1,2]]))
# print("ans :",s.maxRemoval(nums = [2,6,1,2,5], queries = [[0,3],[0,1],[1,2],[1,4]]))



