# 820. Short Encoding of Words
# https://leetcode.com/problems/short-encoding-of-words/description/

from typing import List
from math import inf

# my v2 : 51ms Beats62.50%
class Trie:
    def __init__(self):
        self.root = {}
        self.cou = 0

    def insert(self, word):
        now_n = self.root
        for i, c in enumerate(word) :
            if c not in now_n :
                now_n[c] = {}
            now_n = now_n[c]
            if None in now_n :
                self.cou -= (i+2)
                del(now_n[None])
        if len(now_n) == 0 : # 這個點是底
            now_n[None] = None
            self.cou += len(word)+1

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        trie = Trie()
        for s in words :
            trie.insert(s[::-1])
        return trie.cou

# my v1 : 51ms Beats62.50%
class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word):
        now_n = self.root
        for c in word :
            if c not in now_n :
                now_n[c] = {}
            now_n = now_n[c]

    def count_end(self):
        cou = 0
        def dfs(now_n, now_i) :
            if len(now_n) == 0 :
                nonlocal cou
                cou += now_i
            for next_n in now_n.values() :
                dfs(next_n, now_i+1)
        dfs(self.root, 1)
        return cou

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        trie = Trie()
        for s in words :
            trie.insert(s[::-1])
        return trie.count_end()
        
# given ans : 14ms Beats95.24%
from itertools import pairwise
class Solution: 
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = sorted(map(lambda x: x[::-1], words))
        ans = len(words[-1])+1
        for s1, s2 in pairwise(words):
            if not s2.startswith(s1):
                ans += len(s1)+1
        return ans

s = Solution()
print("ans :",s.minimumLengthEncoding(["time", "me", "bell"])) # 10
print("ans :",s.minimumLengthEncoding(["me", "time", "bell"])) # 10
print("ans :",s.minimumLengthEncoding(["t"])) # 2
# print("ans :",s.minimumLengthEncoding()) # 



