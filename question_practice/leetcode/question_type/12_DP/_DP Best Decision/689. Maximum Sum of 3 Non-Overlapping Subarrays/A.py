# 689. Maximum Sum of 3 Non-Overlapping Subarrays
# https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/description

from typing import List
import functools

# my dp 121ms Beats26.85%
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        # making range sum
        now_sum = sum(nums[0:k])
        s_list = [now_sum]
        for n1, n2 in zip(nums, nums[k:]) :
            now_sum += n2 - n1
            s_list.append(now_sum)

        space = len(nums) - k + 1
        dp = [(0, []) for _ in range(space)] # (sum, indx_list)
        for _ in range(3) :
            new_dp = [(0, []) for _ in range(space)]
            for i, new_c in enumerate(s_list) :
                if i == 0 :
                    new_dp[i] = (new_c, [0])
                    continue
                
                # not using this range
                last_sum, last_i = new_dp[i-1]
                # using this range
                if i >= k :
                    this_sum, this_i = dp[i-k]
                else :
                    # 沒有之前的
                    this_sum, this_i = 0, []
                this_sum += new_c
                if this_sum > last_sum :
                    this_i = this_i.copy()
                    this_i.append(i)
                    new_dp[i] = (this_sum, this_i)
                else :
                    new_dp[i] = new_dp[i-1]
            dp = new_dp
        return dp[-1][1]
    
# # my dp recursion version 318ms Beats5.75%
# class Solution:
#     def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
#         # making range sum
#         now_sum = sum(nums[0:k])
#         s_list = [now_sum]
#         for n1, n2 in zip(nums, nums[k:]) :
#             now_sum += n2 - n1
#             s_list.append(now_sum)
        
#         @functools.lru_cache(None)
#         def best_comb(st_indx, comb) : # end_indx not included
#             if st_indx < 0 or comb <= 0:
#                 return 0, []
#             # using this range
#             us_sum, us_list = best_comb(st_indx-k, comb-1)
#             us_sum += s_list[st_indx]
#             us_list.append(st_indx)
#             # not using this range
#             n_us_sum, n_us_list = best_comb(st_indx-1, comb)
#             if us_sum > n_us_sum :
#                 # print(st_indx, comb, us_sum, us_list)
#                 return us_sum, us_list.copy()
#             else :
#                 # print(st_indx, comb, n_us_sum, n_us_list)
#                 return (n_us_sum, n_us_list.copy())

#         return best_comb(len(nums)-k, 3)


# given ans 28ms Beats56.30%
# 因為剛好3個 所以可以定中間 找左右最佳
class Solution:
    def maxSumOfThreeSubarrays(self, nums: list[int], k: int) -> list[int]:
        n = len(nums) - k + 1
        sums = [0] * n
        l = [0] * n
        r = [0] * n

        # making range sum
        summ = 0
        for i, num in enumerate(nums):
            summ += num
            if i >= k:
                summ -= nums[i - k]
            if i >= k - 1:
                sums[i - k + 1] = summ

        # finding the max sums from left and from right
        maxIndex = 0
        for i in range(n):
            if sums[i] > sums[maxIndex]:
                maxIndex = i
            l[i] = maxIndex
        maxIndex = n - 1
        for i in range(n - 1, -1, -1):
            if sums[i] >= sums[maxIndex]:
                maxIndex = i
            r[i] = maxIndex

        ans_mid_i = 0
        max_ans = 0
        for i in range(k, n - k):
            #           左邊可以的最大 + 中間 + 右邊可以的最大
            this_sum = sums[l[i - k]] + sums[i] + sums[r[i + k]]
            if max_ans < this_sum :
                ans_mid_i = i
                max_ans = this_sum
        return [l[ans_mid_i - k], ans_mid_i, r[ans_mid_i + k]]
    
# given ans 11ms Beats99.73%
# concept is similar to # my dp, but better implement method
from itertools import accumulate
class Solution:
    def maxSumOfThreeSubarrays(self, nums, k):
        sm1 = sm2 = sm3 = 0
        idx1 = idx2 = idx3 = None
        acc = list(accumulate(nums, initial = 0))
        for i, (a0,a1,a2,a3) in enumerate(zip(acc, acc[k:],acc[2*k:],acc[3*k:])):
            # sm1 為目前最好的 sum range
            new_sm1 = a1 - a0
            if new_sm1 > sm1:
                sm1 = new_sm1
                idx1 = i
            new_sm2 = sm1 + a2 - a1
            if new_sm2 > sm2:
                sm2 = new_sm2
                idx2 = (idx1, i+k)
            new_sm3 = sm2 + a3 - a2
            if new_sm3 > sm3:
                sm3 = new_sm3
                idx3 = (*idx2, i+2*k)
        return idx3

# # former explain version (slower)
# from itertools import accumulate
# class Solution:
#     def maxSumOfThreeSubarrays(self, nums, k):
#         # making range sum
#         now_sum = sum(nums[0:k])
#         s_list = [now_sum]
#         for n1, n2 in zip(nums, nums[k:]) :
#             now_sum += n2 - n1
#             s_list.append(now_sum)
        
#         sm1 = sm2 = sm3 = 0
#         idx1 = idx2 = idx3 = None
#         for i, (s1,s2,s3) in enumerate(zip(s_list,s_list[k:],s_list[2*k:])):
#             # sm1 為目前最好的 sum range
#             if s1 > sm1:
#                 sm1 = s1
#                 idx1 = i
#             new_sm2 = sm1 + s2
#             if new_sm2 > sm2:
#                 sm2 = new_sm2
#                 idx2 = (idx1, i+k)
#             new_sm3 = sm2 + s3
#             if new_sm3 > sm3:
#                 sm3 = new_sm3
#                 idx3 = (*idx2, i+2*k)
#         return idx3

s = Solution()
print("ans :",s.maxSumOfThreeSubarrays(nums = [1,2,1,2,6,7,5,1], k = 2)) # [0,3,5]
# print("ans :",s.maxSumOfThreeSubarrays(nums = [1,2,1,2,1,2,1,2,1], k = 2)) # [0,2,4]
# print("ans :",s.maxSumOfThreeSubarrays(nums = [1,2,3,1,2,3,1,2,3,1,2,3,1], k = 3)) # [0,3,6]
# print("ans :",s.maxSumOfThreeSubarrays([4,3,2,1], 1)) # [0,1,2]
# print("ans :",s.maxSumOfThreeSubarrays([18,11,14,7,16,4,18,11,4,8], 2)) # [0,3,6]
# print("ans :",s.maxSumOfThreeSubarrays([7,13,20,19,19,2,10,1,1,19], 3)) # [1,4,7]



