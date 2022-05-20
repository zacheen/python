# my Runtime: 466 ms, faster than 85.58% of Python3
# DP + DFS
class Solution:
    def longestIncreasingPath(self, matrix):
        
        # 每個點做 DFS 
        # 如果做過了就跳過
        # 如果可以就接上
        
        x_bound = len(matrix)
        y_bound = len(matrix[0])
        
        mem_len = [[0]*y_bound for _ in range(x_bound)]
        # 這個用 numpy 初始化會不會比較快阿
        
        direction = [1,0,-1,0,1]
        def dfs(x, y) :
            if mem_len[x][y] != 0 :
                return mem_len[x][y]
            
            max_len = 0
            now_num = matrix[x][y]
            for i in range(4) :
                next_x = x+direction[i]
                next_y = y+direction[i+1]
                # 突然想到應該是 matrix 加上周圍 
                # 如果是周圍就不繼續
                if next_x < 0 or next_x >= x_bound or next_y < 0 or next_y >= y_bound :
                    continue
                if now_num > matrix[next_x][next_y] :
                    max_len = max(max_len, dfs(next_x, next_y))
                    
            # 加上自己的長度 順便變成紀錄已經走過了
            max_len += 1
            mem_len[x][y] = max_len
            return max_len
        
        ans = 0
        for i in range(x_bound) :
            for ii in range(y_bound) :
                ans = max(ans, dfs(i, ii))
        return ans
                

# given ans 觀念一樣
    # 優化
    # 此位置跟上一個位置比較 (O)
    # 我是 此位置 跟上下左右比較

# class Solution:
#     def longestIncreasingPath(self, matrix):    
#         m = len(matrix)
#         n = len(matrix[0])

#         @lru_cache(None)
#         def dfs(i: int, j: int, prev: int) -> int:
#             if i < 0 or i == m or j < 0 or j == n:
#                 return 0
#             if matrix[i][j] <= prev:
#                 return 0

#             curr = matrix[i][j]
#             return 1 + max(dfs(i + 1, j, curr),
#                             dfs(i - 1, j, curr),
#                             dfs(i, j + 1, curr),
#                             dfs(i, j - 1, curr))

#         return max(dfs(i, j, -math.inf) for i in range(m) for j in range(n))

s = Solution()
print(s.longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]])) # 4 # [1, 2, 6, 9]



