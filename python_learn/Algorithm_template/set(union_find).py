# union 是用來
    # 看說兩點之間有沒有關係
    # 沒關係的區域共有幾個 (有count版本)

# 無count版本
class UF:
    def __init__(self, n):
        self.id = list(range(n))

    def union(self, u, v):
        i = self.find(u)
        j = self.find(v)
        if i == j:
            return
        self.id[i] = j

    def find(self, u):
        if self.id[u] != u:
            self.id[u] = self.find(self.id[u])
        return self.id[u]

# 有count版本
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

        # 加入連結
        for i in range(n):
            for j in range(i, n):
                if M[i][j] == 1:
                    uf.union(i, j)

        return uf.count
# M[i][j] 代表 點i與點j有相連
# 請問總共有幾區 (若兩點之前有相連代表是同一區)
s = Solution()
print(s.findCircleNum(M = [[1,1,0],[1,1,0],[0,0,1]]))
print(s.findCircleNum(M = [[1,0,0],[0,1,0],[0,0,1]]))

# 解釋 --------------------------------------------

class UF:
    def __init__(self, n):
        self.count = n
        self.id = list(range(n))

    def union(self, u, v):
        i = self.find(u)
        j = self.find(v)
        if i == j:
            return
        # 如果不一樣的tree 就合併此兩個tree (就是root接到另一個root)
        # v 對應的 tree root  會是新的 root
        self.id[i] = j
        self.count -= 1

    # u這個點在此tree的root是哪個數字
    def find(self, u):
        if self.id[u] != u:
            # 查找root時 順便更新此點對到的root 下次找root更快
            self.id[u] = self.find(self.id[u])
        return self.id[u]

