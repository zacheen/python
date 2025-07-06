# 3307. Find the K-th Character in String Game II
# https://leetcode.com/problems/find-the-k-th-character-in-string-game-ii

from typing import List
from math import inf

# my : 0ms
class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        bin_s = f'{k-1:b}'
        ans = 0
        for op, c in zip(operations, bin_s[::-1]):
            if c == "1" :
                ans += op
        return chr(ord('a')+(ans)%26)

s = Solution()
print("ans :",s.kthCharacter(k = 5, operations = [0,0,0])) # a
print("ans :",s.kthCharacter(k = 10, operations = [0,1,0,1])) # b



