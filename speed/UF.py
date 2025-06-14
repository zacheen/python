import sys
sys.setrecursionlimit(10000000)  # 將最大遞迴深度設為 2000

class UF:
    def __init__(self, n):
        self.id = list(range(n))

    def union(self, u, v):
        i = self.find(u)
        j = self.find(v)
        if i == j:
            return
        self.id[i] = j

    # 這個方法會跳著更新link (但更新整個link最多花 log2 次)
    def find(self, up):
        while (up:=self.id[up]) != (deep:=self.id[up]):
            self.id[up] = self.id[deep]
        return up
    # # 照理比較快，但不確定(且易讀性較差)
    # def find(self, up):
    #     while up != (deep:=self.id[up]):
    #         self.id[up] = up = self.id[deep]
    #     return up
    # # recursive version (slower)
    # def find(self, u):
    #     if self.id[u] != u:
    #         self.id[u] = self.find(self.id[u])
    #     return self.id[u]

n = 3000000
uf = UF(n)

import time
start = time.time()
for i in range(n-1) :
    uf.union(i, i+1)
# print("time :", time.time() - start)
uf.find(0)
# print("time :", time.time() - start)
for _ in range(10000):
    uf.find(0)
print("time :", time.time() - start)