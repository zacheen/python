# my Runtime: 98 ms, faster than 94.57% of Python3
class Solution:
    def minPathSum(self, grid):
        
        for i in range(1,len(grid)):
            grid[i][0] += grid[i-1][0]
        # print(grid)  
        # print("i:",i) # 這個時候i竟然還可以用...
        for j in range(1,len(grid[0])):
            grid[0][j] += grid[0][j-1]
        # print(grid)

        for i in range(1,len(grid)):
            for j in range(1,len(grid[0])):
                grid[i][j] = grid[i][j] + min(grid[i-1][j], grid[i][j-1])
        
        # print(grid)
        return grid[-1][-1]

# given ans 一樣 只是是在for裡面處理邊界的問題

# 20230327 再次練習 Beats 92.44%

class Solution:
    def minPathSum(self, grid):

        width = len(grid[0])
        height = len(grid)

        for w in range(width) :
            for h in range(height) :
                if h == 0 :
                    if w != 0 :
                        grid[h][w] = grid[h][w-1] + grid[h][w]
                elif w == 0 :
                    grid[h][w] = grid[h-1][w] + grid[h][w]
                else :
                    grid[h][w] = min(grid[h-1][w], grid[h][w-1]) + grid[h][w]

        # print(grid)
        return grid[height-1][width-1]

s = Solution()
print(s.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
print(s.minPathSum([[1,2,3],[4,5,6]]))



