# 547. Number of Provinces
# https://leetcode.com/problems/number-of-provinces/description/

# my 3ms Beats90.07%
class UF:
    def __init__(self, n):
        self.count = n
        self.id = list(range(n))

    def union(self, u, v):
        i = self.find(u)
        j = self.find(v)
        if i == j:
            return
        self.id[i] = j
        self.count -= 1

    def find(self, u):
        if self.id[u] != u:
            self.id[u] = self.find(self.id[u])
        return self.id[u]

class Solution:
    def findCircleNum(self, isConnected):
        n_len = len(isConnected)
        uf = UF(n_len)
        for n1 in range(n_len) :
            for n2 in range(n1+1, n_len) :
                if isConnected[n1][n2] :
                    uf.union(n1,n2)
        return uf.count

s = Solution()
# M[i][j] 代表 點i與點j有相連
# 請問總共有幾區 (若兩點之前有相連代表是同一區)
print(s.findCircleNum(M = [[1,1,0],[1,1,0],[0,0,1]]))
print(s.findCircleNum(M = [[1,0,0],[0,1,0],[0,0,1]]))



