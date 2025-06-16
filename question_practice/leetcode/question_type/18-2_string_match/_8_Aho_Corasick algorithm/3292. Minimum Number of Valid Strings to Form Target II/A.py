# 3292. Minimum Number of Valid Strings to Form Target II
# https://leetcode.com/problems/minimum-number-of-valid-strings-to-form-target-ii/description/

from typing import List
from math import inf

class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word):
        now_n = self.root
        for c in word :
            if c not in now_n :
                now_n[c] = {}
            now_n = now_n[c]
        now_n[None] = None

    # None : return at the middle
    # else : return the end node
    def find_end(self, prefix) :
        now_n = self.root
        for c in prefix :
            if c not in now_n :
                return None
            now_n = now_n[c]
        return now_n
    
class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        

s = Solution()
print("ans :",s.minValidStrings(words = ["abc","aaaaa","bcdef"], target = "aabcdabc")) # 3
print("ans :",s.minValidStrings(words = ["abababab","ab"], target = "ababaababa")) # 2
print("ans :",s.minValidStrings(words = ["abcdef"], target = "xyz")) # -1
print("ans :",s.minValidStrings(words = ["a","babc"], target = "aacab")) # -1
print("ans :",s.minValidStrings(words = ["babc"], target = "a")) # -1
print("ans :",s.minValidStrings(words = ["cab","bacbbbbcababca","a"], target = "ccbacbbaaa")) # 6
print("ans :",s.minValidStrings(words = ["caacbbbbbcaccb","baccccb","aacabcca"], target = "aacaacbabb")) # 5 : aac, aac, ba, b, b
