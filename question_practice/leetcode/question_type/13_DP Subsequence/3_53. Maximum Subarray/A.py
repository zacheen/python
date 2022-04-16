import math
# my 原本想要用for迴圈DP 不過好像沒辦法
# Time Limit Exceeded
# class Solution:
#     def maxSubArray(self, nums):
#         # mem[i][j] 代表 nums[i:j] 的總和
#         # mem = [[0]*(len(nums)+1) for _ in range(len(nums)+1)]
#         max_sum = -math.inf
#         for i in range(len(nums)) : 
#             now_total = nums[i]
#             max_sum = max(now_total, max_sum) 
#             for j in range(i+1, len(nums)) :
#                 # mem[i][j] = now_total
#                 now_total += nums[j]
#                 max_sum = max(now_total, max_sum)
#         return max_sum

# My v2 fail 想法不對
# class Solution:
#     def maxSubArray(self, nums):

#         mem = [[0]*(len(nums)+1) for _ in range(len(nums)+1)]
#         def dp(i,j):
#             if i == j :
#                 return nums[i]
#             if mem[i][j] > 0:
#                 return mem[i][j]

#             # 這樣遇到負的會出問題
#             mem[i][j] = max(dp(i+1,j) + nums[i] , dp(i,j-1) + nums[j] , nums[i], nums[j] )
#             return mem[i][j]
#         return dp(0,len(nums)-1)

# my Runtime: 985 ms, faster than 46.21% of Python3
class Solution:
    def maxSubArray(self, nums):
        # 到i這個位置 最大的總和是多少
        before_max = nums[0]
        def rec(i):
            nonlocal before_max
            if i == 0 :
                return nums[0]
            ret = max(nums[i], rec(i-1)+nums[i])
            # print("nonlocal 更新 :", max(before_max, ret))
            before_max = max(before_max, ret)
            return ret
        rec(len(nums)-1)
        return before_max

# given ans greedy
# class Solution:
#     def maxSubArray(self, nums):
#         ans = -math.inf
#         summ = 0
#         # summ 是到目前為止 最大的總和
#         for num in nums:
#             summ += num
#             ans = max(ans, summ)  # 看目前的總和 跟之前的總和 哪個比較大
#             summ = max(summ, 0)   # 只要是負的一遇到正的 就從這個數字開始算
#         return ans



s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])) # 6
print(s.maxSubArray([5,4,-1,7,8])) # 23



