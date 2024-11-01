# 1052. Grumpy Bookstore Owner
# https://leetcode.com/problems/grumpy-bookstore-owner/

from typing import List
import functools

# my 210ms Beats 83.16%
from collections import deque
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        sat_num = sum(cus if is_g==0 else 0 for cus, is_g in zip(customers, grumpy))
        
        extra_sat = 0
        max_extra_sat = 0
        extra_sat_list = deque()
        for cus, is_g in zip(customers, grumpy):
            if is_g == 1 :
                extra_sat += cus
                extra_sat_list.append(cus)
            else :
                extra_sat_list.append(0)
            if len(extra_sat_list) > minutes :
                extra_sat -= extra_sat_list.popleft()
            max_extra_sat = max(max_extra_sat, extra_sat)
            
        return sat_num + max_extra_sat 

# given ans

s = Solution()
# print(s.maxSatisfied(customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3))
print(s.maxSatisfied(customers = [4,10,10], grumpy = [1,1,0], minutes = 2))



