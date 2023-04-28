from typing import List
import functools

# my Beats Beats 81.97%
# O(N) : (len(N)^2)*len(s) : 300*300*300 
# UF 會比較快的前提是我已經知道全部點之間的關係
    # 如果不知道 DFS 會比較快
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
    def numSimilarGroups(self, strs: List[str]) -> int:
        # 應該是用合併 group
        # 也不用 count 了 (因為全部字串的個數都相同)

        # 1. 怎麼判斷兩個字串是 "similar"
        def is_similar(s1,s2):
            count = 0
            for c1,c2 in zip(s1,s2) :
                if c1 != c2 :
                    count += 1
                    if count > 2 :
                        return False
            return True

        uf = UF(len(strs))
        for i, s1 in enumerate(strs) :
            for j in range(i+1, len(strs)) :
                if is_similar(s1,strs[j]) :
                    uf.union(i,j)
        return uf.count
    
        

# given ans Beats 90.16%
    # 反正都是要兩兩比較 乾脆直接全部都做
        # 有合併就 -1 個群組
# 我的寫法跟 UF 的方法架構是一樣的
# DFS 翻譯 given ans
class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def is_similar(s1,s2):
            count = 0
            for c1,c2 in zip(s1,s2) :
                if c1 != c2 :
                    count += 1
                    if count > 2 :
                        return False
            return True
        
        seen = [False]*len(strs)
        def dfs(i) :
            seen[i] = True
            for j in range(len(strs)) :
                if (not seen[j]) and is_similar(strs[i],strs[j]) :
                    dfs(j)

        ans = 0
        for i in range(len(strs)):
            if not seen[i] :
                dfs(i)
                ans+=1
        return ans

        

s = Solution()
print(s.numSimilarGroups(["tars","rats","arts","star"])) # {"tars", "rats", "arts"} and {"star"}
print(s.numSimilarGroups(["omv","ovm"]))



