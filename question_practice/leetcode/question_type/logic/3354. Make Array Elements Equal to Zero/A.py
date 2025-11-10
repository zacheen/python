# 3354. Make Array Elements Equal to Zero
# https://leetcode.com/problems/make-array-elements-equal-to-zero

from typing import List
from math import inf

# my 28ms Beats99.51%
class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        # we have to select the index that left sum == right sum
        # Or if diff is one, we can choose one direction
        ans_cnt = 0
        total = sum(nums)
        now_sum = 0
        for n in nums :
            now_sum += n

            if n == 0 :
                # left dir
                diff = now_sum - (total - now_sum)
                if diff == 0 or diff == 1 :
                    ans_cnt += 1

                # right fir
                diff = -diff
                if diff == 0 or diff == 1 :
                    ans_cnt += 1
        return ans_cnt

s = Solution()
print("ans :",s.countValidSelections([1,0,2,0,3])) # 2
print("ans :",s.countValidSelections([2,3,4,0,4,1,0])) # 0



