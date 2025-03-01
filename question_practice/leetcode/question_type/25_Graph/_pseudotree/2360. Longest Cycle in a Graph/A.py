# 2360. Longest Cycle in a Graph
# https://leetcode.com/problems/longest-cycle-in-a-graph/description/

# # my practice again : 211ms Beats57.94%
#     # modify from has_cycle
#     # this method acceptable, since graph is pseudotree
# class Solution:
#     def longestCycle(self, edges):
#         len_n = len(edges)
#         color = [0] * len_n
#         max_ans = -1
#         def dfs(x, now_len):
#             if color[x] == 2 :
#                 return None
#             color[x] = 1
#             next_n = edges[x]
#             if next_n == -1 : return None
#             if color[next_n] == 1 :
#                 return next_n, 2 # 2 : include now_n and next_n
#             ret = dfs(next_n, now_len+1)
#             if ret :
#                 if ret[0] == x :
#                     nonlocal max_ans
#                     if ret[1] > max_ans :
#                         max_ans = ret[1]
#                     return None
#                 else :
#                     return ret[0], ret[1]+1
#             color[x] = 2
#             return None
        
#         for n in range(len_n) :
#             dfs(n, 1)
#         return max_ans

# my 187ms Beats69.93%
    # mem path
    # use path[0] to indicate which round > prevent second assign
class Solution:
    def longestCycle(self, edges):
        seen = [-1]*len(edges) # 比較快
        max_cycle = -1
        def dfs(now_p, path):
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
                nonlocal max_cycle
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
print(s.longestCycle(edges = [3,3,4,2,3])) # 3
print(s.longestCycle(edges = [3,3,4,2,-1]))
print(s.longestCycle(edges = [2,-1,3,1])) # -1



