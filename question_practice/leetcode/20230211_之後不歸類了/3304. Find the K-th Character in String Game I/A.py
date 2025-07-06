# 3304. Find the K-th Character in String Game I
# https://leetcode.com/problems/find-the-k-th-character-in-string-game-i

from typing import List
from math import inf

# my 0ms
op_dict = {chr(i):chr(i+1) for i in range(ord("a"), ord("z"))}
op_dict["z"] = "a"
word_gen = "a"
for _ in range(9):
    word_gen += "".join(op_dict[c] for c in word_gen)
# print(len(word_gen))
class Solution:
    def kthCharacter(self, k: int) -> str:
        return word_gen[k-1]

s = Solution()
print("ans :",s.kthCharacter(5)) # 
print("ans :",s.kthCharacter(10)) # 



