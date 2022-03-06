# My Runtime: 180 ms, faster than 59.40% of Python3 
from collections import Counter
class Solution:
    def singleNumber(self, nums):
        c = Counter(nums)
        for eachNum, val in c.items() :
            if val % 2 != 0:
                return eachNum
s = Solution()
print(s.singleNumber([4,1,2,1,2]))