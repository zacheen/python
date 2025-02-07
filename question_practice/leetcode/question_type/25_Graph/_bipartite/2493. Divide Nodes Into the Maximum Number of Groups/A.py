# 2493. Divide Nodes Into the Maximum Number of Groups
# https://leetcode.com/problems/divide-nodes-into-the-maximum-number-of-groups/description

from typing import List
from math import inf

from collections import deque

# given ans : 587ms Beats95.56%
class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for x, y in edges:
            x -= 1
            y -= 1
            g[x].append(y)
            g[y].append(x)

        color = [0] * n
        # check whether the graph is valid, and generate connectedComponent simultaneously
        def is_bipartite(x: int, c: int) -> bool: 
            nodes.append(x)
            color[x] = c
            for y in g[x]:
                if color[y] == c or color[y] == 0 and not is_bipartite(y, -c):
                    return False
            return True

        def bfs(root: int):
            visited = [False] * n
            visited[root] = True
            depth = 0
            q = [root]
            while q:
                new_q = []
                for x in q:
                    for y in g[x]:
                        if not visited[y]:
                            visited[y] = True
                            new_q.append(y)
                q = new_q
                depth += 1
            return depth

        ans = 0
        for i, c in enumerate(color):
            if c != 0:
                continue
            nodes = []
            if not is_bipartite(i, 1): 
                return -1
            ans += max(bfs(x) for x in nodes)
        return ans

# given ans 2 : 1741ms Beats39.96%
class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        ### Greating the graph
        graph = [[] for _ in range(n+1)]
        for s,e in edges:
            graph[s].append(e)
            graph[e].append(s)

        ### Do a BFS on the graph given a start point.
        ### One thing we have to do is to check if the graph has a odd number edges cycle.
        ### This is done by checking the if the neighbor node has been visited before 
        ### and if the neighbor was on the same level as the current node when we were visiting the neighbor.
        # node 這一點開始當第一個 group，每次 BFS 都可以增加長度1，直到結束
        def BFS(node):
            q = deque([node])
            seen = {node:1}
            while q:
                cur = q.popleft()
                level = seen[cur]
                for nei in graph[cur]:
                    if nei not in seen:
                        seen[nei] = level+1
                        q.append(nei)
                    ### check if there is a odd number edges cycle
                    elif seen[nei]==level: 
                        return -1
            # BFS 愈後面當然愈長
            return level
        
        ### Store the largest number of groups in each connected component
        maxGroup = []
        visited = set()
        for i in range(1,n+1):
            if i in visited:
                continue
            ### BFS to find the connected component.
            q = deque([i])
            connectedComponent = {i}
            while q:
                cur = q.popleft()
                for nei in graph[cur]:
                    if nei not in connectedComponent:
                        connectedComponent.add(nei)
                        q.append(nei)
                        visited.add(nei)
            
            ### Place holder for the current connected component.
            max_len = 0
            ### Start a BFS on each node, and update the maxGroup for the current connected component
            for i in connectedComponent:
                ret_len = BFS(i)
                ### There is a odd number edges cycle, so return -1
                if ret_len==-1 :
                    return -1
                max_len = max(max_len,ret_len)
            maxGroup.append(max_len)
        return sum(maxGroup)



s = Solution()
# print("ans :",s.magnificentSets(n = 6, edges = [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]])) # 4
# print("ans :",s.magnificentSets(n = 3, edges = [[1,2],[2,3],[3,1]])) # -1
print("ans :",s.magnificentSets(n = 8, edges = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,8],[8,1],[1,6]])) # -1



