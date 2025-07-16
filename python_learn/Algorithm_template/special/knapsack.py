# knapsack
    # 0/1 knapsack Problem
    # Fixed-size Knapsack Problem
        # 因為每個其實還是只能選一次，所以還是算 0/1 knapsack Problem
    # Complete Knapsack Problem / Unbounded Knapsack Problem
# 類型
    # << 1_boolean_decision >>      判斷會不會到 target
    # << 2_path_count >>            過程中追蹤某個值(最小拿取 最大拿取 ...)
    # << 3_Combinations_count >>    計算 combination 有多少種組合
    # << 4_Permutation_count >>     計算 Permutation 有多少種組合
# 計算 nums中挑選的數字相加 能不能組合出target

from math import inf
from typing import List
from collections import defaultdict
MOD = 10**9+7

## 0/1 take or don't take ################################################################
# << 1_boolean_decision >>
    # 416. Partition Equal Subset Sum
    # https://leetcode.com/problems/partition-equal-subset-sum/
# # v1 (slower)
# def knapsack_01_reach(nums, target):
#     # dp[i] := True if i can be formed by nums so far
#     dp = [True] + [False]*(target)
#     for num in nums:
#         for pre_i in range(target-num, -1, -1): # 從大到小
#             if dp[pre_i] :
#                 dp[pre_i+num] = True
#         if dp[-1] :
#             return True
#     return False
# v2, if sparse, this is faster
def knapsack_01_reach(nums, target):
    can_comb_set = {0}  # 裡面紀錄目前可以的組合
    for num in nums:
        can_comb_set |= set( new_s for s in can_comb_set if (new_s := s+num) <= target )
        if target in can_comb_set:
            return True
    return False

# << 2_path_count >> 
    # 2915. Length of the Longest Subsequence That Sums to Target
    # https://leetcode.com/problems/length-of-the-longest-subsequence-that-sums-to-target
# # v1 (slower)
# def knapsack_01_max_cnt(nums, target):
#     dp = [0] + [-inf]*(target)
#     for num in nums:
#         for i in range(target, num-1, -1): # 從大到小
#             dp[i] = max(dp[i], dp[i-num]+1)
#     return dp[-1] if dp[-1] != -inf else -1
# v2, if sparse, this is faster
def knapsack_01_max_cnt(nums, target):
    mem = defaultdict(int)
    mem[0] = 0
    for num in nums:
        for s, l in mem.copy().items() :
            if (new_s := s+num) <= target :
                if (new_l := l+1) > mem[new_s] :
                    mem[new_s] = new_l
    if target in mem :
        return mem[target]
    else :
        return -1

# << 3_Combinations_count >>
    # 2787. Ways to Express an Integer as Sum of Powers
    # https://leetcode.com/problems/ways-to-express-an-integer-as-sum-of-powers
# v1
def knapsack_01_comb(nums, target):
    dp = [1]+[0]*(target)
    for num in nums:
        for fut_i in range(target, num-1, -1):
            dp[fut_i] += dp[fut_i-num]
    return dp[target]
# # v2, if sparse, this is faster
# def knapsack_01_comb(nums, target):
#     mem = defaultdict(int)
#     mem[0] = 1
#     for num in nums:
#         for s, cnt in mem.copy().items() :
#             if (new_s := s+num) <= target :
#                 mem[new_s] += cnt
#     return mem[target]

## Fixed-size Knapsack Problem ################################################################
    # 從所有的項目中挑出剛好 K 個
# << 1_boolean_decision >>
    # 3287. Find the Maximum Sequence Value of Array
    # https://leetcode.com/problems/find-the-maximum-sequence-value-of-array
def Fixed_Knap_reach(nums, target, exact_k):
    mem_front = [{0}] + [set() for _ in range(exact_k)] 
    # mem_front[i] : 挑了i個項目之後，所有可能組合
    mem_i_poss = [i] # 紀錄從最前面到 k+i 個，挑k個所有的可能
    for i, num in enumerate(nums, 1):
        for fut_i in range(min(exact_k, i), 0, -1):
            mem_front[fut_i] |= set( s+num for s in mem_front[fut_i-1] )
        if i >= exact_k :
            mem_i_poss.append(mem_front[-1].copy())

# << 3_Combinations_count >>
# range_n : possible coin value from 1~range_n
# exact_k : take exact k items
    # might able be optimized using prefix ??
def Fixed_Knap_comb(range_n, target, exact_k):
    dp = [1]+[0]*(target)
    for _ in range(exact_k):
        new_dp = [0]*len(dp)
        for fut_i in range(target, -1, -1):
            # # < coin is a single value>
            # new_dp[fut_i] = sum(dp[pre_i] for num in nums if (pre_i := fut_i-num) >= 0)
            # < available coin is a range> EX: 1~range_n
            new_dp[fut_i] = sum(dp[max(0,fut_i-range_n) : fut_i])
                # (expand)
                # for num in range(1,min(range_n, fut_i)+1):
                #     new_dp[fut_i] += dp[fut_i-num]
        dp = new_dp
    return dp[-1] % MOD

## complete knapsack problem / bounded Knapsack problem ########################
# << 1_boolean_decision >>
    # 139. Word Break
    # https://leetcode.com/problems/word-break/description/
# v1. 從這點往後推 下一點可以到的位置
def C_Knap_reach(nums, target):
    dp = [True] + [False]*target
    for i in range(len(dp)-1) :
        if dp[i] :
            for n in nums :
                if (lat_i:=i+n) < len(dp) :
                    dp[lat_i] = True
        if dp[-1] :
            return True
    return False
# v2. 看前面有沒有路
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


# << 2_path_count >> 
    # 可以用 < 3_Unbounded Combination > 跟 < 4_Unbounded Permutation > 修改
        # 通常 < 4_Unbounded Permutation > 會快一些
    # 322. Coin Change
    # https://leetcode.com/problems/coin-change/description/
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
