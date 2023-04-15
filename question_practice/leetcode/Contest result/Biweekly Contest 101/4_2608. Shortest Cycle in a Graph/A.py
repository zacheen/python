from typing import List
from collections import defaultdict

# my
# false : print(s.findShortestCycle(n = 8, edges = [[0,1],[1,2],[2,3],[3,4],[4,5],[0,7],[0,6],[5,7],[5,6]])) # 4 # 0 -> 6 -> 7 -> 0 
    # 這種情況我有可能會先找到 0,1,2,3,4,5,7,0 ,但是 0,6,7,0 更短，但因為 7 我走過了 所以我不會繼續走到 0
class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        # 1 <= edges.length <= 1000
        # 所以 DFS 最多也就做 1000 次吧
        
        # Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.
        # 這句話的意思是不會同時出現 (0,1) (1,0) 
        
        # DFS 如果走到相同的位置 代表一定有 cycle

        path = defaultdict(list)
        for p1,p2 in edges :
            path[p1].append(p2)
            path[p2].append(p1)

        min_ans = n+1
        path_mem = []
        path_mem_set = set()
        seen = [0]*n
        seen_count = 1
        def dfs(p):
            nonlocal min_ans
            nonlocal path_mem
            nonlocal seen_count

            # print("dfs :", seen, path_mem, p)
            path_mem.append(p)
            path_mem_set.add(p)
            seen[p] = seen_count
            seen_count += 1
            start_indx = 0
            for next_p in path[p] :
                if len(path_mem) >= 2 and next_p == path_mem[-2] :
                    continue
                if seen[next_p] != 0:
                    # print("seen :", next_p, seen, path_mem)
                    if seen[next_p] > start_indx :
                        if next_p in path_mem_set :
                            min_ans = min(min_ans, len(path_mem)-path_mem.index(next_p))
                            # print("min_ans :",min_ans)
                else :
                    dfs(next_p)
            path_mem.pop()
            path_mem_set.remove(p)
        
        
        for i in range(n) :
            if not seen[i]:
                start_indx = seen_count
                dfs(i)
        
        if min_ans == (n+1) :
            return -1
        else :
            return min_ans

# given ans
# 學到新的演算法 找環的方法 從某個點延伸出去 BFS 如果某個分支相遇代表有環
import math
from collections import deque
class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        path = defaultdict(list)
        for p1,p2 in edges :
            path[p1].append(p2)
            path[p2].append(p1)

        ans = math.inf
        for i in range(n):
            # dis[X] : 從 i 這個點出發，到點 X 距離有多遠
            dis = [math.inf]*(n)
            dis[i] = 0
            can_go_list = deque([i])
            while can_go_list :
                # print(can_go_list)
                now_p = can_go_list.popleft()
                for can_go_p in path[now_p] :
                    if dis[can_go_p] == math.inf :
                        dis[can_go_p] = dis[now_p]+1
                        can_go_list.append(can_go_p)
                    # 會執行到這裡代表 can_go_p 之前已經走過了
                    # 然後有因為是 popleft，所以是 BFS
                    # 所以 dis[can_go_p]>=dis[now_p] 代表形成一個新的環
                        # 且此環是從點 i BFS 出去最快相遇的兩個點
                        # 也就是最小的環
                    elif dis[can_go_p]>=dis[now_p] :
                        # print(i, can_go_p, now_p, dis[can_go_p], dis[now_p])
                        ans = min(ans, dis[can_go_p]+dis[now_p]+1) # +1 是為了加上 i 這個點
                        break

        if ans == math.inf :
            return -1
        else :
            return ans 
        
# given ans 2 Beats 49.95%
    # 這邊會比較快的原因是 1 <= edges.length <= 1000
    # 不過這個條件通常不會達成
# 這裡的想法是
    # 因為每條路徑都是不重複的
    # 所以就去判斷 每條edges 一個當起始點(start_p) 一個當終點(destin_p) 形成的最小cycle的長度

    # 所以就是從 start_p bfs (走過就不用走了)，看會不會走到 destin_p
class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        path = defaultdict(list)
        for p1,p2 in edges :
            path[p1].append(p2)
            path[p2].append(p1)

        ans = math.inf
        for start_p, destin_p in edges:
            dis = [math.inf]*(n)
            dis[start_p] = 0
            can_go_list = deque([start_p])
            while can_go_list :
                # print(can_go_list)
                now_p = can_go_list.popleft()
                for can_go_p in path[now_p] :
                    if (now_p != start_p or can_go_p != destin_p) and dis[can_go_p] == math.inf :
                        dis[can_go_p] = dis[now_p] + 1
                        can_go_list.append(can_go_p)
                        if can_go_p == destin_p :
                            ans = min(ans , dis[destin_p]+1)
                            break
            # ans = min(ans , dis[destin_p]+1)
        if ans == math.inf :
            return -1
        else :
            return ans 

s = Solution()
print(s.findShortestCycle(n = 7, edges = [[0,1],[1,2],[2,0],[3,4],[4,5],[5,6],[6,3]]))  # 3 # 0 -> 1 -> 2 -> 0 
print(s.findShortestCycle(n = 7, edges = [[0,1],[1,2],[0,2],[3,4],[4,5],[5,6],[6,3]]))  # 3 # 0 -> 1 -> 2 -> 0 
print(s.findShortestCycle(n = 4, edges = [[0,1],[0,2]])) # -1

print(s.findShortestCycle(n = 8, edges = [[0,1],[1,2],[2,3],[3,4],[4,5],[0,7],[0,6],[5,7],[5,6]])) # 4 # 0 -> 6 -> 7 -> 0 



