# my Runtime: 882 ms, faster than 44.22% of Python3
# from collections import deque
# class Solution:
#     def shortestPathBinaryMatrix(self, grid):
        
#         # quick and corner case 
#         if grid[-1][-1] == 1 :
#             return -1
        
#         # BFS 因為每走一步都是長度1 所以BFS的每一步一定都是最短的
#         directions = [(1,1),(1,-1),(-1,1),(-1,-1),(0,1),(1,0),(0,-1),(-1,0)]
        
#         can_reach = deque()
#         can_reach.append((0,0,1))
#         mem = [[math.inf]*len(grid[0]) for _ in range(len(grid))]
        
#         bound_x, bound_y = len(grid)-1, len(grid[0])-1
#         while can_reach :
#             x, y, now_len = can_reach.popleft()
            
#             # 判斷底
#             if bound_x == x and bound_y == y :
#                 return now_len
            
#             if x >= 0 and x <= bound_x and y >= 0 and y <= bound_y :
#                 if grid[x][y] != 1 and now_len < mem[x][y] :
#                     mem[x][y] = now_len
#                     # 往八個方向
#                     now_len += 1
                    
#                     for d_x, d_y in directions :
#                         can_reach.append((x+d_x, y+d_y, now_len))
        
#         return -1

# given ans
# 真的是 BFS 所以不用創建 mem 紀錄每個位置的 長度
# 真的比較快
# Runtime: 656 ms, faster than 81.58% of Python3 
class Solution:
    def shortestPathBinaryMatrix(self, grid):
        
        # quick and corner case 
        if grid[-1][-1] == 1 :
            return -1
        
        # BFS 因為每走一步都是長度1 所以BFS的每一步一定都是最短的
        directions = [(1,1),(1,-1),(-1,1),(-1,-1),(0,1),(1,0),(0,-1),(-1,0)]
        
        can_reach = []
        can_reach.append((0,0))
        not_seen = [[True]*len(grid[0]) for _ in range(len(grid))]
        
        bound_x, bound_y = len(grid)-1, len(grid[0])-1
        now_len = 0
        while can_reach :
            now_len += 1
            new_can_reach = []
            for x, y in can_reach :
                # 判斷底
                if bound_x == x and bound_y == y :
                    return now_len
                
                if x >= 0 and x <= bound_x and y >= 0 and y <= bound_y :
                    if grid[x][y] != 1 and not_seen[x][y] :
                        not_seen[x][y] = False
                        # 往八個方向
                        for d_x, d_y in directions :
                            new_can_reach.append((x+d_x, y+d_y))
            can_reach = new_can_reach
        return -1



s = Solution()
print(s.shortestPathBinaryMatrix([[0,1],[1,0]]))  # 2
print(s.shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]])) # 4
print(s.shortestPathBinaryMatrix([[1,0,0],[1,1,0],[1,1,0]])) # -1
print(s.shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,1]])) # -1



