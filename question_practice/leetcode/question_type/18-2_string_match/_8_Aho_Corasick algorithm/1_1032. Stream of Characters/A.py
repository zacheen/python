# 1032. Stream of Characters
# https://leetcode.com/problems/stream-of-characters/description/
from typing import List

# my, modify from template Aho_Corasick : 99ms Beats94.66%
    # if len(query) highter this method would be much faster than Trie
from collections import defaultdict, deque
class TrieNode:
    def __init__(self):
        self.dict = defaultdict(TrieNode)
        self.target = set()
        self.fail = None # fastforward path when failed

class Aho_Corasick:
    def __init__(self, arrs):
        # for root node of trie, init as empty Trie
        self.trie_root = TrieNode()
        
        for pattern in arrs:
            cur_node = self.trie_root
            for p in pattern:                
                cur_node = cur_node.dict[p]
            cur_node.target.add(pattern)
            
        # root fail to itself
        self.trie_root.fail = self.trie_root
        # first level : fail to root
        q = deque()
        for char, node in self.trie_root.dict.items():
            node.fail = self.trie_root
            q.append(node)

        # other level
        while q:
            cur_node = q.popleft()
            for val, next_node in cur_node.dict.items():
                # find fail node
                fail_node = cur_node.fail
                while (unmatch := val not in fail_node.dict) and fail_node != self.trie_root:
                    fail_node = fail_node.fail
                if unmatch:
                    next_node.fail = self.trie_root
                else:
                    next_node.fail = fail_node.dict[val]
                next_node.target |= next_node.fail.target  # inherit target from fail node
                # add to queue for next level
                q.append(next_node)
        self.cur_node = self.trie_root

    def query(self, this_val: str):
        while (unmatch := this_val not in self.cur_node.dict) and self.cur_node != self.trie_root:
            self.cur_node = self.cur_node.fail
        if not unmatch:
            self.cur_node = self.cur_node.dict[this_val]
            if self.cur_node.target:
                return True
        return False

class StreamChecker:
    def __init__(self, words: List[str]):
        self.ac = Aho_Corasick(words)

    def query(self, letter: str) -> bool:
        return self.ac.query(letter)

# my, modify from template Trie : 106ms Beats90.60%
class Trie:
    def __init__(self):
        self.root = {}
        self.mem_find = deque()

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
        self.mem_find.appendleft(prefix)
        # print("find", self.mem_find)
        now_n = self.root
        for c in self.mem_find :
            if c not in now_n :
                return False
            now_n = now_n[c]
            if None in now_n :
                return True
        return False

class StreamChecker:
    def __init__(self, words: List[str]):
        self.trie = Trie()
        for w in words :
            self.trie.insert(w[::-1])

    def query(self, letter: str) -> bool:
        ret = self.trie.find_end(letter)
        return ret