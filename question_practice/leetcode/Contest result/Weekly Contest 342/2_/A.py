from typing import List
import functools

# my 
class Solution:
    def sumOfMultiples(self, n: int) -> int:
        ans = 0
        for i in range(n+1) :
            if i%3==0 or i%5==0 or i%7==0 :
                ans += i
        return ans

# given ans

s = Solution()
print(s.sumOfMultiples(7))
print(s.sumOfMultiples(10))
print(s.sumOfMultiples(9))



