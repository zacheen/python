# my 紀錄我寫程式的過程
# 第一步先確認可以判斷有沒有 cycle
# 因為要計算最長的路徑我有兩種方法
    # 1. 紀錄走過的點
    # 2. link list 的 fast slow (最後沒實作)
        # 感覺會比較慢 但優點是不需要多餘的空間紀錄
# class Solution:
#     def longestCycle(self, edges):
#         # 紀錄這次 cycle dfs 走過的點，如果有重複，代表有一個 cycle
#         # 因為每個點只有一條路徑
#             # 所以如果走過了，就不用再判斷了
#         seen = set()
#         # seen = [False]*len(edges) # 不知道會不會比較快
#         def dfs(now_p, this_cycle):
#             if now_p == -1 :
#                 return False
#             if now_p in this_cycle :
#                 print(now_p, this_cycle)
#                 return True
#             if now_p in seen :
#                 return False

#             seen.add(now_p)
#             this_cycle.add(now_p)

#             return dfs(edges[now_p], this_cycle)

#         for i in range(len(edges)):
#             if dfs(edges[i], set([i])) :
#                 return 1
        
#         return -1

# my 改寫成第一種方法 紀錄走過的路徑 \
# 比較 seen = set() 跟 seen = [False]*len(edges) 速度
    # seen = set()
        # Runtime Beats 45.80%
        # Memory 169.1 MB Beats 24.30%
    # seen = [False]*len(edges)
        # Runtime Beats 46.42%
        # Memory 153.2 MB Beats 41.43%
    # 結論 : 速度差不多 但是空間比較省
# class Solution:
#     def longestCycle(self, edges):
#         # 紀錄這次 cycle dfs 走過的點，如果有重複，代表有一個 cycle
#         # 因為每個點只有一條路徑
#             # 所以如果走過了，就不用再判斷了
#         # seen = set()
#         seen = [False]*len(edges) # 比較快
#         max_cycle = -1
#         # 雖然 this_cycle 跟 path 是紀錄同一個東西
#             # 但是 this_cycle 是 set 所以判斷 有沒有走過比較快
#             # path 就是用來記錄路徑，計算最後路徑長度用
#         def dfs(now_p, this_cycle, path):
#             nonlocal max_cycle
#             nonlocal seen
#             if now_p == -1 :
#                 return
#             if now_p in this_cycle :
#                 cycle_len = len(path) - path.index(now_p)
#                 max_cycle = max(max_cycle, cycle_len)
#                 # print(now_p, this_cycle, cycle_len)
#                 return
#             if seen[now_p] :
#                 return

#             seen[now_p] = True
#             this_cycle.add(now_p)
#             path.append(now_p)

#             dfs(edges[now_p], this_cycle, path)

        
#         for i in range(len(edges)):
#             dfs(edges[i], set([i]), [i])

#         return max_cycle

# my 再優化 this_cycle 跟 seen 合併
# Beats 78.82%
class Solution:
    def longestCycle(self, edges):
        seen = [-1]*len(edges) # 比較快
        max_cycle = -1
        def dfs(now_p, path):
            nonlocal max_cycle
            nonlocal seen
            if now_p == -1 :
                return
            if seen[now_p] == -1:
                # 新的點
                seen[now_p] = path[0]
                path.append(now_p)
                dfs(edges[now_p], path)
            elif seen[now_p] == path[0] :
                # 形成 cycle  
                cycle_len = len(path) - path.index(now_p)
                max_cycle = max(max_cycle, cycle_len)
                # print(now_p, path, cycle_len)     
        
        for i in range(len(edges)):
            dfs(edges[i], [i])

        return max_cycle

# given ans Beats 96.89%
# 優化點
    # 1. 我是用 recursive 不過也可以用 while 解決
    # 2. 他又把 seen 跟 path 合併了
        # 那時候分開是因為我要判斷是不是這個 cycle 的結果
        # 難道不用嗎 ?
            # 那時候我想到的反例是，如果我上一個圈走過了，然後我下一個圈又走到此點，我會不知道有沒有形成 cycle
            # 因為她這裡 time 沒有歸0 而是繼續加上去
            # 所以只需要判斷現在遇到的這個重複的點有沒有大於 startTime 就好了
                # 大於 startTime 代表是這一圈的結果
class Solution:
    def longestCycle(self, edges):
        ans = -1
        time = 1
        timeVisited = [0] * len(edges)

        for i in range(len(edges)):
            # my 優化 (因為我覺得下面就會處理到了 而且中間也沒有做什麼複雜的運算)
            # if timeVisited[u] :
            #     continue
            startTime = time
            u = i
            while u != -1 and not timeVisited[u]:
                timeVisited[u] = time
                time += 1
                u = edges[u]  # Move to next node
            if u != -1 and timeVisited[u] >= startTime:
                ans = max(ans, time - timeVisited[u])

        return ans

s = Solution()
print(s.longestCycle(edges = [3,3,4,2,3]))
print(s.longestCycle(edges = [3,3,4,2,-1]))
print(s.longestCycle(edges = [2,-1,3,1]))



