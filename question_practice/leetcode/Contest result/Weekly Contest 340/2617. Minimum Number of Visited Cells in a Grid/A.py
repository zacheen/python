from typing import List
import functools
from collections import deque
import math
# my Time Limit Exceeded
class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        # BFS 
            # 1 <= m * n <= 10**5 所以 BFS 最多也就 10**5 次
            # 是因為支線太多 所以還是超出 Time Limit 嗎?
                # 因為我已經判斷只要做過就不會再重做了
        
        len_1D = len(grid)
        len_2D = len(grid[0])
        last_1D = len_1D-1
        last_2D = len_2D-1
        mem_len = [[math.inf]*len_2D for _ in range(len_1D)]
        next_p_list = deque([(0,0,1)])
        while next_p_list :
            # print(next_p_list)
            now_p_1D, now_p_2D, now_len = next_p_list.popleft()
            if now_p_1D == last_1D and now_p_2D == last_2D :
                return now_len

            if now_len >= mem_len[now_p_1D][now_p_2D] :
                continue

            # print("can go p :",now_p_1D,now_p_2D)
            mem_len[now_p_1D][now_p_2D] = now_len
            step = grid[now_p_1D][now_p_2D] +1 # +1 because I am using range
            for next_1D in range(now_p_1D+1, min(now_p_1D+step, len_1D)) :
                next_p_list.append((next_1D, now_p_2D, now_len+1))
            for next_2D in range(now_p_2D+1, min(now_p_2D+step, len_2D)) :
                next_p_list.append((now_p_1D, next_2D, now_len+1))

        return -1

# 如果提早判斷 會比較好嗎? (因為就不用一直 append) 
# 還是差不多，Time Limit Exceeded
class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        # BFS 
            # 1 <= m * n <= 10**5 所以 BFS 最多也就 10**5 次
            # 是因為支線太多 所以還是超出 Time Limit 嗎?
                # 因為我已經判斷只要做過就不會再重做了
        
        len_1D = len(grid)
        len_2D = len(grid[0])
        mem_len = [[math.inf]*len_2D for _ in range(len_1D)]
        next_p_list = deque([(0,0)])
        mem_len[0][0] = 1
        while next_p_list :
            # print(next_p_list)
            now_p_1D, now_p_2D = next_p_list.popleft()

            # print("can go p :",now_p_1D,now_p_2D)
            last_len = mem_len[now_p_1D][now_p_2D]
            step = grid[now_p_1D][now_p_2D] +1 # +1 because I am using range
            for next_1D in range(now_p_1D+1, min(now_p_1D+step, len_1D)) :
                if mem_len[next_1D][now_p_2D] == math.inf :
                    mem_len[next_1D][now_p_2D] = last_len + 1
                    next_p_list.append((next_1D, now_p_2D))
            for next_2D in range(now_p_2D+1, min(now_p_2D+step, len_2D)) :
                if mem_len[now_p_1D][next_2D] == math.inf :
                    mem_len[now_p_1D][next_2D] = last_len + 1
                    next_p_list.append((now_p_1D, next_2D))

        if mem_len[-1][-1] == math.inf:
            return -1
        else :
            return mem_len[-1][-1] 

# 按照 given ans 的想法重新實作 順便想優化
# 怎麼還是 Time Limit Exceeded ...
class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        len_1D = len(grid)
        last_1d = len_1D-1
        len_2D = len(grid[0])
        last_2d = len_2D-1
        candidate_result_1D_indx = [[x for x in range(len_1D)] for _ in range(len_2D)]
        # candidate_result_1D_indx[2D] 代表 2D 這一行剩下的候選 1D 點
        candidate_result_2D_indx = [[x for x in range(len_2D)] for _ in range(len_1D)]

        stack = [(0,0)]
        steps = 1
        while stack :
            new_stack = []
            # print(stack)
            for this_1D, this_2D in stack :
                if this_1D == last_1d and this_2D == last_2d :
                    return steps
                
                can_go_len = grid[this_1D][this_2D]
                max_1D = this_1D + can_go_len
                for can_1D in candidate_result_1D_indx[this_2D].copy() :
                    if can_1D > this_1D and can_1D <= max_1D :
                        candidate_result_1D_indx[this_2D].remove(can_1D)
                        candidate_result_2D_indx[can_1D].remove(this_2D)
                        new_stack.append((can_1D, this_2D))
                max_2D = this_2D + can_go_len
                for can_2D in candidate_result_2D_indx[this_1D].copy() :
                    if can_2D > this_2D and can_2D <= max_2D :
                        candidate_result_2D_indx[this_1D].remove(can_2D)
                        candidate_result_1D_indx[can_2D].remove(this_1D)
                        new_stack.append((this_1D, can_2D))
            stack = new_stack
            steps += 1
        return -1
      
# given ans
# 不是直接判斷長度可以走到哪裡，而是從後選可以走的選項 判斷候選的選項可不可以走
class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        pos1 = [[x for x in range(m)] for _ in range(n)]
        pos2 = [[x for x in range(n)] for _ in range(m)]
        # print(pos1, pos2)
        dis = [[-1]*m for _ in range(n)]
        dis[0][0]=1
        q = deque()
        def add_to_queue(i,j) :
            # print("add_to_queue", i, j)
            # print(pos1, pos2)
            pos1[i].remove(j)
            pos2[j].remove(i)
            q.append((i,j))
        add_to_queue(0,0)
        while q :
            i,j = q.popleft()
            # print(q , pos1[i] , i, j)
            for it in pos1[i].copy() :
                # print("for",it, min(pos1[i]))
                if it<=j+grid[i][j] :
                    dis[i][it]=dis[i][j]+1
                    add_to_queue(i,it)
                    continue
                break
            for it in pos2[j].copy() :
                if it<=i+grid[i][j] :
                    dis[it][j]=dis[i][j]+1
                    add_to_queue(it,j)
                    continue
                break
        return dis[n-1][m-1]


s = Solution()
# print(s.minimumVisitedCells([[3,4,2,1],[4,2,3,1],[2,1,0,0],[2,4,0,0]]))
# print(s.minimumVisitedCells([[3,4,2,1],[4,2,1,1],[2,1,1,0],[3,4,1,0]]))
# print(s.minimumVisitedCells([[2,1,0],[1,0,0]]))
# print(s.minimumVisitedCells([[6,4,8],[7,3,2],[2,1,11],[8,13,12],[4,3,0]]))
print(s.minimumVisitedCells([[1,5,0,0,0,0,1,1,1,0]]))



