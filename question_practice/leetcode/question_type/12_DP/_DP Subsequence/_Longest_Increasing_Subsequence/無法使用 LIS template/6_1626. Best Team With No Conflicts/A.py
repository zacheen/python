# 1626. Best Team With No Conflicts
# https://leetcode.com/problems/best-team-with-no-conflicts/description/

from typing import List
from math import inf
from bisect import bisect_left
from functools import cache

# my 5854ms Beats7.19%
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        a_s = [(a,s) for s, a in zip(scores, ages)]
        a_s.sort()
        len_n = len(scores)
        @cache
        def dp(now_i, last_ok):
            if now_i == len_n :
                return 0
            
            # dont take
            ret = dp(now_i+1, last_ok)

            # take
            this_a, this_sc = a_s[now_i]
            if this_a == last_ok[0] or this_sc >= last_ok[1]:
                r = this_sc + dp(now_i+1, (this_a, this_sc))
                if r > ret :
                    ret = r
            
            return ret
        return dp(0,(0,0))

# given ans
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        dp = [0] * (1+max(ages))
        zipped = sorted(zip(scores,ages))

        for s,a in zipped:
            dp[a] = s + max(dp[:a+1])
        return max(dp)

s = Solution()
# print("ans :",s.bestTeamScore(scores = [1,3,5,10,15], ages = [1,2,3,4,5])) # 34
print("ans :",s.bestTeamScore(scores = [4,5,6,5], ages = [2,1,2,1])) # 16
print("ans :",s.bestTeamScore(scores = [1,2,3,5], ages = [8,9,10,1])) # 6



