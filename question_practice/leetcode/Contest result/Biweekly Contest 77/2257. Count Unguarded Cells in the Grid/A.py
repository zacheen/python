# my 3298 ms
# 我是以每一個 guards 看四方
# class Solution:
#     def countUnguarded(self, m, n, guards, walls):
        
#         mem = [[None]*n for _ in range(m)]
        
#         for w in walls :
#             mem[w[0]][w[1]] = "w"
            
#         for g in guards :
#             mem[g[0]][g[1]] = "g"
            
#         for g in guards :
#             gx = g[0]
#             gy = g[1]
            
#             now_gx = gx + 1
#             now_gy = gy
#             while now_gx < m :
#                 if mem[now_gx][now_gy] == "w" or mem[now_gx][now_gy] == "g":
#                     break
#                 mem[now_gx][now_gy] = "s" # 看過
#                 now_gx += 1
                
#             now_gx = gx
#             now_gy = gy + 1
#             while now_gy < n :
#                 if mem[now_gx][now_gy] == "w" or mem[now_gx][now_gy] == "g" :
#                     break
#                 mem[now_gx][now_gy] = "s" # 看過
#                 now_gy += 1
                
#             now_gx = gx - 1
#             now_gy = gy
#             while now_gx >= 0 :
#                 if mem[now_gx][now_gy] == "w" or mem[now_gx][now_gy] == "g" :
#                     break
#                 mem[now_gx][now_gy] = "s" # 看過
#                 now_gx -= 1
                
#             now_gx = gx
#             now_gy = gy - 1
#             while now_gy >= 0 :
#                 if mem[now_gx][now_gy] == "w" or mem[now_gx][now_gy] == "g" :
#                     break
#                 mem[now_gx][now_gy] = "s" # 看過
#                 now_gy -= 1
                
                
#         # print(mem)
#         ans = 0
#         for i in range(m):
#             for ii in range(n):
#                 if mem[i][ii] == None :
#                     ans += 1
#         return ans

# given ans
# Runtime: 2718 ms, faster than 88.19% of Python3
# 判斷有沒有人看的方式不一樣
# 一行一行掃 可以想成這一個某個方向有沒有 G
# flag 用來記錄現在有沒有人看
# 遇到 G 就改成可以看到 遇到 W 就改成看不到
# G 0 W 0 G
# 1 1 0 0 1 如果從左往右掃 
class Solution:
    def countUnguarded(self, R, C, guards, walls):
        state = [[0] * C for _ in range(R)]
        
        GUARD = 1
        WALL = 2
        USED = 3
        for x, y in guards:
            state[x][y] = GUARD
            
        for x, y in walls:
            state[x][y] = WALL

        for i in range(R):
            current = 0
            for j in range(C):
                if state[i][j] == GUARD:
                    current = USED
                elif state[i][j] == WALL:
                    current = 0
                elif state[i][j] == 0:
                    if current == USED:
                        state[i][j] = USED
        
        for i in range(R):
            current = 0
            for j in range(C - 1, -1, -1):
                if state[i][j] == GUARD:
                    current = USED
                elif state[i][j] == WALL:
                    current = 0
                elif state[i][j] == 0:
                    if current == USED:
                        state[i][j] = USED
                
        for j in range(C):
            current = 0
            for i in range(R):
                if state[i][j] == GUARD:
                    current = USED
                elif state[i][j] == WALL:
                    current = 0
                elif state[i][j] == 0:
                    if current == USED:
                        state[i][j] = USED

        for j in range(C):
            current = 0
            for i in range(R - 1, -1, -1):
                if state[i][j] == GUARD:
                    current = USED
                elif state[i][j] == WALL:
                    current = 0
                elif state[i][j] == 0:
                    if current == USED:
                        state[i][j] = USED

        count = 0
        for i in range(R):
            for j in range(C):
                if state[i][j] == 0:
                    count += 1
        return count

s = Solution()
print(s.countUnguarded(m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]]))



