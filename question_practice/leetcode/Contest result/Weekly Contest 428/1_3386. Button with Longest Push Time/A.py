# 3386. Button with Longest Push Time
# https://leetcode.com/problems/button-with-longest-push-time/description/

from typing import List
import functools

# my 0ms Beats100.00%
class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        last_cou = 0
        max_cou = 0
        max_indx = 0
        for i, cou in events :
            this_cou = cou - last_cou
            if this_cou > max_cou :
                max_indx = i
                max_cou = this_cou
            elif this_cou == max_cou :
                max_indx = min(i, max_indx)
            last_cou = cou
        return max_indx

s = Solution()
print("ans :",s.buttonWithLongestTime([[10,5],[1,7]])) # 10



