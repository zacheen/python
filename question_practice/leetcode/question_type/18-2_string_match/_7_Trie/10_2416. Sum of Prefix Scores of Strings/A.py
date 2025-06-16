# 2416. Sum of Prefix Scores of Strings
# https://leetcode.com/problems/sum-of-prefix-scores-of-strings/description/

from typing import List
from math import inf

# my 1844ms Beats77.04%
class Trie_node:
    def __init__(self):
        self.next = {}
        self.pre_cou = 0

class Trie:
    def __init__(self):
        self.root = Trie_node()

    def insert(self, word: str) -> None:
        now_n = self.root
        for c in word :
            if c not in now_n.next :
                now_n.next[c] = Trie_node()
            now_n = now_n.next[c]
            now_n.pre_cou += 1

    # None : return at the middle
    # else : return the end node
    def find_end(self, prefix) :
        ret = 0
        now_n = self.root
        for i, c in enumerate(prefix) :
            now_n = now_n.next[c]
            ret += now_n.pre_cou
        return ret

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        for s in words :
            trie.insert(s)
        return [trie.find_end(s) for s in words]

# given ans


s = Solution()
print("ans :",s.sumPrefixScores(["abc","ab","bc","b"])) # [5, 4, 3, 2]
print("ans :",s.sumPrefixScores(["abcd"])) # [4]
