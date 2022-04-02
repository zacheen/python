# my 思考不夠完整 fail
# import numpy as np
# class Solution:
#     def pacificAtlantic(self, heights):
#         ans = []
#         y_len = len(heights[0])
#         res = np.zeros( shape = (len(heights), y_len) , dtype=int ) 
#         res[0][y_len] = 2
#         ans.append((0,y_len))
#         res[len(heights)][0] = 2
#         ans.append((len(heights),0))
#         # res :
#             # 1 代表走過失敗
#             # 2 代表走過成功

#         # 四個方向 如果比較低就可以往前走 
#         # 遇到死掉的格子 也會跟著死掉
#         # 直到抵達 對岸 ( <0 或 >len )
#         his = []
#         way_BL = True  # 這個是往右下角(Bottom Left)的方向找路
#         def find_way(x, y):
#             if (x, y) in his :
#                 return False
#             if way_BL :
#                 if x >= len(heights) or y >= y_len :
#                     return True
#             if res[x][y] == 1 :
#                 return False
#             if res[x][y] == 2 :
#                 return True

#             his.append((x, y))
#             now_height = heights[x][y]
#             ret = False
#             if (x+1)<len(grid) and now_height >= grid[x+1][y]:
#                 if find_way(x+1,y) : ret = True
#             if (y+1) < y_len and now_height >= grid[x][y+1]:
#                 if find_way(x,y+1) : ret = True
#             if (x-1) >= 0 and now_height >= grid[x-1][y]:
#                 if find_way(x-1,y) : ret = True
#             if (y-1) >= 0 and now_height >= grid[x][y-1]:
#                 if find_way(x,y-1) : ret = True
#             return ret

#         ans = []
#         for i in range(len(heights)) :
#             if find_way(0, i) :
#                 for e_x, e_y in his :
#                     res[x][y] = 1
#                     ans = ans + his
#             else :
#                 for e_x, e_y in his :
#                     res[x][y] = 2
#         return ans

# my 想法2
# 如過不行就紀錄
# 如果可以就 DFS 找高點紀錄

# given ans
# 從左上各點 找尋各點連接的最高點
# 從右下再做一次
# 重疊的部分代表 從左上或右下都可以到達
class Solution:
    def pacificAtlantic(self, heights):
        m = len(heights)
        n = len(heights[0])
        seenP = [[False] * n for _ in range(m)]
        seenA = [[False] * n for _ in range(m)]

        def dfs(i, j, h, seen):
            if i < 0 or i == m or j < 0 or j == n:
                return
            if seen[i][j] or heights[i][j] < h:
                return

            seen[i][j] = True
            dfs(i + 1, j, heights[i][j], seen)
            dfs(i - 1, j, heights[i][j], seen)
            dfs(i, j + 1, heights[i][j], seen)
            dfs(i, j - 1, heights[i][j], seen)

        for i in range(m):
            dfs(i, 0, 0, seenP)
            dfs(i, n - 1, 0, seenA)

        for j in range(n):
            dfs(0, j, 0, seenP)
            dfs(m - 1, j, 0, seenA)

        return [[i, j]
                for i in range(m)
                for j in range(n)
                if seenP[i][j] and seenA[i][j]]

s = Solution()
heights = [[1,2,2,3,5],
           [3,2,3,4,4],
           [2,4,5,3,1],
           [6,7,1,4,5],
           [5,1,1,2,4]]
print(s.pacificAtlantic(heights))



