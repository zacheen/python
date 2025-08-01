# 898. Bitwise ORs of Subarrays
# https://leetcode.com/problems/bitwise-ors-of-subarrays

from typing import List
from math import inf

# my 395ms Beats74.40%
class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        all_seen = set()
        now_seen = set()
        for n in arr :
            now_seen = {n | past_n for past_n in now_seen}
            now_seen.add(n)
            all_seen |= now_seen
        return len(all_seen)

s = Solution()
print("ans :",s.subarrayBitwiseORs([0])) # 1
print("ans :",s.subarrayBitwiseORs([1,1,2])) # 3
print("ans :",s.subarrayBitwiseORs([1,2,4])) # 6



