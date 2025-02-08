# 3439. Reschedule Meetings for Maximum Free Time I
# https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-i/description/

from typing import List
from math import inf

from collections import deque

# my v2 23ms Beats99.70%
class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        startTime = startTime+[eventTime]
        endTime = [0]+endTime
        free_len = [(s-e) for s, e in zip(startTime, endTime)]
        total_free = sum(free_len[:k+1])
        max_free = total_free
        for indx, t in enumerate(free_len[k+1:]) :
            total_free += (t - free_len[indx])
            if total_free > max_free :
                max_free = total_free
        return max_free

# my v1 : 75ms Beats38.15%
class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        startTime = [0] + startTime + [eventTime]
        endTime = [0] + endTime + [eventTime]
        
        # 把 k 個往前推
        stack = deque()
        total_l = 0
        left = 0
        max_free = 0
        for s,e in zip(startTime, endTime) :
            if len(stack) >= k :
                # cal free time
                this_f = s - (left + total_l)
                if this_f > max_free :
                    max_free = this_f
                
                # update
                left, l = stack.popleft()
                total_l -= l
            # update
            l = e-s
            total_l += l
            stack.append((e, l))
        return max_free

s = Solution()
print("ans :",s.maxFreeTime(eventTime = 5, k = 1, startTime = [1,3], endTime = [2,5])) # 2
print("ans :",s.maxFreeTime(eventTime = 10, k = 1, startTime = [0,2,9], endTime = [1,4,10])) # 6
print("ans :",s.maxFreeTime(eventTime = 5, k = 2, startTime = [0,1,2,3,4], endTime = [1,2,3,4,5])) # 0
print("ans :",s.maxFreeTime(eventTime = 21, k = 2, startTime = [18,20], endTime = [20,21])) # 0



