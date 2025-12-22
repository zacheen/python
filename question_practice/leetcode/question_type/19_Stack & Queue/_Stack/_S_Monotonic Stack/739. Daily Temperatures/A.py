# 739. Daily Temperatures
# https://leetcode.com/problems/daily-temperatures

from typing import List
from math import inf

# my 
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0]*len(temperatures)
        for i, t in enumerate(temperatures) :
            while stack and t > temperatures[stack[-1]] :
                pre_i = stack.pop()
                ans[pre_i] = i-pre_i
            stack.append(i)
        return ans

s = Solution()
print("ans :",s.dailyTemperatures([73,74,75,71,69,72,76,73])) # 
print("ans :",s.dailyTemperatures([30,40,50,60])) # 
print("ans :",s.dailyTemperatures([30,60,90])) # 



