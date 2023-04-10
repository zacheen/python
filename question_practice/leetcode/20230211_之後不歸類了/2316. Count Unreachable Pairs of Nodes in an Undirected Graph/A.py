from collections import Counter
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


# my v1 Time Limit Exceeded
class Solution(object):
    def countPairs(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        uf = UF(n)

        for i,j in edges :
            uf.union(i, j)

        ans_count = 0
        for p1 in range(n) :
            for p2 in range(n) :
                if p1 == p2 :
                    continue
                
                if uf.find(p1) != uf.find(p2) :
                    ans_count += 1

        return ans_count/2

# my v2 優化 Beats 51.35%
class Solution(object):
    def countPairs(self, n, edges):
        uf = UF(n)

        for i,j in edges :
            uf.union(i, j)

        c = Counter()
        for p1 in range(n) :
            c[uf.find(p1)] += 1

        ans_count = 0
        for count in c.values() :
            ans_count += count * (n - count)

        return ans_count//2

# given ans
# 我無法執行
# 不過概念跟我很像
    # 不過優化了 直接去找每個點有幾個點相連 找過的點就紀錄找過了
# class Solution:
#     def dfs(self, graph, u, seen):
#         if seen[u]:
#             return 0
#         seen[u] = True
#         return accumulate(
#             begin(graph[u]), end(graph[u]), 1,
#             [ & ](subtotal, v) [return subtotal + dfs(graph, v, seen)])
    
#     def countPairs(self, n, edges):
#         ans = 0
#         graph = [0] * n
#         seen = [0] * n
#         unreached = n

#         for e in edges:
#             u = e[0]
#             v = e[1]
#             graph[u].append(v)
#             graph[v].append(u)

#         for i in range(n):
#             reached = dfs(graph, i, seen)
#             unreached -= reached
#             ans += static_cast < long > (unreached) * reached

#         return ans

# 翻譯自 given ans Beats 30.60%
# 竟然比較慢
    # 可能是因為要從 defaultdict 裡面撈資料的關係
from collections import defaultdict
class Solution:
    def countPairs(self, n, edges):
        ans = 0
        graph = defaultdict(list)
        seen = [0] * n
        unreached = n

        def dfs(u):
            if seen[u]:
                return 0
            seen[u] = True

            return sum( dfs(p) for p in graph[u]) +1 # +1 是加上本身這個點 
            # count = 1
            # for p in graph[u] :
            #     count += dfs(p)
            # return count

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        for i in range(n):
            reached = dfs(i)
            unreached -= reached
            ans += unreached * reached

        return ans

    

s = Solution()
print(s.countPairs(n = 3, edges = [[0,1],[0,2],[1,2]]))
print(s.countPairs(n = 7, edges = [[0,2],[0,5],[2,4],[1,6],[5,4]]))



