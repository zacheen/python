# 740. Delete and Earn
# https://leetcode.com/problems/delete-and-earn/description/

from typing import List
from math import inf
from collections import Counter, deque
from itertools import pairwise

# my : slower, but can use at different limit amount
# Template ###########################################
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        limit_nei = 1
        cou = Counter(nums)
        diff_n = list(cou.keys())
        diff_n.sort()

        dp_q = deque([0]*(limit_nei+1))
        for i, now_n in enumerate(diff_n) :
            best_pre = 0
            for prev_i in range(i-1,-1,-1) :
                if now_n > diff_n[prev_i] + limit_nei :
                    best_pre = dp_q[-(i-prev_i)]
                    break
            new_points = now_n*cou[now_n] + best_pre
            # take : now_points
            # don't take : dp_q[-1]
            dp_q.append(max(dp_q[-1], new_points))
            dp_q.popleft()
        return dp_q[-1]
# Template end ###########################################

# my : 6ms Beats87.15%
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        cou = Counter(nums)
        diff_n = list(cou.keys())
        diff_n.sort()

        dp1 = 0
        dp2 = diff_n[0]*cou[diff_n[0]]
        for prev_n, now_n in pairwise(diff_n):
            now_points = now_n*cou[now_n]
            if (prev_n+1) < now_n :
                now_points += dp2
            else :
                now_points += dp1
            # take : now_points
            # don't take : dp2
            dp1, dp2 = dp2, max(dp2, now_points)
        return dp2

s = Solution()
print("ans :",s.deleteAndEarn([3,4,2])) # 6
print("ans :",s.deleteAndEarn([2,2,3,3,3,4])) # 9



