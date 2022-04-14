# 計算 nums中挑選的數字相加 能不能組合出target

# 通用
def knapsack(nums, target):
    can_comb_set = {0}  # 裡面紀錄目前可以的組合
    for num in nums:
        for s in can_comb_set.copy() :
            can_comb_set.add(s + num)
    return target in can_comb_set

# 如果項目多 但target小 會比較快
# def knapsack(nums, target):
#     # dp[i] := True if i can be formed by nums so far
#     dp = [False] * (target + 1)
#     dp[0] = True

#     for num in nums:
#         for i in range(target, num - 1, -1):
#             dp[i] = dp[i] or dp[i - num]
#     return dp[target]



# print(knapsack([1,2,3,6], 5))
print(knapsack([1,2,4,8,16], 31))
# for i in range(1,32):
#     print(knapsack([1,2,4,8,16], i))
# print(knapsack([2,4,8,16], 17))
