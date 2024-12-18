# 2593. Find Score of an Array After Marking All Elements
# https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements/description

from typing import List
import functools

# my 331ms Beats84.73%
class Solution:
    def findScore(self, nums: List[int]) -> int:
        ord_indx = [ (n,i) for i,n in enumerate(nums) ]
        ord_indx.sort()
        # print(ord_indx)

        mem_check = [False]*len(nums)
        ans = 0
        for n,i in ord_indx :
            if mem_check[i] :
                continue
            ans += n
            for each_i in range(max(0, i-1), min(len(nums), i+2)) :
                mem_check[each_i] = True
            # print("now :", n, i)
            # print(mem_check)
        return ans

# # given ans
# # same concept but using set to memery
# class Solution:
#     def findScore(self, nums: list[int]) -> int:
#         ans = 0
#         seen = set()
#         for num, i in sorted([(num, i) for i, num in enumerate(nums)]):
#             if i in seen:
#                 continue
#             seen.add(i - 1)
#             seen.add(i + 1)
#             seen.add(i)
#             ans += num
#         return ans
    
s = Solution()
print("ans :",s.findScore(nums = [2,1,3,4,5,2])) #7
print("ans :",s.findScore(nums = [2,3,5,1,3,2])) #5



