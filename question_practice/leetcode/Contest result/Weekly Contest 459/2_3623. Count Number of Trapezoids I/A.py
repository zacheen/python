# 3623. Count Number of Trapezoids I
# https://leetcode.com/problems/count-number-of-trapezoids-i

# fail : I thought I have to calculate both horizontal and vertical trapezoids
    # but actually horizontal trapezoids are needed

from typing import List
from math import inf
from collections import Counter

# my : 111ms
    # given ans opt : 60ms
MOD = 10**9+7
class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        # given ans opt : 60ms
        y_cnt = Counter(y for x, y in points)

        # my
        # y_cnt = Counter()
        # for x, y in points:
        #     y_cnt[y] += 1

        def cal_comb(n):
            return (n-1)*n//2

        ans = 0
        same_cnt = [cal_comb(n) for n in y_cnt.values() if n >= 2]
        past_comb = 0
        for new_comb in same_cnt :
            ans = (past_comb*new_comb + ans) % MOD
            past_comb += new_comb
        return ans

s = Solution()
print("ans :",s.countTrapezoids([[1,0],[2,0],[3,0],[2,2],[3,2]])) # 3
print("ans :",s.countTrapezoids([[0,0],[1,0],[0,1],[2,1]])) # 1
# print("ans :",s.countTrapezoids()) # 

