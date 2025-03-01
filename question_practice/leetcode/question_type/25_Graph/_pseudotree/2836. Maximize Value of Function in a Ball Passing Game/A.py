# 2836. Maximize Value of Function in a Ball Passing Game
# https://leetcode.com/problems/maximize-value-of-function-in-a-ball-passing-game/description/

from typing import List
from math import inf
from collections import deque

# # my 239ms Beats82.50%
class Solution:
    def getMaxFunctionValue(self, receiver: List[int], k: int) -> int:
        max_ans = 0
        len_n = receiver
        deg = [0] * len_n
        for n2 in receiver:
            deg[n2] += 1  # 統計基環樹每個節點的入度
        end_point = [i for i, d in enumerate(deg) if d == 0]
        mem_path = {}
        timeVisited = [0] * len_n
        while end_point:  # 拓樸排序，剪掉圖上所有樹枝
            now_n = end_point.pop()
            timeVisited[now_n] = 1
            if now_n in mem_path :
                path = mem_path[now_n]
                del(mem_path[now_n])
                for i in range(len(path)) :
                    path[i] += now_n
            else :
                path = deque([])
            path.appendleft(now_n)
            _ = ""

            nei_n = receiver[now_n]
            # compare path
            if nei_n in mem_path :
                pre_path = mem_path[nei_n]
                for i, (pre, new) in enumerate(zip(pre_path, path)) :
                    if new > pre :
                        pre_path[i] = new
                if len(path) > len(pre_path) :
                    mem_path[nei_n] += path[len(pre_path):]
            else :
                mem_path[nei_n] = path
            _ = ""

            deg[nei_n] -= 1
            if deg[nei_n] == 0:
                end_point.append(nei_n)
                if len(mem_path[nei_n]) > k :
                    max_ans = max(max_ans, mem_path[nei_n][-1]-mem_path[nei_n].pop())
                else :
                    max_ans = max(max_ans, mem_path[nei_n][-1])
            _ = ""

        ret = []
        time = 2
        
        for now_n in range(len_n):
            if timeVisited[now_n]:
                continue
            startTime = time
            path = []
            for _ in range() :
                
            while now_n != -1 and not timeVisited[now_n]:
                timeVisited[now_n] = time
                path.append(now_n)
                time += 1
                now_n = edges[now_n]  # Move to next node
            if now_n != -1 and timeVisited[now_n] >= startTime:
                ret.append((time - timeVisited[now_n], now_n))



s = Solution()
print("ans :",s.getMaxFunctionValue(receiver = [2,0,1], k = 4)) # [3,3,3,4]
print("ans :",s.getMaxFunctionValue(receiver = [1,1,1,2,3], k = 3)) # [5,5,5,5,5]
