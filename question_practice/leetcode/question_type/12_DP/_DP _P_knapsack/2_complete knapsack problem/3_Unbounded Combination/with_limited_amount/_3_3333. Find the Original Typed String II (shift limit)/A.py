# 3333. Find the Original Typed String II
# https://leetcode.com/problems/find-the-original-typed-string-ii

from typing import List
from math import inf

# my using template C_Knap_comb_limit
    # 這題可以想成 每個項目的 coin值 都是1
    # 每種 coin 可以取1~limit個 > shift成 取0~limit-1個 (但 target 要先扣除)
MOD = 10**9+7
# # direct assign coin value to zero
# def C_Knap_comb_limit(target, limits):
#     dp = [1] + [0]*target
#     # # 排除掉 coin == 0 # 還沒確認
#     # for i, (max_lim, coin) in enumerate(types) :
#     #     if coin == 0 :
#     #         dp[0] += max_lim
#     #         del types[i]
#     #         break

#     s = 0
#     for max_lim in limits:
#         coin = 1
#         s = min(s+coin*max_lim, target) # 到目前為止最大可能總和
#         # 先正常計算所有可能組合數量
#         for fut_i in range(coin, s+1):
#             dp[fut_i] += dp[fut_i-coin]
#         # 再減去超過使用次數c的組合數量
#         t = (max_lim+1)*coin
#         for fut_i in range(s, t-1, -1):
#             dp[fut_i] -= dp[fut_i-t]
#     return sum(dp[:-1]) % MOD

# optimized : 1239ms Beats97.87%
def C_Knap_comb_limit(target, limits):
    target -= 1
    dp = [1]+[0]*target
    s = 0
    for max_lim in limits:
        s = min(s+max_lim, target) # 到目前為止最大可能總和
        # 先正常計算所有可能組合數量
        for fut_i in range(1, s+1):
            dp[fut_i] += dp[fut_i-1]
        # 再減去超過使用次數c的組合數量
        t = (max_lim+1)
        for fut_i in range(s, t-1, -1):
            dp[fut_i] -= dp[fut_i-t]
    return sum(dp) % MOD

class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        all_comb = 1
        now_cnt = 1
        cnts = []
        end_i = len(word)-1
        for i, c1 in enumerate(word) :
            if i < end_i and c1 == word[i+1] :
                now_cnt += 1
            else :
                if now_cnt > 1 :
                    all_comb = (all_comb*now_cnt) % MOD
                    cnts.append(now_cnt-1)
                now_cnt = 1
                k -= 1

        if k <= 0 :
            return all_comb
        return (all_comb-C_Knap_comb_limit(k,cnts)) % MOD

s = Solution()
print("ans :",s.possibleStringCount(word = "aabbccdd", k = 7)) # 5
print("ans :",s.possibleStringCount(word = "aabbccdd", k = 8)) # 1
print("ans :",s.possibleStringCount(word = "aaabbb", k = 3)) # 8
print("ans :",s.possibleStringCount(word = "aaabbbccc", k = 3)) # 27
print("ans :",s.possibleStringCount(word = "kkkkk", k = 4)) # 2



