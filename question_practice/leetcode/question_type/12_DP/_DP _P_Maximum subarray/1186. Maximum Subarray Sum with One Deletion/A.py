# 1186. Maximum Subarray Sum with One Deletion
# https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/description/

from typing import List
from math import inf

# my using Kadane's Algorithm template : 7ms Beats99.47%
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        max_n = max(arr)
        if max_n <= 0:
            return max_n
        
        max_current = 0
        max_current_del1 = 0
        max_ans = 0
        min_n = 0
        for n in arr:
            if n < min_n :
                min_n = n
            max_current += n 
            # one number should be removed, or not contain this part
            if max_current < 0 :
                # concept is similar to outside part
                # find the max_sum where end at this number
                max_current_del1 += n # to link to this number all nubmer have to be added
                if (new_del := max_current - min_n) > max_current_del1 :
                    max_current_del1 = new_del
                max_current = 0
                min_n = 0
            # case : link two parts
            if (new_s := max_current_del1 + max_current) > max_ans :
                max_ans = new_s
            # case : remove the smallest num from max subarray
            if (new_s := max_current - min_n) > max_ans :
                max_ans = new_s
        return max_ans

s = Solution()
print("ans :",s.maximumSum([1,-2,0,3])) # 4
print("ans :",s.maximumSum([1,-2,-2,3])) # 3
print("ans :",s.maximumSum([-1,-1,-1,-1])) # -1
print("ans :",s.maximumSum([1,-4,-5,-2,5,0,-1,2])) # 7 [5,0,-1,2]
print("ans :",s.maximumSum([-8,7,-12,-1,0,11,-2,-3,4,-13,2,3,-6])) # 17 [7,-12,-1,0,11]



