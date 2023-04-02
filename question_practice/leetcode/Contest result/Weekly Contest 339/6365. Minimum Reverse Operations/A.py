# my Time Limit Exceeded
from collections import deque
from typing import List
class Solution:
    def minReverseOperations(self, n: int, p: int, banned: List[int], k: int):
        # 可以換到 不大於自己 的偶數或奇數個位子 (還要確保有足夠的空間可以換)
        # k = 2 : 可以換到 1
        # k = 3 : 可以換到 0,2
        # k = 4 : 可以換到 1,3

        # BFS 如果走到 banned 或 != 0 就停止
            # BFS 因為要印出最小的數字

        banned_indx = set(banned)
        stack = [p]
        # never_seen = n+1
        ans = [-1]*n # n+1 還沒走過, -1 不行走, 0~n 代表走過了  
        k_is_odd = (k%2 == 1)

        for ban in banned :
            ans[ban] = -1

        step_count = 0
        while stack :
            next_stack = set()
            for now_p in stack :
                # check range
                if now_p < 0 or now_p >= n :
                    continue
                # check block
                if now_p in banned_indx :
                    continue
                # check seen
                if ans[now_p] > -1 :
                    continue

                ans[now_p] = step_count
                
                if k_is_odd :
                    r = now_p + (k+1)//2
                    offset = 2
                    while(r < n and offset < k ):
                        if (r-(k-1) >= 0):
                            next_stack.add(now_p + offset)
                        r += 1
                        offset += 2
                    l = now_p - (k+1)//2
                    offset = 2
                    while(l >= 0 and offset < k ):
                        if (l+(k-1) < n):
                            next_stack.add(now_p - offset)
                        l -= 1
                        offset += 2
                else :
                    r = now_p + (k)//2
                    offset = 1
                    while(r < n and offset < k ):
                        if (r-(k-1) >= 0):
                            next_stack.add(now_p + offset)
                        r += 1
                        offset += 2
                    l = now_p - (k)//2
                    offset = 1
                    while(l >= 0 and offset < k ):
                        if (l+(k-1) < n):
                            next_stack.add(now_p - offset)
                        l -= 1
                        offset += 2
            step_count += 1
            stack = next_stack
            # print(ans)
        
        return ans

# given ans
from sortedcontainers import SortedSet
class Solution:
    def minReverseOperations(self, n: int, p: int, banned: List[int], k: int):
        a, b, c, q, v = [-1] * n, [False] * n, [SortedSet(), SortedSet()], deque([p]), 0
        for x in banned:
            b[x] = True
        for i in range(n):
            if not b[i]:
                c[i & 1].add(i)
        c[p & 1].remove(p)
        while q:
            for s in range(len(q), 0, -1):
                w = q.popleft()
                a[w], x = v, c[abs(w - k + 1) & 1].bisect_right(abs(w - k + 1) - 1)
                while x < len(c[abs(w - k + 1) & 1]) and c[abs(w - k + 1) & 1][x] <= n - 1 - abs(n - w - k):
                    q.append(c[abs(w - k + 1) & 1][x])
                    c[abs(w - k + 1) & 1].remove(c[abs(w - k + 1) & 1][x])
            v += 1
        return a
s = Solution()
print(s.minReverseOperations(n = 4, p = 0, banned = [1,2], k = 4))
print(s.minReverseOperations(n = 5, p = 0, banned = [2,4], k = 3))
print(s.minReverseOperations(n = 4, p = 2, banned = [0,1,3], k = 1))
print(s.minReverseOperations(n = 4, p = 0, banned = [], k = 4))



