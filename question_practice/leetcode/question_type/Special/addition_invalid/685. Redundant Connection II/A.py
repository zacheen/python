# 685. Redundant Connection II
# https://leetcode.com/problems/redundant-connection-ii/description/
    # after remove, must be a tree

# my : 1ms Beats82.75%
from typing import List
class UF:
    def __init__(self, n):
        self.id = list(range(n))

    def union(self, u, v):
        i = self.find(u)
        j = self.find(v)
        if i == j:
            return True
        self.id[i] = j
        return False

    def find(self, u):
        if self.id[u] != u:
            self.id[u] = self.find(self.id[u])
        return self.id[u]

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        len_n = len(edges) + 1
        links = [[] for _ in range(len_n)]
        for n1,n2 in edges :
            links[n1].append(n2)

        # invalid 有兩種情況
            # 1. 兩個點匯集到同一個點
            # 2. 形成 cycle

        # 找 root找 root
        def find_top(links, len_n):
            seen_set = set(n2 for n1,n2 in links)
            return set([i for i in range(len_n)]) - seen_set
        root = find_top(edges, len_n)
        root.remove(0)
        if len(root) == 0 :
            # 如果找不到 root 代表有環
            uf = UF(len(edges)+1)
            for n1,n2 in edges :
                if uf.union(n1,n2) :
                    return (n1,n2)
        
        # 其他可能就是 DFS 會走到同一點 (包含 cycle 跟 匯到同個點)
        root = list(root)[0]
        seen = set()
        def dfs(n):
            if n in seen :
                if n in path : # cycle
                    return [path[-1], n]
                else : # 匯到同個點
                    # 找出比較後面的 link
                    for n1,n2 in edges[::-1] :
                        if n2 == n :
                            return [n1,n2]
            else :
                seen.add(n)
                path.append(n)
                for next_p in links[n] :
                    ret = dfs(next_p)
                    if ret != None :
                        return ret
                path.pop()
            return None
        path = []
        return dfs(root)

# given ans : 0ms
class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        def find(x: int) -> int:
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        n = len(edges)
        in_d = [0] * n
        for _, v in edges:
            in_d[v - 1] += 1
        poss_ans_indx = [i for i, (_, v) in enumerate(edges) if in_d[v - 1] == 2]

        p = list(range(n))
        if poss_ans_indx: # 如果有 in_d == 2 的情況 : 一定屬於 "DFS 會走到同一點"
            for i, (u, v) in enumerate(edges):
                if i == poss_ans_indx[1]:
                    continue
                pu, pv = find(u - 1), find(v - 1)
                if pu == pv:
                    return edges[poss_ans_indx[0]]
                p[pu] = pv
            return edges[poss_ans_indx[1]]
            # 如果我排除比較後面的 Link 卻是 valid : 後面的 Link 才是問題
            # 如果排除兩個都會變成 valid : 這樣才會回傳後面的
        else :
            for i, (u, v) in enumerate(edges):
                pu, pv = find(u - 1), find(v - 1)
                if pu == pv:
                    return edges[i]
                p[pu] = pv

s = Solution()
print("ans :",s.findRedundantDirectedConnection([[1,2],[1,3],[2,3]])) # [2,3]
print("ans :",s.findRedundantDirectedConnection([[1,2],[2,3],[3,4],[4,1],[1,5]])) # [4,1] 
print("ans :",s.findRedundantDirectedConnection([[2,1],[3,1],[4,2],[1,4]])) # [2,1]
# print("ans :",s.findRedundantDirectedConnection()) # 



