# 1863. Sum of All Subset XOR Totals
# 

from typing import List
from math import inf

# my 2ms
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        all_res = []
        for n in nums :
            all_res += [prev_res^n for prev_res in all_res]
            all_res.append(n)
        return sum(all_res)

# given ans : 0ms
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = 0
        for i in nums:
            ans |= i
        return ans << (len(nums)-1)

# # # this is subarray
# class Solution:
#     def subarrayXORSum(self, nums: List[int]) -> int:
#         mem = [0]
#         for n in nums :
#             mem.append(mem[-1]^n)
#         # print(mem)

#         ans = 0
#         for i, prev in enumerate(mem) :
#             for sub in mem[i+1:] :
#                 ans += sub ^ prev
#         return ans 

s = Solution()
print("ans :",s.subsetXORSum([1,3])) # 6
print("ans :",s.subsetXORSum([5,1,6])) # 28
print("ans :",s.subsetXORSum([3,4,5,6,7,8])) # 480



