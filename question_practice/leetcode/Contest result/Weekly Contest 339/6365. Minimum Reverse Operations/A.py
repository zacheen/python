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

# given ans 改寫 (改成有意義的變數名稱) Beats 100%
# 我是透過這一個點去計算下一個有可能的位置
# 但是這裡是先把有可能的點列好(can_go)，然後從這個位置判斷要從 can_go 取出哪些下一回合可以走的點
    # 這樣就不會判斷很多次，只需要判斷 can_go 剩餘的點是不是現在這個點，可以走到的位置
from sortedcontainers import SortedSet
class Solution:
    def minReverseOperations(self, n: int, p: int, banned: List[int], k: int):
        ans = [-1] * n
        ban = [False] * n
        can_go = [SortedSet(), SortedSet()]
        stack = deque([p])
        step_count = 0
        
        # 紀錄不能走的位置
        for x in banned:
            ban[x] = True

        # 跟我 k 要分偶數跟奇數相同
        for i in range(n):
            if not ban[i]:
                can_go[i & 1].add(i)
        can_go[p & 1].remove(p)
        # print(can_go)

        while stack:
            for _ in range(len(stack)):
                now_p = stack.popleft()
                ans[now_p] = step_count
                smallest_possible_p = abs(now_p - k + 1)
                next_pos_odd_even = smallest_possible_p & 1
                next_candidate = can_go[next_pos_odd_even]
                smallest_possible_indx = next_candidate.bisect_right(smallest_possible_p - 1) # -1 是為了找到下一個位置
                # print("next_candidate :", next_candidate, now_p, smallest_possible_p, smallest_possible_indx)
                # print("stack :",stack)
                while smallest_possible_indx < len(next_candidate):
                    next_p = next_candidate[smallest_possible_indx]
                    if next_p > n - 1 - abs(n - now_p - k) :
                        break
                    stack.append(next_p)
                    next_candidate.remove(next_p)
                # print("stack :",stack)
            step_count += 1
        return ans
s = Solution()
# print(s.minReverseOperations(n = 4, p = 0, banned = [1,2], k = 4))
# print(s.minReverseOperations(n = 5, p = 0, banned = [2,4], k = 3))
# print(s.minReverseOperations(n = 4, p = 2, banned = [0,1,3], k = 1))
# print(s.minReverseOperations(n = 4, p = 0, banned = [], k = 4))
print(s.minReverseOperations(n = 20, p = 10, banned = [], k = 5))



