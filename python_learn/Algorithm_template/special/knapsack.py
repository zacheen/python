# 計算 nums中挑選的數字相加 能不能組合出target

from math import inf

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
    return dp[target]

# print(knapsack_01_for_target([1,2,3,6], 5))
# print(knapsack_01_for_target([1,2,4,8,16], 31))
# print([knapsack_01_for_target([1,2,4,8,16], i) for i in range(1,32)])
# print(knapsack_01_for_target([1,2,5], 11))

## take any amount ################################################################
# classic : 322. Coin Change
# https://leetcode.com/problems/coin-change/description/

def knapsack_several(nums, target):
    dp=[0] + [inf]*target
    for n in nums:
        for i in range(n, len(dp)):  # 從小到大
            if (t:=1+dp[i-n]) < dp[i]:
                dp[i] = t
    if dp[target]==inf:
        return -1
    else :
        return dp[target]
    
# def knapsack_several_sort(nums, target): # not correct
