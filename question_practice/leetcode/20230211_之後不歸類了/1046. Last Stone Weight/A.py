from typing import List
import functools

# my Beats 93.33%
    # 不過 1 <= stones.length <= 30 所以 heap 也不會特別快，因為數量太少了
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while(len(stones) >= 2) :
            s1 = heapq.heappop(stones)
            s2 = heapq.heappop(stones)
            if s1 == s2 :
                continue
            heapq.heappush(stones, s1 - s2)

        if stones :
            return -stones[0]
        else :
            return 0

# given ans

s = Solution()
print(s.lastStoneWeight([2,7,4,1,8,1]))
print(s.lastStoneWeight([1]))
# print(s.lastStoneWeight())



