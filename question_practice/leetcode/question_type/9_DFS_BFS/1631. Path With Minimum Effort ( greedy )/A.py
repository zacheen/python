# (X)
# my Time Limit Exceeded
# import math
# class Solution:
#     def minimumEffortPath(self, heights):
#         bound_i = len(heights)
#         bound_ii = len(heights[0])
#         end_i = bound_i-1
#         end_ii = bound_ii-1
        
#         if bound_i <= 1 and bound_ii <= 1 :
#             return 0
        
#         # 紀錄走到這一點 最小的 abs
#         mem = [[math.inf]*len(heights[0]) for _ in range(len(heights))]
        
#         def bfs(next_pos, path, now_min):
#             if next_pos[0] == -1 or next_pos[0] == bound_i :
#                 return None
#             if next_pos[1] == -1 or next_pos[1] == bound_ii :
#                 return None
#             if next_pos in path :
#                 return None
            
#             direct = [1,0,-1,0,1]
#             last_pos = path[-1]
#             now_min = max(now_min, abs(heights[next_pos[0]][next_pos[1]] - heights[last_pos[0]][last_pos[1]]) )
#             if now_min < mem[next_pos[0]][next_pos[1]] :
#                 mem[next_pos[0]][next_pos[1]] = now_min
            
#                 # 到終點就不用繼續了
#                 if next_pos[0] == end_i and next_pos[1] == end_ii :
#                     return None
                
#                 # 有更新再繼續找路
#                 for i in range(4):
#                     ret = bfs((next_pos[0]+direct[i],next_pos[1]+direct[i+1]), path + [(next_pos[0],next_pos[1])], now_min)
            
#         bfs((1,0) ,[(0,0)], 0)
#         bfs((0,1) ,[(0,0)], 0)
#         return mem[-1][-1]
        
# given ans
# 每次都先找目前差距最小的路徑走
# 如果到終點就一定是最大差距最小的
# (O)
class Solution:
    def minimumEffortPath(self, heights):
        m = len(heights)
        n = len(heights[0])
        dirs = [0, 1, 0, -1, 0]
        # diff[i][j] := max absolute difference to reach (i, j
        diff = [[math.inf] * n for _ in range(m)]
        seen = set()

        minHeap = [(0, 0, 0)]  # (d, i, j)
        diff[0][0] = 0

        while minHeap:
            # 每次都先找目前差距最小的路徑走
            d, i, j = heapq.heappop(minHeap)
            if i == m - 1 and j == n - 1:
                return d
            seen.add((i, j))
            for k in range(4):
                x = i + dirs[k]
                y = j + dirs[k + 1]
                if x < 0 or x == m or y < 0 or y == n:
                    continue
                if (x, y) in seen:
                    continue
                newDiff = abs(heights[i][j] - heights[x][y])
                maxDiff = max(diff[i][j], newDiff)
                if diff[x][y] > maxDiff:
                    diff[x][y] = maxDiff
                    heapq.heappush(minHeap, (diff[x][y], x, y))

s = Solution()
# print(s.minimumEffortPath([[1,2,2],[3,8,2],[5,3,5]])) # 2
# print(s.minimumEffortPath([[1,2,3],[3,8,4],[5,3,5]])) # 1
# print(s.minimumEffortPath([[1,2,1,1,1],
#                            [1,2,1,2,1],
#                            [1,2,1,2,1],
#                            [1,2,1,2,1],
#                            [1,1,1,2,1]])) # 0
# print(s.minimumEffortPath([[1,2,3],[6,5,4],[7,8,9]])) # 1
print(s.minimumEffortPath([[10,8],
                           [10,8],
                           [1,2],
                           [10,3],
                           [1,3],
                           [6,3],
                           [5,2]])) # 6



