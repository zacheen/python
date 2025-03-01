# 2050. Parallel Courses III
# https://leetcode.com/problems/parallel-courses-iii/description/

from typing import List
from math import inf

# my 97ms Beats99.07%
class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        deg = [0] * n
        li = [[] for _ in range(n)]
        for n1,n2 in relations:
            n1 -= 1
            n2 -= 1
            deg[n2] += 1  # 統計基環樹每個節點的入度
            li[n1].append(n2)
        end_point = [i for i, d in enumerate(deg) if d == 0]
        mem_time = [0]*n
        while end_point:  # 拓樸排序，剪掉圖上所有樹枝
            now_n = end_point.pop()
            min_time = mem_time[now_n] + time[now_n]
            mem_time[now_n] = min_time
            for nei_n in li[now_n] :
                deg[nei_n] -= 1
                if min_time > mem_time[nei_n] :
                    mem_time[nei_n] = min_time
                if deg[nei_n] == 0:
                    end_point.append(nei_n)
        # print(mem_time)
        return max(mem_time)

s = Solution()
print("ans :",s.minimumTime(n = 3, relations = [[1,3],[2,3]], time = [3,2,5])) # 8
print("ans :",s.minimumTime(n = 5, relations = [[1,5],[2,5],[3,5],[3,4],[4,5]], time = [1,2,3,4,5])) # 12



