# 648. Replace Words
# https://leetcode.com/problems/replace-words/description/

from typing import List
from math import inf

# my 24ms Beats96.04%
class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        now_n = self.root
        for c in word :
            if None in now_n:
                break
            if c not in now_n :
                now_n[c] = {}
            now_n = now_n[c]
        now_n[None] = None

    # None : return at the middle
    # else : return the end node
    def find_end(self, prefix) :
        now_n = self.root
        for i, c in enumerate(prefix) :
            if None in now_n:
                return prefix[:i]
            if c not in now_n :
                return prefix
            now_n = now_n[c]
        return prefix

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for each_d in dictionary :
            trie.insert(each_d)
        return " ".join(trie.find_end(w) for w in sentence.split(" "))

s = Solution()
print("ans :",s.replaceWords(dictionary = ["cat","bat","rat"], 
    sentence = "the cattle was rattled by the battery")) # 
print("ans :",s.replaceWords(dictionary = ["a","b","c"], 
    sentence = "aadsfasf absbs bbab cadsfafs")) # 



