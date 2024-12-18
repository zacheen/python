# 2558. Take Gifts From the Richest Pile
# https://leetcode.com/problems/take-gifts-from-the-richest-pile/description

from typing import List
import functools

# my 2ms Beats91.28%
import heapq
import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-n for n in gifts]
        heapq.heapify(gifts)
        for _ in range(k) :
            heapq.heappush(gifts, -math.floor(math.sqrt(-heapq.heappop(gifts))))
        # print(gifts)
        return -sum(gifts)

# given ans
# same, but using isqrt

s = Solution()
print("ans :",s.pickGifts(gifts = [25,64,9,4,100], k = 4))
print("ans :",s.pickGifts(gifts = [1,1,1,1], k = 4))



