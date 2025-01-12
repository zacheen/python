# 3418. Maximum Amount of Money Robot Can Earn
# https://leetcode.com/problems/maximum-amount-of-money-robot-can-earn/description/

from typing import List
import functools

# my opt 1768ms Beats100.00%
from math import inf
class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        mem = [[-inf,-inf,-inf,-inf] for _ in range(len(coins[0]))]
        mem[0] = [0,0,0,-inf]
        for this_row in coins :
            for n2, c in enumerate(this_row) :
                for n3 in range(3):
                    # from up         # up & not use, up & use      
                    mem[n2][n3] = max(mem[n2][n3]+c, mem[n2][n3+1])
                    # from left
                    if n2 > 0 :           # best up  , left & not use , left & use
                        mem[n2][n3] = max(mem[n2][n3], mem[n2-1][n3]+c, mem[n2-1][n3+1])
        return mem[-1][0]
    
# # my during contest : easier to understand
# # wrong : logic Error : forget to max(up, left)
# # wrong : logic Error
    # [[0,0,0] for _ in range(len(coins[0]))]
# # wrong : Syntax Error
    # [[0,0,0] + [-inf,-inf,-inf] for _ in range(len(coins[0]))]

# from math import inf
# class Solution:
#     def maximumAmount(self, coins: List[List[int]]) -> int:
#         mem = [[0,0,0]] + [[-inf,-inf,-inf] for _ in range(len(coins[0]))]
        
#         for n1 in range(len(coins)) :
#             new_mem = [[-inf,-inf,-inf] for _ in range(len(coins[0]))]
#             for n2, c in enumerate(coins[n1]) :
#                 # from up
#                 if c >= 0 :
#                     for n3 in range(3):
#                         new_mem[n2][n3] = mem[n2][n3] + c
#                 else :
#                     for n3 in range(3):
#                         if n3 == 2 :
#                             new_mem[n2][n3] = mem[n2][n3] + c
#                         else :
#                             new_mem[n2][n3] = max(mem[n2][n3] + c, mem[n2][n3+1]) # + c, since c is neg  
#                 # from left
#                 if n2 >= 1 :
#                     if c >= 0 :
#                         for n3 in range(3):
#                             new_mem[n2][n3] = max( new_mem[n2][n3], new_mem[n2-1][n3]+c )
#                     else :
#                         for n3 in range(3):
#                             if n3 == 2 :
#                                 new_mem[n2][n3] = max(new_mem[n2][n3], new_mem[n2-1][n3]+c)
#                             else :
#                                 new_mem[n2][n3] = max(new_mem[n2][n3], max(new_mem[n2-1][n3] + c, new_mem[n2-1][n3+1])) # + c, since c is neg
#             mem = new_mem
#             # print(new_mem)
#         return mem[-1][0]

# given ans
# my opt is better

s = Solution()
print("ans :",s.maximumAmount([[0,1,-1],[1,-2,3],[2,-3,4]])) # 8
print("ans :",s.maximumAmount([[0,-1,-1,-1],[1,-2,-1,3],[-1,-1,-1,-1],[2,-3,-1,4]])) # 7
print("ans :",s.maximumAmount([[10,10,10],[10,10,10]])) # 40
print("ans :",s.maximumAmount([[-7,12,12,13],[-6,19,19,-6],[9,-2,-10,16],[-4,14,-10,-9]])) # 60



