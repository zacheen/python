# knapsack
# 計算 nums中挑選的數字相加 能不能組合出target

from math import inf
from typing import List
MOD = 10**9+7

## 0/1 take or don't take ################################################################
def knapsack_01_for_set(nums, target):
    can_comb_set = {0}  # 裡面紀錄目前可以的組合
    for num in nums:
        can_comb_set |= set( new_s for s in can_comb_set if (new_s := s + num) <= target )
    return target in can_comb_set

# print(knapsack_01_for_set([1,2,3,6], 5))
# print(knapsack_01_for_set([1,2,4,8,16], 31))
# print([knapsack_01_for_set([1,2,4,8,16], i) for i in range(1,32)])
# print(knapsack_01_for_set([1,2,5], 11))

# 如果項目多 但target小 會比較快
def knapsack_01_for_target(nums, target):
    # dp[i] := True if i can be formed by nums so far
    dp = [True] + [False] * (target)
    for num in nums:
        for i in range(target, num - 1, -1): # 從大到小
            dp[i] = dp[i] or dp[i - num]
    print(dp)
    return dp[-1]

# print(knapsack_01_for_target([1,2,3,6], 5))
# print(knapsack_01_for_target([1,2,4,8,16], 31))
# print([knapsack_01_for_target([1,2,4,8,16], i) for i in range(1,32)])
# print(knapsack_01_for_target([1,2,5], 11))

## complete knapsack problem / bounded Knapsack problem ########################
# << 1_boolean_decision >>
# v1. 看前面有沒有路
def C_Knap_reach(nums, target):
    dp = [True]
    for i in range(1,target+1):
        can_reach = False
        for n in nums :
            if (pre_i:=i-n) >= 0 and dp[pre_i]:
                can_reach = True
                break
        dp.append(can_reach)
    return dp[-1]
# v2. 從這點往後推 下一點可以到的位置
def C_Knap_reach(nums, target):
    dp = [True] + [False]*target
    for i in range(len(dp)-1) :
        if dp[i] :
            for n in nums :
                if (lat_i:=i+n) < len(dp) :
                    dp[lat_i] = True
    return dp[-1]

# << 2_path_count >> 
    # 可以用 < 3_Unbounded Combination > 跟 < 4_Unbounded Permutation > 修改
        # 通常 < 4_Unbounded Permutation > 會快一些
# 1. 使用 < 4_Unbounded Permutation > 修改
def C_Knap_min_cnt(nums, target):
    dp = [0]
    for i in range(1,target+1):
        min_cou = inf
        for n in nums :
            if (pre_i:=i-n) >= 0 and (cou:=dp[pre_i]) < min_cou:
                min_cou = cou
        dp.append(min_cou+1)
    return dp[-1] if dp[-1] != inf else -1
# 2. 使用 < 3_Unbounded Combination > 修改
def C_Knap_min_cnt(nums, target):
    dp=[0] + [inf]*target
    for n in nums:
        for i in range(n, len(dp)):
            if (t:=1+dp[i-n]) < dp[i]:
                dp[i] = t
    return dp[-1] if dp[-1] != inf else -1     
    
# << 3_Unbounded Combination >>
# 518. Coin Change II
# https://leetcode.com/problems/coin-change-ii/description/
def C_Knap_comb(amount, coins):
    dp = [1]+[0]*(amount)
    for coin in coins:
        for fut_i in range(coin, len(dp)):
            dp[fut_i] += dp[fut_i-coin]
    return dp[amount]
    
# << 3_Unbounded Combination with limit amount >>
# 2585. Number of Ways to Earn Points
# https://leetcode.com/problems/number-of-ways-to-earn-points/
# limits 是每種可以取 0~limit 個
    # 每種 coin 可以取1~limit個 
        # 應該要先減去總和(先把得拿得拿完) 再轉換成 取0~limit-1個
            # 3333. Find the Original Typed String II
            # https://leetcode.com/problems/find-the-original-typed-string-ii
def C_Knap_comb_limit(target, limits):
    dp = [1] + [0]*target
    # # 排除掉 coin == 0 # 還沒確認
    # for i, (max_lim, coin) in enumerate(types) :
    #     if coin == 0 :
    #         dp[0] += max_lim
    #         del types[i]
    #         break

    s = 0
    for max_lim, coin in limits:
        s = min(s+coin*max_lim, target) # 到目前為止最大可能總和
        # 先正常計算所有可能組合數量
        for fut_i in range(coin, s+1):
            dp[fut_i] += dp[fut_i-coin]
        # 再減去超過使用次數c的組合數量
        t = (max_lim+1)*coin
        for fut_i in range(s, t-1, -1):
            dp[fut_i] -= dp[fut_i-t]
    return dp[-1] % MOD

# << 4_Unbounded Permutation >>
# 377. Combination Sum IV
# https://leetcode.com/problems/combination-sum-iv/description/

# v1 超級精簡版 (每次都從前面的結果 統計可行的組合總數)
def C_Knap_perm(nums: List[int], target: int) -> int:
    dp = [1]
    for i in range(1,target+1):
        dp.append(sum( dp[i-n] for n in nums if i>=n ) )
    return dp[-1]
# v2 (v1 的展開)
def C_Knap_perm(nums, target):
    dp = [1]+[0]*target
    for i in range(len(dp)):
        for n in nums :
            if (pre_i := i-n) >= 0 :
                dp[i] += dp[pre_i]
    return dp[-1]
