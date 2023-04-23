from typing import List
import functools

# my 
class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        return (arrivalTime+delayedTime)%24

# given ans
# 一樣

s = Solution()
print(s.findDelayedArrivalTime(arrivalTime = 15, delayedTime = 5 ))
print(s.findDelayedArrivalTime(arrivalTime = 13, delayedTime = 11 ))



