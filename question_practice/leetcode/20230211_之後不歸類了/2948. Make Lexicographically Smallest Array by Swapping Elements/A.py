# 2948. Make Lexicographically Smallest Array by Swapping Elements
# https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements/description

from typing import List
import functools

# my 279ms Beats83.33%
from math import inf
class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        nums_i = [[n,i] for i,n in enumerate(nums)]
        nums_i.sort()
        nums_i.append([inf,None])

        last_n = nums_i[0][0]
        indx_list = []
        num_list = []
        for n,i in nums_i :
            if n-last_n <= limit :
                indx_list.append(i)
                num_list.append(n)
            else :
                indx_list.sort()
                for for_i,for_n in zip(indx_list, num_list) :
                    nums[for_i] = for_n
                indx_list = [i]
                num_list = [n]
            last_n = n
        return nums

# given ans
# same concept

s = Solution()
print("ans :",s.lexicographicallySmallestArray(nums = [1,5,3,9,8], limit = 2)) # [1,3,5,8,9]
print("ans :",s.lexicographicallySmallestArray(nums = [1,7,6,18,2,1], limit = 3)) # [1,6,7,18,1,2]
print("ans :",s.lexicographicallySmallestArray(nums = [1,7,28,19,10], limit = 3)) # [1,7,28,19,10]



