# 3685. Subsequence Sum After Capping Elements
# https://leetcode.com/problems/subsequence-sum-after-capping-elements/description/

from typing import List
from math import inf

# my 3935ms Beats41.61%
# fail 1 : didn't limit the maximum sum
class Solution:
    def subsequenceSumAfterCapping(self, nums: List[int], k: int) -> List[bool]:
        nums.sort()
        nums_i = 0
        all_pos_sum = set([0])
        ans = []
        for x in range(1, len(nums)+1):
            while nums_i < len(nums) and nums[nums_i] == x :
                nums_i += 1
                for all_s in all_pos_sum.copy() :
                    if (new_sum := all_s + x) <= k :
                        all_pos_sum.add(new_sum)
            rem_x_cnt = len(nums) - nums_i
            flag_find_ans = False
            for rem in range(k,k-(rem_x_cnt*x)-1,-x) :
                if rem in all_pos_sum :
                    ans.append(True)
                    flag_find_ans = True
                    break
            if not flag_find_ans :
                ans.append(False)
        return ans
  

s = Solution()
print("ans :",s.subsequenceSumAfterCapping(nums = [4,3,2,4], k = 5)) # 
print("ans :",s.subsequenceSumAfterCapping(nums = [1,2,3,4,5], k = 3)) # 
# print("ans :",s.subsequenceSumAfterCapping(nums = [4,3,2,4], k = 5)) # 



