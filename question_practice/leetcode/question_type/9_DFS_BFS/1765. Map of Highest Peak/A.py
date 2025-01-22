# 1765. Map of Highest Peak
# https://leetcode.com/problems/map-of-highest-peak/description

from typing import List
import functools

# my 
from itertools import pairwise
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        nei_list = []
        for i1, l in enumerate(isWater):
            for i2, n in enumerate(l) :
                if n == 1 : 
                    nei_list.append((i1,i2))

        n1_len = len(isWater)
        n2_len = len(isWater[0])
        isWater = [[-1]*n2_len for _ in range(n1_len)]   
        dir_list = [0,1,0,-1,0]
        cou = 0
        while nei_list :
            new_nei_list = []
            for n1,n2 in nei_list :
                if n1 < 0 or n1 >= n1_len or n2 < 0 or n2 >= n2_len or isWater[n1][n2] >= 0:
                    continue
                isWater[n1][n2] = cou
                for d1, d2 in pairwise(dir_list) :
                    new_nei_list.append((n1+d1,n2+d2))
            nei_list = new_nei_list
            cou += 1
        return isWater

# given ans
# same concept

s = Solution()
print("ans :",s.highestPeak(isWater = [[0,1],[0,0]])) # 
print("ans :",s.highestPeak(isWater = [[0,0,1],[1,0,0],[0,0,0]])) # 



