# 676. Implement Magic Dictionary
# https://leetcode.com/problems/implement-magic-dictionary/description/

from typing import List
from math import inf

# my 72ms Beats73.94%
class MagicDictionary:
    def __init__(self):
        self.root = {}

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary :
            now_n = self.root
            for c in word :
                if c not in now_n :
                    now_n[c] = {}
                now_n = now_n[c]
            now_n[None] = None

    def search(self, searchWord: str) -> bool:
        def dfs(now_n, now_i, rem):
            if now_i == len(searchWord) :
                # print("reach end", now_n, now_i, rem)
                return (rem == 0 and None in now_n)
            
            now_c = searchWord[now_i]
            # not same 
            if rem == 1 :
                for c, next_n in now_n.items() :
                    if next_n != None :
                        if c == now_c : continue
                        if dfs(next_n, now_i+1, 0) :
                            return True
            
            # same
            if now_c in now_n :
                # print("same", now_n[now_c], now_i+1, rem)
                return dfs(now_n[now_c], now_i+1, rem)
            return False
        return dfs(self.root, 0, 1)

# given ans : bucket sort by length : 9ms Beats97.37%
from collections import defaultdict
class MagicDictionary:
    def __init__(self):
        self.words = defaultdict(list)

    def buildDict(self, dictionary: List[str]) -> None:
        for x in dictionary:
            self.words[len(x)].append(x)

    def search(self, searchWord: str) -> bool:
        lengt = len(searchWord)
        if lengt not in self.words.keys():
            return False
        for word in self.words[lengt]:
            cou = 0
            for c1,c2 in zip(word, searchWord):
                if c1 != c2 :
                    cou += 1
                    if cou == 2 :
                        break
            if cou == 1 :
                return True
        return False


