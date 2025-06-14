# Disjoint Set Union-find algorithm (DSU)
# union 是用來
    # 看說兩點之間有沒有關係
    # 沒關係的區域共有幾個 : <計算目前總共分成幾個 set>
    # 看有關係的點共有幾個 : <計算各個 set 的個數>

# 最基本的版本
    # find 有做路徑壓縮 (下一次搜尋的時候就不需要這麼久的時間)
    # 如果是字串 其實可以比較字串是否有關連 union index 位置 (union(i1,i2))
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
    # # recursive version (slower, might because recursive needs a lot of mem)
    # def find(self, u):
    #     if self.id[u] != u:
    #         self.id[u] = self.find(self.id[u])
    #     return self.id[u]

# <不需要初始化 且適用各種type(str, tuple)>
    # !! 有相同的項目不能用 > 可以改成用項目位置
class UF_no_init:
    def __init__(self):
        self.id = {}                # <適用各種type> 多的

    def union(self, u, v):
        i = self.find(u)
        j = self.find(v)
        if i == j:
            return
        self.id[i] = j

    def find(self, up):
        while up in self.id and up != (deep:=self.id[up]):
            self.id[up] = up = self.id[deep] if deep in self.id else deep
        return up
    # # recursive version (slower)
    # def find(self, u):
    #     if u not in self.id : return u
    #     if self.id[u] != u:
    #         self.id[u] = self.find(self.id[u])
    #     return self.id[u]

# <計算目前總共分成幾個 set>
class UF_count:
    def __init__(self, n):
        self.count = n              # <計算目前總共分成幾個 set> 多的
        self.id = list(range(n))

    def union(self, u, v):
        i = self.find(u)
        j = self.find(v)
        if i == j:
            return
        self.id[i] = j
        self.count -= 1             # <計算目前總共分成幾個 set> 多的

    def find(self, up):
        while (up:=self.id[up]) != (deep:=self.id[up]):
            self.id[up] = self.id[deep]
        return up
    
# <計算各個 set 的個數> 
# "ID" 這個項目的 set 有幾個項目 : uf.set_member[uf.find(ID)] 
class UF_each_set_count:
    def __init__(self, n):
        self.id = list(range(n))
        self.set_member = [1]*n     # <計算各個 set 的個數> 多的

    def union(self, u, v):
        i = self.find(u)
        j = self.find(v)
        if i == j:
            return
        self.set_member[j] += self.set_member[i]  # <計算各個 set 的個數> 多的
        self.set_member[i] = 0                    # 0 代表被合併了 (非必要)
        self.id[i] = j 

    def find(self, up):
        while (up:=self.id[up]) != (deep:=self.id[up]):
            self.id[up] = self.id[deep]
        return up

# Union by size 
    # 可助於減少 新增union時 find需要查找與修改代表的時間
        # 不過也因為多了一些判斷 所以不一定會比較快
    # 原理是把小的 set 歸類到 大的 set 中
        # 所以就是把 有計算各個 set 的個數 再加上判斷變更 union 的方向
class UF_by_size:
    def __init__(self, n):
        self.id = list(range(n))
        self.set_member = [1]*n    # <計算各個 set 的個數> 多的

    def union(self, u, v):
        i = self.find(u)
        j = self.find(v)
        if i == j:
            return
        if self.set_member[i] > self.set_member[j] : #  <Union by size> 多的
            i,j = j,i
        self.set_member[j] += self.set_member[i]  # <計算各個 set 的個數> 多的
        self.id[i] = j

    def find(self, up):
        while (up:=self.id[up]) != (deep:=self.id[up]):
            self.id[up] = self.id[deep]
        return up

# 讓 union 每次都指到最小的數字
class UF_by_min:
    def __init__(self, n):
        self.id = list(range(n))

    def union(self, u, v):
        i = self.find(u)
        j = self.find(v)
        if i == j:
            return
        if i < j :           # union 的時候比較數字大小
            self.id[j] = i
        else :
            self.id[i] = j

    def find(self, up):
        while (up:=self.id[up]) != (deep:=self.id[up]):
            self.id[up] = self.id[deep]
        return up

# 全功能都有 (除了 "讓 union 每次都指到最小的數字")
class UF_all:
    def __init__(self, n):
        self.count = n
        self.id = list(range(n))
        self.set_member = [1]*n

    def union(self, u, v):
        i = self.find(u)
        j = self.find(v)
        if i == j:
            return
        if self.set_member[i] > self.set_member[j] :
            i,j = j,i
        self.set_member[j] += self.set_member[i]
        self.id[i] = j
        self.count -= 1

    def find(self, up):
        while (up:=self.id[up]) != (deep:=self.id[up]):
            self.id[up] = self.id[deep]
        return up
    
# 全功能都有 
    # 但set_member 改成紀錄相關的成員
    # 因此可以透過 uf.set_member[uf.find(ID)] 查詢相關成員
class UF_find_relate:
    def __init__(self, n):
        self.count = n
        self.id = list(range(n))
        self.set_member = [set([i]) for i in range(n)]

    def union(self, u, v):
        i = self.find(u)
        j = self.find(v)
        if i == j:
            return
        self.set_member[j] = self.set_member[j] | self.set_member[i]
        self.set_member[i] = None
        self.id[i] = j
        self.count -= 1

    def find(self, up):
        while (up:=self.id[up]) != (deep:=self.id[up]):
            self.id[up] = self.id[deep]
        return up
    
    def ger_related(self, u):
        if self.id[u] != u:
            self.id[u] = self.find(self.id[u])
        return self.set_member[self.id[u]]

# 從 UF_find_relate 修改而來 + UF_no_init
# 新增功能 : 一開始不用指定大小 且適用 char
class UF_find_relate_no_init_v1:
    def __init__(self):
        self.id = {}
        self.set_member = {}
    
    def add_item(self, item):
        try :
            # 如果有找到此項目 就代表此項目已經存在
            self.find(item)
        except :
            # 如果跳錯 代表沒有此項目
            self.id[item] = item
            self.set_member[item] = set([item])

    def union(self, u, v):
        i = self.find(u)
        j = self.find(v)
        if i == j:
            return
        self.set_member[j] = self.set_member[j] | self.set_member[i]
        del(self.set_member[i])
        self.id[i] = j

    def find(self, up):
        while up in self.id and up != (deep:=self.id[up]):
            self.id[up] = up = self.id[deep] if deep in self.id else deep
        return up
    
    def ger_related(self, u):
        if self.id[u] != u:
            self.id[u] = self.find(self.id[u])
        return self.set_member[self.id[u]]
    
from collections import defaultdict
# 跟 UF_find_relate_no_init_v1 差在這裡用 defaultdict
class UF_find_relate_no_init_v2: # 尚未驗證
    def __init__(self):
        self.id = {}
        self.set_member = defaultdict(lambda x : x)

    def union(self, u, v):
        i = self.find(u)
        j = self.find(v)
        if i == j:
            return
        self.set_member[j] = self.set_member[j] | self.set_member[i]
        del(self.set_member[i])
        self.id[i] = j

    def find(self, up):
        while up in self.id and up != (deep:=self.id[up]):
            self.id[up] = up = self.id[deep] if deep in self.id else deep
        return up
    
    def ger_related(self, u):
        if self.id[u] != u:
            self.id[u] = self.find(self.id[u])
        return self.set_member[self.id[u]]

# classic question : 計算目前總共分成幾個 set
# 547. Number of Provinces
# https://leetcode.com/problems/number-of-provinces/description/
class Solution:
    def findCircleNum(self, M):
        n = len(M)
        uf = UF_all(n)

        # 加入連結
        for i in range(n):
            for j in range(i, n):
                if M[i][j] == 1:
                    uf.union(i, j)
        print("u have linked point :", uf.set_member[uf.find(0)])
        return uf.count
# M[i][j] 代表 點i與點j有相連
# 請問總共有幾區 (若兩點之前有相連代表是同一區)
s = Solution()
print(s.findCircleNum(M = [[1,1,0],[1,1,0],[0,0,1]]))
print(s.findCircleNum(M = [[1,0,0],[0,1,0],[0,0,1]]))

if __name__ == "__main__" :
    # demo_find_related
    relation = [(5,4),(11,12),(10,8),(6,7),(1,3),(4,6),(2,3),(8,9)]
    # (1,3),(2,3),(6,7),(5,4),(4,6),(10,8),(8,9),(11,12)
    uf = UF_find_relate(15)
    for i,j in relation:
        uf.union(i, j)
    print("find :", uf.find(1))
    print("set_member :", uf.set_member)
    print("related :",uf.ger_related(1))

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
            # 也就是說可以重複加入
        # v 對應的 tree root 會是新的 root
        self.id[i] = j
        self.count -= 1

    # u這個點在此tree的root是哪個數字
    def find(self, u):
        if self.id[u] != u:
            # 查找root時 順便更新此點對到的root 下次找root更快
            self.id[u] = self.find(self.id[u])
        return self.id[u]

