# my 
# Runtime: 8067 ms, faster than 50.00% of Python3
class Solution:
    def maxTrailingZeros(self, grid):
        
        @cache
        def cal_2(num):
            c = 0
            while num%2==0 :
                c += 1
                num = num//2
            return c
            
        @cache
        def cal_5(num):
            c = 0
            while num%5==0 :
                c += 1
                num = num//5
            return c
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                now_num = grid[i][j]
                grid[i][j] = (cal_2(now_num), cal_5(now_num))
        # print(grid)
        
        import numpy as np 
        cal = np.zeros( shape = (len(grid), len(grid[0]), 4) , dtype=list)
        # cal[i][j][方向]
        # 左邊到底
        for i in range(len(grid)):
            total = [0,0]
            for j in range(len(grid[0])):
                total[0] += grid[i][j][0]
                total[1] += grid[i][j][1]
                cal[i][j][0] = total.copy()
                
        # 右邊到底
        for i in range(len(grid)):
            total = [0,0]
            for j in reversed(range(len(grid[0]))):
                total[0] += grid[i][j][0]
                total[1] += grid[i][j][1]
                cal[i][j][2] = total.copy()
                
        # 上邊到底
        for j in range(len(grid[0])):
            total = [0,0]
            for i in range(len(grid)):
                total[0] += grid[i][j][0]
                total[1] += grid[i][j][1]
                cal[i][j][1] = total.copy()
                
        # 下邊到底
        for j in range(len(grid[0])):
            total = [0,0]
            for i in reversed(range(len(grid))):
                total[0] += grid[i][j][0]
                total[1] += grid[i][j][1]
                cal[i][j][3] = total.copy()
                
        # print(cal)
        
        # 轉角 i,j (四種組合)
        max_ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # print(cal[i][j][0][0])
                now_mem = cal[i][j]
                now_p = grid[i][j]
                max_ans = max(max_ans, min(now_mem[0][0]+now_mem[1][0]-now_p[0], now_mem[0][1]+now_mem[1][1]-now_p[1]))
                max_ans = max(max_ans, min(now_mem[1][0]+now_mem[2][0]-now_p[0], now_mem[1][1]+now_mem[2][1]-now_p[1]))
                max_ans = max(max_ans, min(now_mem[2][0]+now_mem[3][0]-now_p[0], now_mem[2][1]+now_mem[3][1]-now_p[1]))
                max_ans = max(max_ans, min(now_mem[3][0]+now_mem[0][0]-now_p[0], now_mem[3][1]+now_mem[0][1]-now_p[1]))
        return max_ans

# given ans 我看概念大家差不多 
# 頂多就 左右一起for 上下一起for
# 重複取位置的 就先存到變數裡面

s = Solution()
print(s.maxTrailingZeros(grid = [[23,17,15,3,20],[8,1,20,27,11],[9,4,6,2,21],[40,9,1,10,6],[22,7,4,5,3]]))
print(s.maxTrailingZeros(grid = [[4,3,2],[7,6,1],[8,8,8]]))



