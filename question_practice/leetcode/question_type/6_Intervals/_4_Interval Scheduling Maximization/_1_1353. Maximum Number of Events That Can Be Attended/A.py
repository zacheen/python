# 1353. Maximum Number of Events That Can Be Attended
# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended

from typing import List
from math import inf
from heapq import heappush, heappop

# my : 118ms Beats91.90%
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(key = lambda x : x[0])
        ans = 0
        # 先把目前可以取的範圍加入 heap 中
        # 都先取出最先結束的值(最小的)，判斷是否可行
        len_e = len(events)
        max_en = max(en for st, en in events)
        heap = []
        add_i = 0
        ans = 0
        for now_st in range(max_en+1) :
            while add_i < len_e and now_st == events[add_i][0] :
                heappush(heap, events[add_i][1])
                add_i += 1
            while heap :
                pop_en = heappop(heap)
                if pop_en >= now_st :
                    ans += 1
                    break
        return ans

s = Solution()
print("ans :",s.maxEvents([[1,2],[2,3],[3,4]])) # 3
print("ans :",s.maxEvents([[1,2],[2,3],[3,4],[1,2]])) # 4
print("ans :",s.maxEvents([[1,2],[1,2],[3,3],[1,5],[1,5]])) # 5
print("ans :",s.maxEvents([[1,5],[1,5],[1,5],[2,3],[2,3]])) # 5
print("ans :",s.maxEvents([[1,1],[1,2],[2,2]])) # 2



