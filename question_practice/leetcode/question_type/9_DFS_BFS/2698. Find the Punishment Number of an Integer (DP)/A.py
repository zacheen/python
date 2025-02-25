# 2698. Find the Punishment Number of an Integer
# https://leetcode.com/problems/find-the-punishment-number-of-an-integer

from typing import List
from math import inf
from functools import lru_cache
from collections import Counter

# my 32ms Beats66.80%
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        cou = Counter(tiles)
        def dfs():
            nonlocal cou
            poss_comb = 0
            for diff_c, num in cou.items(): # only use key, so wont generate the same string
                if num == 0 : continue
                cou[diff_c] -= 1 # use diff_c as this word
                poss_comb += 1 + dfs() # 1 is append empty string
                cou[diff_c] += 1 # recover
            return poss_comb
        return dfs()

# given ans : 0ms Beats100.00%
# this method is related with math
import math
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        tile_counter = Counter(tiles)
        result_counter = Counter([0])
        for tc in tile_counter.values():
            for l, n in list(result_counter.items()):
                for i in range(1, tc+1):
                    result_counter[i+l] += math.comb(i+l, i)*n
        return sum(result_counter.values())-1

s = Solution()
print("ans :",s.numTilePossibilities("AAB")) # 8
print("ans :",s.numTilePossibilities("AAABBC")) # 188
print("ans :",s.numTilePossibilities("V")) # 1



