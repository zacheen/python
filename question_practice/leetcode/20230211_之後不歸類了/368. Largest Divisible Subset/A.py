# 368. Largest Divisible Subset
# https://leetcode.com/problems/largest-divisible-subset/description/

# my practice again : 55ms Beats100.00%
# "distinct" positive integers
    # so I don't have to optimize, the numbers appear twice
class Solution:
    def largestDivisibleSubset(self, nums):
        nums.sort()
        mem = []
        def check_valid(n, check_len) :
            for prev_n in mem[check_len] :
                if n % prev_n == 0 :
                    return (True, mem[check_len][prev_n])
            return (False, [])

        ans = None
        for n in nums :
            # 找最長可以接的長度
            left, right = 0, len(mem) # right 通常會超出界線(因為執行的時候不會執行到這個數字) # 但是最後 l 有可能會超出範圍
            path = [n]
            while left < right:
                mid = (left + right) // 2
                ret = check_valid(n, mid)
                if ret[0] :
                    left = mid + 1
                    path = ret[1] + [n]
                else:
                    right = mid 
            if left == len(mem) :
                mem.append({n : path})
                ans = path
            else :
                mem[left][n] = path
        return ans

# # given ans
# # 我是用 recursive 的寫法
# # 但他是用 DP 的寫法 (比較省記憶體)
# class Solution:
#     def largestDivisibleSubset(self, nums):
#         n = len(nums)
#         ans = []
#         count = [1] * n
#         prevIndex = [-1] * n
#         maxCount = 0
#         index = -1

#         nums.sort()
#         for i, num in enumerate(nums):
#             for j in reversed(range(i)):
#                 if num % nums[j] == 0 and count[i] < count[j] + 1:
#                     count[i] = count[j] + 1
#                     prevIndex[i] = j
#             # 這個是為了下面的組合出原本的路徑
#             if count[i] > maxCount:
#                 maxCount = count[i]
#                 index = i

#         while index != -1:
#             ans.append(nums[index])
#             index = prevIndex[index]

#         return ans

s = Solution()
# print(s.largestDivisibleSubset(nums = [1,2,3]))
# print(s.largestDivisibleSubset(nums = [1,2,4,8]))
print(s.largestDivisibleSubset(nums = [1,2,3,4,6,12]))



