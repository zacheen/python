from collections import Counter
# my Runtime: 71 ms, faster than 76.36% of Python3
# 概念是 已經從這個數字跑過了 就不要再跑重覆的數字
class Solution:
    def permuteUnique(self, nums):
        count = Counter(nums)
        ans = []
        
        def rec(mem, remain):
            if len(mem) == len(nums):
                ans.append(mem)
                return 
            
            for item, c in remain.items():
                if c > 0 :
                    pass_in_c = remain.copy()
                    pass_in_c[item] -= 1
                    rec(mem+[item], pass_in_c)
          
        rec([], count)
        return ans

# given ans
# 先sort 多判斷此數是否跟上一個數字相同 如果相同就不做
# class Solution:
#     def permuteUnique(self, nums):
#         ans = []
#         used = [False] * len(nums)

#         def dfs(path):
#             if len(path) == len(nums):
#                 ans.append(path.copy())
#                 return

#             for i, num in enumerate(nums):
#                 if used[i]:
#                     continue
#                 if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
#                     continue
#                 used[i] = True
#                 path.append(num)
#                 dfs(path)
#                 path.pop()
#                 used[i] = False

#         nums.sort()
#         dfs([])
#         return ans

s = Solution()
# print(s.permuteUnique(nums = [1,2,3]))
print(s.permuteUnique(nums = [1,1,2]))


