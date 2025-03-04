# 279. Perfect Squares
# https://leetcode.com/problems/perfect-squares/description/

from math import inf, sqrt

# my practice again : 898ms Beats81.35%
mem = [1]
def get_squ(n) :
    while mem[-1] < n :
        mem.append((len(mem)+1)**2)
    return mem
class Solution:
    def numSquares(self, n: int) -> int:
        dp=[0] + [inf]*n
        # print(get_squ(n))
        for poss_n in get_squ(n) :
            for i in range(poss_n, len(dp)):  # 從小到大
                if (t:=1+dp[i-poss_n]) < dp[i]:
                    dp[i] = t
        return dp[n]
   
# given ans : case by case (math)
class Solution: 
    def numSquares(self, n):
        if int(sqrt(n))**2 == n: return 1
        for j in range(int(sqrt(n)) + 1):
            if int(sqrt(n - j*j))**2 == n - j*j: return 2
            
        while n % 4 == 0: 
            n >>= 2
        if n % 8 == 7: return 4
        return 3

s = Solution()
# print(s.numSquares(12)) # 3
# print(s.numSquares(13)) # 2
print(s.numSquares(20))



