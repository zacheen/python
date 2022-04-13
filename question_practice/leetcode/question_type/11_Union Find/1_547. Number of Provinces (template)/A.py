# my 

# given ans
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
    def findCircleNum(self, M):
        n = len(M)
        uf = UF(n)

        for i in range(n):
            for j in range(i, n):
                if M[i][j] == 1:
                    uf.union(i, j)

        return uf.count



s = Solution()
print(s.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))



