# 31. Next Permutation
# https://leetcode.com/problems/next-permutation/description/

from itertools import permutations
for ex in list(permutations([1,2,3,4,5],5)):
    print(ex)
from typing import List
from math import inf

# my 
class Solution:
    def nextPermutation(self, nums):
        # find the position that the previous one is smaller than the rear one
        start_pos = len(nums)-2
        while start_pos >= 0 and nums[start_pos] > nums[start_pos+1]:
            start_pos -= 1

        # corner case
        if start_pos == -1 :
            nums.sort()
            return nums
        
        # find the next bigger number
        smaller_num = nums[start_pos]
        next_big_indx = start_pos+1
        # optimized version
        for i in range(len(nums)-1, start_pos, -1) :
            now_n = nums[i]
            if now_n > smaller_num :
                next_big_indx = i
                break

        # for i in range(start_pos+1, len(nums)) :
        #     now_n = nums[i]
        #     if now_n > smaller_num and now_n < next_big :
        #         next_big = now_n
        #         next_big_indx = i

        
        # sort the remain part
        nums[start_pos], nums[next_big_indx] = nums[next_big_indx], nums[start_pos]
        print(nums[:start_pos+1], sorted(nums[start_pos+1:]))
        return nums[:start_pos+1] + sorted(nums[start_pos+1:])

s = Solution()
# print("ans :",s.nextPermutation([1,2,3])) # 
# print("ans :",s.nextPermutation([3,2,1])) # 
# print("ans :",s.nextPermutation([1,1,5])) # 
print("ans :",s.nextPermutation([1,3,2])) # 



