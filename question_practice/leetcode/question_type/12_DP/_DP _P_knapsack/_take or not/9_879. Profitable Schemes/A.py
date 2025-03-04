# 879. Profitable Schemes
# https://leetcode.com/problems/profitable-schemes/description/

from typing import List
from math import inf
from functools import cache
from collections import Counter
from itertools import zip_longest

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

# my 1571ms Beats54.86%
MOD = 10**9+7
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        len_n = len(group)
        @cache
        def dp(i, remain_n):
            if remain_n == 0 or i >= len_n:
                return Counter({0:1})
            ret = Counter()
            this_profit = profit[i]
            need_n = group[i]
            # take i
            if remain_n >= need_n :
                pass_ret = dp(i+1, remain_n-need_n)
                for pro in list(pass_ret.keys()):  # 需要使用 list() 來避免修改時影響迭代
                    if (new_pro:=pro + this_profit) < minProfit :
                        ret[new_pro] = pass_ret[pro]
                    else :
                        ret[minProfit] += pass_ret[pro]
            # dont take
            ret += dp(i+1, remain_n)
            return ret
        res = dp(0, n)
        return res[minProfit]%MOD

# given ans : 266ms Beats100.00%
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

s = Solution()
print("ans :",s.profitableSchemes(n = 5, minProfit = 3, group = [2,2], profit = [2,3])) # 2
print("ans :",s.profitableSchemes(n = 10, minProfit = 5, group = [2,3,5], profit = [6,7,8])) # 7



