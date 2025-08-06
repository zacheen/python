# 2561. Rearranging Fruits
# https://leetcode.com/problems/rearranging-fruits

from typing import List
from math import inf
from collections import Counter

# my 83ms Beats79.22%
class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        basket1_cnt = Counter(basket1)
        basket2_cnt = Counter(basket2)
        target = basket1_cnt + basket2_cnt
        if any( cnt&1 == 1 for cnt in target.values() ) :
            return -1
        target = {n : cnt//2 for n, cnt in target.items()}

        missing = []
        remove  = []
        for n, cnt in target.items() :
            diff = cnt - basket1_cnt[n]
            if diff >= 0 :
                missing += [n]*diff
            else :
                remove += [n]*-diff

        min_num_twice = min(target)*2
        missing.sort()
        remove.sort(reverse=True)
        return sum(min(n1,n2,min_num_twice) for n1,n2 in zip(missing, remove))
    
s = Solution()
print("ans :",s.minCost(basket1 = [4,2,2,2], basket2 = [1,4,1,2])) # 1
print("ans :",s.minCost(basket1 = [2,3,4,1], basket2 = [3,2,5,1])) # -1
print("ans :",s.minCost([4,4,4,4,3], [5,5,5,5,3])) # 8

# fail once : minor swap twice
print("ans :",s.minCost([84,80,43,8,80,88,43,14,100,88], [32,32,42,68,68,100,42,84,14,8])) # 48
print("ans :",s.minCost([1,100,100], [1,99,99])) # 2



