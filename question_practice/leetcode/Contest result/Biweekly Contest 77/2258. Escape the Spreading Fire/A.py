# my 卡在火跟人同時到 這樣是算可以的
# 我猜很多人 交第一次是錯的 就是因為這個
# 但我不想再重新實作 下面的邏輯應該是對的
# 我應該是要先算人可以到的地方
# 判斷有沒有到終點
# 再扣掉火燒到的位置
# class Solution:
#     def maximumMinutes(self, grid):
#         import copy
        
#         len_i = len(grid)
#         len_ii = len(grid[0])
        
#         new_fire = []
#         for i in range(len_i) :
#             for ii in range(len_ii) :
#                 if grid[i][ii] == 1:
#                     new_fire.append((i,ii))
                
#         grid_mem = [copy.deepcopy(grid)]
#         direction = [(0,1),(1,0),(0,-1),(-1,0)]
#         reach_end = False
#         def get_grid_mem(t):
#             nonlocal new_fire
#             while len(new_fire) != 0 and len(grid_mem) <= t:
#                 # print("in loop")
#                 temp_new_fire = []
#                 for fi_x,fi_y in new_fire :
#                     dir_x = fi_x+1
#                     if dir_x < len_i and grid[dir_x][fi_y] == 0:
#                         grid[dir_x][fi_y] = 1
#                         temp_new_fire.append((dir_x,fi_y))
#                     dir_y = fi_y+1
#                     if dir_y < len_ii and grid[fi_x][dir_y] == 0:
#                         grid[fi_x][dir_y] = 1
#                         temp_new_fire.append((fi_x,dir_y))
#                     dir_x = fi_x-1
#                     if dir_x >= 0 and grid[dir_x][fi_y] == 0:
#                         grid[dir_x][fi_y] = 1
#                         temp_new_fire.append((dir_x,fi_y))
#                     dir_y = fi_y-1
#                     if dir_y >= 0 and grid[fi_x][dir_y] == 0:
#                         grid[fi_x][dir_y] = 1
#                         temp_new_fire.append((fi_x,dir_y))
                
#                 if len(temp_new_fire) == 0 :
#                     break
#                 new_fire = temp_new_fire
#                 # print(new_fire)
#                 grid_mem.append(copy.deepcopy(grid))
                        
#             if len(grid_mem) > t :
#                 return grid_mem[t]
#             else :
#                 nonlocal reach_end
#                 reach_end = True
#                 return grid_mem[-1] # 代表這個秒數後 火就不會再變多了
            
#         # 從第幾秒開始跑 回傳能不能到
#         end_point = (len_i-1, len_ii-1)
#         def bfs(t) :
#             reach_before = []
#             can_reach = {(0,0)}
            
#             while len(can_reach) != 0 :
#                 if end_point in can_reach:
#                     return True
#                 t += 1
#                 temp_new_reach = set()
#                 grid_me = get_grid_mem(t)
#                 for px,py in can_reach :
#                     dir_x = px+1
#                     if dir_x < len_i  and grid_me[dir_x][py] == 0 and (dir_x,py) not in reach_before:
#                         temp_new_reach.add((dir_x,py))
#                     dir_y = py+1
#                     if dir_y < len_ii and grid_me[px][dir_y] == 0 and (dir_x,py) not in reach_before:
#                         temp_new_reach.add((px,dir_y))
#                     dir_x = px-1
#                     if dir_x >= 0 and grid_me[dir_x][py] == 0 and (dir_x,py) not in reach_before:
#                         temp_new_reach.add((dir_x,py))
#                     dir_y = py-1
#                     if dir_y >= 0 and grid_me[px][dir_y] == 0 and (dir_x,py) not in reach_before:
#                         temp_new_reach.add((px,dir_y))
#                     # 如果往下或往右走是終點
#                     # if ((px,py+1) == end_point or (px+1,py) == end_point) and grid_me[px][py] == 0 :
#                     #     return True
#                 can_reach = temp_new_reach
            
#             return False
        
#         # print(bfs(0))
#         # print(bfs(1))
#         # print(bfs(2))
#         # print(bfs(3))
#         # print(bfs(4))
                
#         # binary 看有沒有路

#         left, right = 0, 20000
#         # left right 不會碰到
#         while left + 1 < right:
#             mid = (left + right) // 2
#             # 這裡我移除 少一次判斷
#             # if nums[mid] == target:
#             #     return mid
#             if bfs(mid):
#                 left = mid
#             else:
#                 right = mid

#             if reach_end :
#                 right = min(right, len(grid_mem))

#         # print(left, right)
#         # print("bfs(0)",bfs(0))
#         if bfs(right) :
#             if right == len(grid_mem) :
#                 return 1000000000
#             else :
#                 return right
#         elif bfs(left) :
#             return left
#         else :
#             return -1

import collections
# given ans
# 跟我的想法差不多 只是不是每秒記錄一張 而是使用數字代替現在會燒到哪裡
class Solution:
    def maximumMinutes(self, grid):
        left = 0
        right = 1000000000

        R = len(grid)
        C = len(grid[0])
        INF = 10 ** 20
        
        q = collections.deque()
        dist = [[INF] * C for _ in range(R)]
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    dist[i][j] = 0
                    q.append((0, i, j))
        
        while len(q) > 0:
            d, x, y = q.popleft()
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < R and 0 <= ny < C and dist[nx][ny] == INF and grid[nx][ny] != 2:
                    dist[nx][ny] = d + 1
                    q.append((d + 1, nx, ny))
        
        def good(target):
            q = collections.deque()
            d2 = [[INF] * C for _ in range(R)]
            
            if dist[0][0] <= target:
                return False
            
            q.append((target, 0, 0))
            
            while len(q) > 0:
                d, x, y = q.popleft()
                #print(target, x, y, d)
                
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    
                    if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] != 2 and d2[nx][ny] == INF and d + 1 < dist[nx][ny]:
                        d2[nx][ny] = d + 1
                        q.append((d + 1, nx, ny))

                        if nx == R - 1 and ny == C - 1:
                            return True
                        
                    if nx == R - 1 and ny == C - 1 and grid[nx][ny] != 2 and d2[nx][ny] == INF and d + 1 <= dist[nx][ny]:
                        return True
            return False
        
        while left < right:
            mid = (left + right + 1) // 2
            
            if good(mid):
                left = mid
            else:
                right = mid - 1
            
        if left == 0:
            if good(0):
                return 0
            else:
                return -1
        return left


s = Solution()
# print(s.maximumMinutes([[0,2,0,0,0,0,0],
#                         [0,0,0,2,2,1,0],
#                         [0,2,0,0,1,2,0],
#                         [0,0,2,2,2,0,2],
#                         [0,0,0,0,0,0,0]]))
# print(s.maximumMinutes([[0,0,0,0],
#                         [0,1,2,0],
#                         [0,2,0,0]]))
# print(s.maximumMinutes([[0,0,0],
#                         [2,2,0],
#                         [1,2,0]]))

# 如果同時到 房子是算可以的
print(s.maximumMinutes([[0,2,0,0,1],
                        [0,2,0,2,2],
                        [0,2,0,0,0],
                        [0,0,2,2,0],
                        [0,0,0,0,0]]))
