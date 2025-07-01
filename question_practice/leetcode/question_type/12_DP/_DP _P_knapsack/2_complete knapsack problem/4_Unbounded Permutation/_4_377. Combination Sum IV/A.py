# 377. Combination Sum IV
# https://leetcode.com/problems/combination-sum-iv/description/

# my template 
class Solution:
    def combinationSum4(self, nums, target):
        dp = [1]+[0]*target
        for i in range(len(dp)):
            for n in nums :
                if (pre_i := i-n) >= 0 :
                    dp[i] += dp[pre_i]
        return dp[-1]

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

s = Solution()
print(s.combinationSum4(nums = [1,2,3], target = 4))
print(s.combinationSum4(nums = [9], target = 4))


