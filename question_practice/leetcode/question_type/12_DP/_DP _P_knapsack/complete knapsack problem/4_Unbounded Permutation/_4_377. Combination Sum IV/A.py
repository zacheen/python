# 377. Combination Sum IV
# https://leetcode.com/problems/combination-sum-iv/description/

# My Runtime: 37 ms, faster than 92.60% of Python3
class Solution:
    def combinationSum4(self, nums, target):
        nums.sort()

        # DP 回傳 now_target 共有幾種組合
        # @cache
        def DP(now_target):
            if now_target == 0 :
                return 1
            
            ret = 0
            for n in nums :
                sub = now_target - n
                if sub >= 0 :
                    ret += DP(sub)
                else :  # 前提是要先 sort  (如果深度很深的話會比較快 就是都是小的數字的時候)
                    break
            return ret

        return DP(target)

# my 
# 其實 backtrack 也可以想成某種 DP
# 主要差在 DP 通常是處理會經過相同的項目的問題  而 backtrack 不會
# 一開始我以為要回傳所有組合...
# 不過還是留著當記錄
# class Solution:
#     def combinationSum4(self, nums, target):
#         nums.sort()

#         # DP 回傳 now_target 共有幾種組合
#         # @cache
#         def DP(now_target):
#             if now_target == 0 :
#                 return [[]]
            
#             ret = []
#             for n in nums :
#                 sub = now_target - n
#                 if sub >= 0 :
#                     for comb in DP(sub) :
#                         ret.append( comb + [n])
#                 else :  # 前提是要先 sort
#                     break
#             return ret

# given ans
# 觀念一樣 只是比較優雅的寫法
# class Solution:
#     def combinationSum4(self, nums, target):
#         dp = [1] + [-1] * target

#         def dfs(target):
#             if target < 0:
#                 return 0
#             if dp[target] != -1:
#                 return dp[target]

#             dp[target] = sum(dfs(target - num) for num in nums)   # (O) 優雅
#             return dp[target]

#         return dfs(target)

s = Solution()
print(s.combinationSum4(nums = [1,2,3], target = 4))
print(s.combinationSum4(nums = [9], target = 4))


