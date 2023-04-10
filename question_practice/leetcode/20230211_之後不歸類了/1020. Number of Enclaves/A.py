# my Beats 75.7%
class Solution:
    def numEnclaves(self, grid):
        max_col = len(grid)   -1
        max_row = len(grid[0])-1
        
        dir = [1,0,-1,0,1]
        def dfs(i,j) :
            nonlocal grid
            if i < 0 or i > max_col or j < 0 or j > max_row :
                return 
            
            # print(i,j)
            if grid[i][j] == 1 :
                # print(i,j,"go")
                grid[i][j] = 2
                # 走四邊
                for d in range(4) :
                    # print("dir", dir[d], dir[d+1])
                    dfs(i+dir[d], j+dir[d+1])
            return

        for i in range(len(grid)):
            dfs(i,0)
            dfs(i,max_row)
        for i in range(len(grid[0])):
            dfs(0,i)
            dfs(max_col,i)
        
        # print(grid)
        # count 1 number
        return sum(g.count(1) for g in grid)

# given ans
# 想法一樣

s = Solution()
print(s.numEnclaves([[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]))
print(s.numEnclaves([[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]))
print(s.numEnclaves(
    [[0,1,0,0,1,0,1,1,1,1,1,0,0,1],
     [1,1,0,0,1,0,0,1,0,0,1,0,1,0],
     [1,1,1,0,0,0,1,1,0,0,1,1,1,1],
     [1,0,0,1,0,0,1,1,1,0,0,1,0,0],
     [0,1,0,0,1,0,0,0,1,1,1,0,0,1],
     [1,1,1,1,1,0,0,0,0,0,0,1,1,1],
     [0,1,1,0,0,1,0,0,1,1,0,0,1,0],
     [0,1,0,1,0,1,1,0,1,0,0,1,0,0],
     [1,0,0,1,1,0,0,0,0,1,1,0,0,1],
     [1,0,0,0,0,1,0,1,0,1,0,0,0,0]]
))

    # [[0,1,0,0,1,0,1,1,1,1,1,0,0,1],
    #  [1,1,0,0,1,0,0,1,0,0,1,0,1,0],
    #  [1,1,1,0,0,0,1,1,0,0,1,1,1,1],
    #  [1,0,0,X,0,0,1,1,1,0,0,1,0,0],
    #  [0,1,0,0,X,0,0,0,1,1,1,0,0,1],
    #  [1,1,1,1,1,0,0,0,0,0,0,1,1,1],
    #  [0,1,1,0,0,X,0,0,X,X,0,0,1,0],
    #  [0,1,0,1,0,X,X,0,X,0,0,1,0,0],
    #  [1,0,0,1,1,0,0,0,0,1,1,0,0,1],
    #  [1,0,0,0,0,1,0,1,0,1,0,0,0,0]]



