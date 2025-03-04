# 1449. Form Largest Integer With Digits That Add up to Target
# 

from typing import List
from math import inf

# my 125ms Beats50.88%
class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        # def comp(cou1, cou2):
        #     for i in range(9,0,-1) :
        #         if cou1[i] > cou2[i] :
        #             return True
        #         elif cou1[i] < cou2[i] :
        #             return False
        #     return False
        
        dp=[[0,[0]*10]] + [[-inf,[0]*10] for _ in range(target)] # [位數, sum, mem]
        for n, c in zip(range(1,10), cost):
            for i in range(c, len(dp)):  # 從小到大
                if (l:=1+dp[i-c][0]) >= dp[i][0]:
                    new_cou = dp[i-c][1].copy()
                    new_cou[n] += 1
                    dp[i] = (l, new_cou)
                # elif l == dp[i][0] and comp(new_cou, dp[i][1]) :
                #     dp[i] = (l, new_cou)
        final_l, final_cou = dp[target]
        if final_l == -inf :
            return "0"
        else :
            return "".join([str(i)*final_cou[i] for i in range(9,0,-1)])

# optimized by given ans : 67ms Beats91.23%
class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:        
        dp=[""] + [None]*target # [位數, sum, mem]
        for n, c in zip(range(1,10), cost):
            for i in range(c, len(dp)):  # 從小到大
                if dp[i-c] == None :
                    continue
                elif dp[i] == None :
                    dp[i] = str(n) + dp[i-c]
                elif 1+len(dp[i-c]) >= len(dp[i]):
                    dp[i] = str(n) + dp[i-c]
        if dp[target] == None :
            return "0"
        else :
            return dp[target]

s = Solution()
print("ans :",s.largestNumber(cost = [4,3,2,5,6,7,2,5,5], target = 9)) # 7772
print("ans :",s.largestNumber(cost = [7,6,5,5,5,6,8,7,8], target = 12)) # 85
print("ans :",s.largestNumber(cost = [2,4,6,2,4,6,4,4,4], target = 5)) # 0



