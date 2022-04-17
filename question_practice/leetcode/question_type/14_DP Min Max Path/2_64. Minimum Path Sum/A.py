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

s = Solution()
print(s.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
print(s.minPathSum([[1,2,3],[4,5,6]]))



