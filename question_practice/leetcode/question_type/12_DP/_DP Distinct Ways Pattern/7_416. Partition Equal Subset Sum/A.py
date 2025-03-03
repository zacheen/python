# my Runtime: 1625 ms, faster than 48.84% of Python3
# 全部加起來除2 看有沒有組合可以加起來等於這個數字
# class cache:
#     def __init__(self, func):
#         self.func = func
#         self.data = {}

#     def __call__(self, *args, **kwargs):
#         func = self.func
#         data = self.data
#         key = f'{func.__name__}-{str(args)}-{str(kwargs)})'
#         if key in data:
#             result = data.get(key)
#         else:
#             result = func(*args, **kwargs)
#             data[key] = result
#         return result

# class Solution:
#     def canPartition(self, nums):
#         total = sum(nums)
#         if total % 2 != 0 :
#             return False
#         total = total // 2

#         # 找出加起來是 total 的組合
#         # 可以記錄到目前這個位置 是不可能組合出哪些數字的 只是我沒想到可以快這麼多
#         @cache
#         def dfs(indx, remain):
#             if remain == 0 :
#                 return True

#             if remain < 0 :
#                 return False

#             for i in range(indx, len(nums)) :
#                 if dfs(i+1, remain-nums[i]) == True :
#                     return True

#         if dfs(0, total) :
#             return True
#         else :
#             return False

# given ans
# 就快一點 Runtime: 1648 ms, faster than 48.49% of Python3
# 概念跟 dfs cache 差不多
# class Solution:
#     def canPartition(self, nums):
#         summ = sum(nums)
#         if summ & 1:
#             return False
#         return self.knapsack_(nums, summ // 2)

#     def knapsack_(self, nums, subsetSum):
#         n = len(nums)
#         # dp[i][j] 代表nums[:i]可以組合出j這個數字
#         dp = [[False] * (subsetSum + 1) for _ in range(n + 1)]
#         dp[0][0] = True

#         for i in range(1, n + 1):
#             num = nums[i - 1]
#             for j in range(subsetSum + 1):
#                 # j 可以想成是目前的總和
#                 if j < num:
#                     # 前面一個位置可以組合的數字 到現在這個位置一定也可以
#                     dp[i][j] = dp[i - 1][j]
#                 else:
#                     # j - num == 目前的總和 - 現在新的數字 
#                     # dp[i - 1][j - num] 代表之前的組合+新的數字 能不能組合成新的組合
#                     dp[i][j] = dp[i - 1][j] or dp[i - 1][j - num]

#         return dp[n][subsetSum]

# given ans  已加入 template
# Runtime: 890 ms, faster than 67.23% of Python3
# 用bucket來for "for i in range(subsetSum, num - 1, -1)"
# 但時間複雜度 應該是for每個項目會比較快 ?  最下面有優化結果 的確比較快
# class Solution:
#     def canPartition(self, nums):
#         summ = sum(nums)
#         if summ & 1:
#             return False
#         return self.knapsack_(nums, summ // 2)
        
#     def knapsack_(self, nums, subsetSum):
#         # dp[i] := True if i can be formed by nums so far
#         dp = [False] * (subsetSum + 1)
#         dp[0] = True

#         for num in nums:
#             for i in range(subsetSum, num - 1, -1):
#                 dp[i] = dp[i] or dp[i - num]

#         return dp[subsetSum]


# 使用項目優化
# Runtime: 727 ms, faster than 72.39% of Python3
class Solution:
    def canPartition(self, nums):
        summ = sum(nums)
        if summ & 1:
            return False
        return self.knapsack_(nums, summ // 2)
        
    def knapsack_(self, nums, subsetSum):
        can_comb_set = {0}

        for num in nums:
            for s in can_comb_set.copy() :
                can_comb_set.add(s + num)

        return subsetSum in can_comb_set


s = Solution()
# print(s.canPartition(nums = [1,5,11,5]))
# print(s.canPartition(nums = [1,2,3,5]))
long_list = [4,8,16,32,64]
long_list = long_list*48 + [2, 0]
print(long_list)
print(s.canPartition(long_list))


