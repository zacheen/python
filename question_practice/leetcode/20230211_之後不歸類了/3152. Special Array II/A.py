# 3152. Special Array II
# https://leetcode.com/problems/special-array-ii/description

from typing import List
import functools

# combine 31ms Beats93.98%
from itertools import pairwise
class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        cou = 0
        def return_sta(increase):
            nonlocal cou
            cou += increase
            return cou
        nums_sta = [0]+[return_sta(0) if (f-b)%2 else return_sta(1) for f,b in pairwise(nums)]
        return [ nums_sta[f] == nums_sta[t] for f,t in queries]

# # my 
# import bisect
# from itertools import pairwise
# class Solution:
#     def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
#         not_parity_list = []
#         for i,(f,b) in enumerate(pairwise(nums)):
#             if (f-b)%2 == 0 :
#                 not_parity_list.append(i+0.5)
#         # print(not_parity_list)
#         return [bisect.bisect_left(not_parity_list, f) == bisect.bisect_right(not_parity_list, t) for f,t in queries]

# # given ans
# from itertools import pairwise
# class Solution:
#     def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
#         ans = []
#         id = 0
#         # parityIds[i] := the id of the parity group that nums[i] belongs to
#         parityIds = [id]
#         for a, b in pairwise(nums):
#             if a % 2 == b % 2:
#                 id += 1
#             parityIds.append(id)
#         print(parityIds)

#         for _from, to in queries:
#             ans.append(parityIds[_from] == parityIds[to])
#         return ans
    


s = Solution()
print("ans :",s.isArraySpecial(nums = [3,4,1,2,6], queries = [[0,4]]))
print("ans :",s.isArraySpecial(nums = [4,3,1,6], queries = [[0,2],[2,3]]))
print("ans :",s.isArraySpecial(nums = [1,3,1,3,2,4,2,4,1], queries = [[0,2],[2,3]]))
# print("ans :",s.isArraySpecial())



