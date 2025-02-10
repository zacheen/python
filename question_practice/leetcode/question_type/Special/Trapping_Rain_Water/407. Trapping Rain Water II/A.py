# 407. Trapping Rain Water II
# https://leetcode.com/problems/trapping-rain-water-ii/description

from typing import List
import functools
import heapq

dir_list = [(0, 1), (0, -1), (1, 0), (-1, 0)]
# # given ans
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0
        
        m, n = len(heightMap), len(heightMap[0])
        heap = []
        visited = [[False] * n for _ in range(m)]
        
        # Add border cells to heap
        for j in range(n):
            heapq.heappush(heap, (heightMap[0][j], 0, j))
            heapq.heappush(heap, (heightMap[m-1][j], m-1, j))
            visited[0][j] = visited[m-1][j] = True
            
        for i in range(1, m-1):
            heapq.heappush(heap, (heightMap[i][0], i, 0))
            heapq.heappush(heap, (heightMap[i][n-1], i, n-1))
            visited[i][0] = visited[i][n-1] = True
            
        water = 0
        while heap:
            height, row, col = heapq.heappop(heap)
            for dx,dy in dir_list:
                new_row, new_col = row + dx, col + dy
                if (new_row < 0 or new_row >= m or new_col < 0 or new_col >= n or visited[new_row][new_col]):
                    continue
                if heightMap[new_row][new_col] < height:
                    water += height - heightMap[new_row][new_col]
                    heapq.heappush(heap, (height, new_row, new_col))
                else:
                    heapq.heappush(heap, (heightMap[new_row][new_col], new_row, new_col))
                visited[new_row][new_col] = True
        return water

# my cannot deal corner
# import copy
# from math import inf
# class Solution:
#     def trapRainWater(self, heightMap: List[List[int]]) -> int:
#         mem = [copy.deepcopy(heightMap) for _ in range(4)]

#         # look left
#         this_mem = mem[0]
#         for i1 in range(len(this_mem)) :
#             for i2 in range(1,len(this_mem[i1])) :
#                 this_mem[i1][i2] = max(this_mem[i1][i2], this_mem[i1][i2-1])
#         # look right
#         this_mem = mem[1]
#         for i1 in range(len(this_mem)) :
#             for i2 in range(len(this_mem[i1])-2,-1,-1) :
#                 this_mem[i1][i2] = max(this_mem[i1][i2], this_mem[i1][i2+1])
#         # look up
#         this_mem = mem[2]
#         for i1 in range(1,len(this_mem)) :
#             for i2 in range(len(this_mem[i1])) :
#                 this_mem[i1][i2] = max(this_mem[i1][i2], this_mem[i1-1][i2])
#         # look down
#         this_mem = mem[3]
#         for i1 in range(len(this_mem)-2,-1,-1) :
#             for i2 in range(len(this_mem[i1])) :
#                 this_mem[i1][i2] = max(this_mem[i1][i2], this_mem[i1+1][i2])

#         poss_h = copy.deepcopy(heightMap)
#         water_h = copy.deepcopy(heightMap)
#         for i1, this_r in enumerate(heightMap) :
#             for i2, h in enumerate(this_r) :
#                 water_h[i1][i2] = min(mem[i][i1][i2] for i in range(4))
#                 poss_h[i1][i2] = water_h[i1][i2] - h

#         dir_list = [(0, 1), (0, -1), (1, 0), (-1, 0)]
#         n1_len = len(this_mem)
#         n2_len = len(this_mem[0])
#         def dfs(n1,n2) :
#             nonlocal dfs_h_stack
#             nonlocal min_h
#             min_h = min(water_h[n1][n2], min_h)
#             dfs_h_stack.append(heightMap[n1][n2])
#             poss_h[n1][n2] = 0
#             for d1,d2 in dir_list :
#                 nei1, nei2 = n1 + d1, n2 + d2
#                 if 0 <= nei1 < n1_len and 0 <= nei2 < n2_len and poss_h[nei1][nei2] != 0 :
#                     dfs(nei1,nei2)
#             return 

#         ans = 0
#         for i1 in range(1,len(this_mem)-1) :
#             for i2 in range(1,len(this_mem[i1])-1) :
#                 if poss_h[i1][i2] != 0 :
#                     min_h = inf
#                     dfs_h_stack = []
#                     dfs(i1,i2)
#                     ans += sum(max(0, min_h-h) for h in dfs_h_stack)
#         return ans

s = Solution()
# print("ans :",s.trapRainWater([[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]])) # 4
# print("ans :",s.trapRainWater([[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]])) # 10
# print("ans :",s.trapRainWater([[12,13,1,12],[13,4,13,12],[13,8,10,12],[12,13,12,12],[13,13,13,13]])) # 14
print("ans :",s.trapRainWater([[78,16,94,36],[87,93,50,22],[63,28,91,60],[64,27,41,27],[73,37,12,69],[68,30,83,31],[63,24,68,36]])) # 44
    # 28 > 37, 27 > 37, 12 > 37


