# 677. Map Sum Pairs
# https://leetcode.com/problems/map-sum-pairs/description/

from typing import List
from math import inf

# my 0ms
class Trie_node:
    def __init__(self):
        self.next = {}
        self.t_val = 0

class MapSum:
    def __init__(self):
        self.root = Trie_node()
        self.seen = {}

    def insert(self, key: str, val: int) -> None:
        prev_val = self.seen.get(key, 0)
        self.seen[key] = val
        
        now_n = self.root
        for c in key :
            if c not in now_n.next :
                now_n.next[c] = Trie_node()
            now_n.t_val += (val - prev_val)
            now_n = now_n.next[c]
        now_n.t_val += (val - prev_val)

    def sum(self, prefix: str) -> int:
        now_n = self.root
        for c in prefix :
            if c not in now_n.next :
                return 0
            now_n = now_n.next[c]
        return now_n.t_val


