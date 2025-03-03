# 983. Minimum Cost For Tickets
# https://leetcode.com/problems/minimum-cost-for-tickets/description

from typing import List
import functools

from collections import Counter, deque
from math import inf

# my 3ms Beats80.42%
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        cost_days = [1, 7, 30]
        days_set = set(days)
        dp = Counter()
        for d in range(1, days[-1]+1) :
            if d in days_set :
                dp[d] = min( dp[d-c_d]+c for c_d, c in zip(cost_days, costs) )
            else :
                dp[d] = dp[d-1]
        return dp[days[-1]]
    
# given ans 0ms Beats100.00%
# using stack to solve the problem of dp[d] = dp[d-1]
class Solution:
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        ans = 0
        last7 = deque()
        last30 = deque()
        for day in days:
            while last7 and last7[0][0] + 7 <= day:
                last7.popleft()
            while last30 and last30[0][0] + 30 <= day:
                last30.popleft()
            last7.append([day, ans + costs[1]])
            last30.append([day, ans + costs[2]])
            ans = min(ans + costs[0], last7[0][1], last30[0][1])
        return ans

s = Solution()
# print("ans :",s.mincostTickets(days = [1,4,6,7,8,20], costs = [2,7,15])) # 11, 171
print("ans :",s.mincostTickets(days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15])) # 17





