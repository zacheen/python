# 1049. Last Stone Weight II
# https://leetcode.com/problems/last-stone-weight-ii/description/

from typing import List
from math import inf
from bisect import bisect_right

# my Time Limit Exceeded
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stones.sort()
        min_ans = inf
        def dp(stones_l):
            nonlocal min_ans
            if len(stones_l) == 2 :
                if (poss_ans := stones_l[1] - stones_l[0]) < min_ans :
                    min_ans = poss_ans
            if len(stones_l) == 1 :
                min_ans = min(min_ans, stones_l[0])
            for i1,n1 in enumerate(stones_l[:]) :
                back = stones_l[i1+1:]
                for i2,n2 in enumerate(stones_l[:i1]) :
                    new_l = stones_l[:i2]+ stones_l[i2+1:i1] + back 
                    new_stone = n1 - n2
                    if new_stone != 0 :
                        in_i = bisect_right(new_l, new_stone)
                        new_l.insert(in_i, new_stone)
                    dp(new_l)
        dp(stones)
        return min_ans

# inspire by given ans : 3ms Beats98.25%
    # This Question can actually turn into finding 
    # how to split stones to 2 group with minimum difference 
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        summ = sum(stones)
        target = summ//2
        can_comb_set = {0}  # 裡面紀錄目前可以的組合
        for num in stones:
            can_comb_set |= set( new_s for s in can_comb_set if (new_s := s + num) <= target)
        max_comb = max(can_comb_set)
        return (summ-max_comb)-max_comb

s = Solution()
print("ans :",s.lastStoneWeightII([2,7,4,1,8,1])) # 1
print("ans :",s.lastStoneWeightII([31,26,33,21,40])) # 5



