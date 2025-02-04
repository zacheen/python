# 3443. Maximum Manhattan Distance After K Changes
# https://leetcode.com/problems/maximum-manhattan-distance-after-k-changes/description/

from typing import List
import functools

from collections import Counter
# my 4445ms Beats100.00%
class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        cou = Counter()
        def change(d1,d2,k) :
            if cou[d1] < cou[d2] :
                d1,d2 = d2,d1
            # d1 must bigger than d2
            max_change = min(cou[d2], k)
            return (cou[d1]+max_change) - (cou[d2]-max_change), k-max_change
        
        max_ans = 0
        for c in s :
            cou[c] += 1
            ret, tmpk = change('N','S',k)
            ret2, tmpk2 = change('E','W',tmpk)
            max_ans = max(max_ans, ret + ret2)
        return max_ans

import operator
# given ans : 4377ms Beats100.00%
    # optimized
    # max_len == s len
class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        cou = Counter()
        def change(d1,d2) :
            if cou[d1] < cou[d2] :
                d1,d2 = d2,d1
            # d1 must bigger than d2
            return (cou[d1], cou[d2])
        
        max_ans = 0
        for i, c in zip(range(1, len(s)+1), s) :
            cou[c] += 1
            forw_len, need_to_c = (map(operator.add, change('N','S'), change('E','W')))
            max_ans = max(max_ans, min(i, forw_len + k*2 - need_to_c))
        return max_ans

s = Solution()
print("ans :",s.maxDistance(s = "NWSE", k = 1)) # 3
print("ans :",s.maxDistance( s = "NSWWEW", k = 3)) # 6



