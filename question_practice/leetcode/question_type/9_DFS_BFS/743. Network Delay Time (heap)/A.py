import numpy as np
import heapq
from collections import defaultdict

# my v3 最短的路徑就交給 heap 處理
# Runtime: 505 ms, faster than 79.12% of Python3
class Solution:
    def networkDelayTime(self, times, n, k):
        paths = defaultdict(list)  # 竟然是 hash 比較快
        # paths = [[] for _ in range(n+1)] # Runtime: 666 ms, faster than 40.53% of Python3 
        not_seen = [True]*(n+1)
        
        for t in times :
            paths[t[0]].append((t[1],t[2]))

        next_pos = [(0,k)]
        seen_count = 0
        while next_pos :
            # 每次都先挑 時間最短的"紀錄" 
            total_t, pos = heapq.heappop(next_pos)
            if not_seen[pos] :
                not_seen[pos] = False
                seen_count += 1
                if seen_count == n :
                    return total_t
                for i, new_t in paths[pos] :
                    heapq.heappush(next_pos, (total_t + new_t, i))
            
        return -1


# my v2 heap 都先找路徑最短的
# Runtime: 970 ms, faster than 12.58% of Python3 好像也沒有比較快 ...
# class Solution:
#     def networkDelayTime(self, times, n, k):
#         link = np.zeros( shape = (n+1, n+1) , dtype=int )
#         link.fill(10000)
#         paths = defaultdict(list)
        
#         # 自己到自己填 0
#         for i in range(1,n+1) :
#             link[i][i] = 0
        
#         next_pos = []
#         for t in times :
#             link[t[0]][t[1]] = t[2]
#             paths[t[0]].append(t[1])
#             if t[0] == k :
#                 next_pos.append((t[2], t[1]))
             
#         while next_pos :
#             t, pos = heapq.heappop(next_pos)
#             for i in paths[pos] :
#                 new_time = link[pos][i] + t
#                 if new_time < link[k][i] :
#                     link[k][i] = new_time
#                     heapq.heappush(next_pos, (new_time, i))
            
#         # print(link[k][1:])
#         max_time = max(link[k][1:])
#         if max_time == 10000 :
#             return -1
#         else :
#             return max_time

# my v1
# import numpy as np
# class Solution:
#     def networkDelayTime(self, times, n, k):
#         link = np.zeros( shape = (n+1, n+1) , dtype=int )
#         link.fill(10000)
#         paths = defaultdict(list)
        
#         # 自己到自己填 0
#         for i in range(1,n+1) :
#             link[i][i] = 0
        
#         next_pos = []
#         for t in times :
#             link[t[0]][t[1]] = t[2]
#             paths[t[0]].append(t[1])
#             if t[0] == k :
#                 next_pos.append((t[1], t[2]))
             
#         while next_pos :
#             new_next_pos = []
#             for pos,t in next_pos :
#                 for i in paths[pos] :
#                     # print("expand pos", pos, i)
#                     new_time = link[pos][i] + t
#                     # print(new_time , link[k][i])
#                     if new_time < link[k][i] :
#                         link[k][i] = new_time
#                         new_next_pos.append((i, new_time))
            
#             next_pos = new_next_pos  
            
#         # print(link[k][1:])
#         max_time = max(link[k][1:])
#         if max_time == 10000 :
#             return -1
#         else :
#             return max_time

# given ans 概念跟 v3 一樣

s = Solution()
print(s.networkDelayTime(times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2))



