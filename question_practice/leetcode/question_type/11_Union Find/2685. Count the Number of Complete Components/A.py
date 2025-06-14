# 2685. Count the Number of Complete Components
# https://leetcode.com/problems/count-the-number-of-complete-components

from typing import List
from math import inf

# my 48ms Beats59.46%
class UF_each_set_count:
    def __init__(self, n):
        self.id = list(range(n))
        self.set_member = [1]*n     # <計算各個 set 的個數> 多的
        self.edge_cou = [0]*n

    def union(self, u, v):
        i = self.find(u)
        j = self.find(v)
        self.edge_cou[j] += 1
        if i == j:
            return
        self.edge_cou[j] += self.edge_cou[i]
        # self.edge_cou[i] = 0
        self.set_member[j] += self.set_member[i]  # <計算各個 set 的個數> 多的
        self.set_member[i] = 0                    # 0 代表被合併了 (非必要)
        self.id[i] = j 

    def find(self, up):
        while (up:=self.id[up]) != (deep:=self.id[up]):
            self.id[up] = self.id[deep]
        return up


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UF_each_set_count(n)
        for n1,n2 in edges:
            uf.union(n1,n2)
        
        ans = 0
        for num, e_num in zip(uf.set_member, uf.edge_cou):
            if num > 0 and e_num == (num*(num-1))//2 :
                ans += 1
        return ans

# inspire by given ans : 32ms Beats91.01%
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        li = [[] for _ in range(n)]

        # build
        degree = [0]*n
        for n1,n2 in edges :
            li[n1].append(n2)
            li[n2].append(n1)
            degree[n1] += 1
            degree[n2] += 1
        
        visited = [False]*n
        def dfs(now_n, edge_cou):
            ret_cou = 1
            visited[now_n] = True
            for next_n in li[now_n] :
                if visited[next_n] : 
                    continue
                ret = dfs(next_n, edge_cou)
                if ret_cou == 0 or ret == 0 or (degree[next_n] != edge_cou) :
                    ret_cou = 0
                else :
                    ret_cou += ret
            return ret_cou

        ans = 0
        for st in range(n):
            if not visited[st] :
                ret = dfs(st, degree[st])
                if (ret-1) == degree[st] :
                    ans += 1
        return ans


s = Solution()
print("ans :",s.countCompleteComponents(n = 6, edges = [[0,1],[0,2],[1,2],[3,4]])) # 3
print("ans :",s.countCompleteComponents(n = 6, edges = [[0,1],[0,2],[1,2],[3,4],[3,5]])) # 1
print("ans :",s.countCompleteComponents(n = 5, edges = [[2,0],[3,1],[4,2],[4,3]])) # 1
print("ans :",s.countCompleteComponents(n = 5, edges = [[1,0],[2,0],[3,0],[4,2],[4,3]])) # 1



