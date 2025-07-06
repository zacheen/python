# 879. Profitable Schemes
# https://leetcode.com/problems/profitable-schemes/description/

from typing import List
from math import inf
from functools import cache
from collections import Counter, defaultdict
from itertools import zip_longest

# my using template knapsack_01_comb v1 : 328ms Beats99.60%
MOD = 10**9+7
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        dp = [[0]*(n+1) for _ in range(minProfit+1)] # dp[p][g]
        dp[0][0] = 1
        for g,p in zip(group,profit):
            for pre_p in range(minProfit, -1, -1):
                fut_p = min(pre_p+p, minProfit)
                for fut_g in range(n, g-1, -1):
                    dp[fut_p][fut_g] += dp[pre_p][fut_g-g]
        return sum( dp[-1] ) % MOD
    
# given ans optimized: 266ms Beats100.00%
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        mod = 1000000007
        dp = [[0]*(n+1) for i in range(minProfit+1)]
        dp[0][0] = 1
        for g,p in zip(group,profit):
            for j in range(n,g-1,-1):
                dp[minProfit][j] += dp[minProfit][j-g]
            for i in range(max(0,minProfit-p),minProfit):
                for j in range(g,n+1):
                    dp[minProfit][j] += dp[i][j-g]
            # adding take and dont take
            for i in range(minProfit-1,p-1,-1):
                dp[i][g:] = [(x+y) for x,y in zip(dp[i][g:],dp[i-p])]
        return sum(dp[minProfit])%mod

# my using template knapsack_01_comb v2 : 913ms Beats73.91%
MOD = 10**9+7
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        mem = defaultdict(int)
        mem[(0,0)] = 1
        for g,p in zip(group,profit):
            for (pre_g, pre_p), cnt in mem.copy().items() :
                if (new_g := pre_g + g) <= n :
                    new_p = min(pre_p+p, minProfit)
                    mem[(new_g, new_p)] += cnt
        return sum( cnt for (g, p), cnt in mem.items() if p == minProfit) % MOD

# my optimized : 533ms Beats95.99%
MOD = 10**9+7
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        len_n = len(group)
        arr_lim = minProfit+1
        @cache
        def dp(i, remain_n):
            if remain_n == 0 or i >= len_n:
                return [1]
            ret = [0]
            this_profit = profit[i]
            need_n = group[i]
            # take i
            if remain_n >= need_n :
                ret = dp(i+1, remain_n-need_n)
                ret = ([0]*this_profit) + ret
                while len(ret) > arr_lim :
                    t = ret.pop()
                    ret[-1] += t
            # dont take
            ret = [n1+n2 for n1,n2 in zip_longest(ret, dp(i+1, remain_n), fillvalue=0)]
            return ret
        res = dp(0, n)
        if len(res) == arr_lim :
            return res[minProfit]%MOD
        else :
            return 0

s = Solution()
print("ans :",s.profitableSchemes(n = 5, minProfit = 3, group = [2,2], profit = [2,3])) # 2
print("ans :",s.profitableSchemes(n = 10, minProfit = 5, group = [2,3,5], profit = [6,7,8])) # 7



