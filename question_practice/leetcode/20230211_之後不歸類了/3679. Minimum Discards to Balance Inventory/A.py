# 3679. Minimum Discards to Balance Inventory
# https://leetcode.com/problems/minimum-discards-to-balance-inventory/description/

from typing import List
from math import inf
from collections import Counter, deque

# my 251ms Beats14.37%
class Solution:
    def minArrivalsToDiscard(self, arrivals: List[int], w: int, m: int) -> int:
        # since I only know I have to discarded when it is full, and I have no choice
        # thus I use greedy, to count how many item I have to discard
        mem = deque()
        cnt = Counter()
        ans = 0
        for new_item in arrivals :
            cnt[new_item] += 1
            mem.append(new_item)
            if len(mem) > w :
                cnt[mem.popleft()] -= 1
            if cnt[new_item] > m :
                cnt[mem.pop()] -= 1
                ans += 1
                mem.append(-1)
        return ans

s = Solution()
print("ans :",s.minArrivalsToDiscard(arrivals = [1,2,1,3,1], w = 4, m = 2)) # 0
print("ans :",s.minArrivalsToDiscard(arrivals = [1,2,3,3,3,4], w = 3, m = 2)) # 1



