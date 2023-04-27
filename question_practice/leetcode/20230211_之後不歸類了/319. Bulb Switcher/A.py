from typing import List
import functools

# my 
from math import sqrt
class Solution:
    def bulbSwitch(self, n: int) -> int:
        # bolbs = [False]+[True]*n
        # end_n = n+1
        # for i in range(2,end_n) :
        #     for indx in range(i,end_n,i) :
        #         bolbs[indx] = not bolbs[indx]
        # print(bolbs)
        # return bolbs.count(True)

        # 發現只有平方的數字會是 true
        # 因為只有奇數個因數
        return int(sqrt(n))

# given ans
# 一樣

s = Solution()
print(s.bulbSwitch(0))
print(s.bulbSwitch(1))
print(s.bulbSwitch(3))
print(s.bulbSwitch(10))
print(s.bulbSwitch(20))



