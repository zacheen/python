# 3440. Reschedule Meetings for Maximum Free Time II
# https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-ii/description/

from typing import List
from math import inf
import heapq

# my 339ms Beats37.39%
class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        free_len = [((e-s), i) for i, (s, e) in enumerate(zip(startTime+[eventTime], [0]+endTime))]
        heapq.heapify(free_len)
        max_3_free = [heapq.heappop(free_len) for _ in range(3)]
        max_3_free = [(-l,i) for l,i in max_3_free]
        # print(max_3_free)

        ans = 0
        for i, (s, e) in enumerate(zip(startTime[1:]+[eventTime], [0]+endTime[:-1])) :
            poss_free = s-e
            ori_len = endTime[i] - startTime[i]
            # check can move
            for free_len, indx in max_3_free :
                if ori_len <= free_len and i != indx and (i+1) != indx :
                    ans = max(ans, poss_free)
            ans = max(ans, poss_free - ori_len)
        return ans

# given ans (after my optimize): 87ms Beats100.00%
class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        freesArr = [(s-e) for (s, e) in zip(startTime+[eventTime], [0]+endTime)]
        
        ans = 0
        sortedFrees = sorted(freesArr)
        max_indx = len(sortedFrees)-1
        for i in range(len(startTime)):
            dur = endTime[i] - startTime[i]
            left_free = freesArr[i]
            right_free = freesArr[i+1]
            if (left_free + right_free + dur) <= ans:
                # 不會更長 所以跳過
                continue
            idx = max_indx

            if (max(left_free, right_free) == sortedFrees[idx]):
                idx -= 1
            if (min(left_free, right_free) == sortedFrees[idx]):
                idx -= 1
            total_free = left_free + right_free
            if idx >= 0 and sortedFrees[idx] >= dur:
                ans = max(ans, total_free + dur)
            else:
                ans = max(ans, total_free)
        return ans

s = Solution()
print("ans :",s.maxFreeTime(eventTime = 5, startTime = [1,3], endTime = [2,5])) # 2
print("ans :",s.maxFreeTime(eventTime = 10, startTime = [0,7,9], endTime = [1,8,10])) # 7
print("ans :",s.maxFreeTime(eventTime = 10, startTime = [0,3,7,9], endTime = [1,4,8,10])) # 6
print("ans :",s.maxFreeTime(eventTime = 52, startTime = [28,38], endTime = [38,41])) # 38



