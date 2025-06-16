# 1967. Number of Strings That Appear as Substrings in Word
# https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/description/

from typing import List
from math import inf

# my (easy way) : 0ms
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        return sum(p in word for p in patterns)
    
# my, using template Aho-Corasick
from collections import defaultdict, deque
class TrieNode:
    def __init__(self):
        self.dict = defaultdict(TrieNode)
        self.target = set()
        self.fail = None # fastforward path when failed

class Aho_Corasick:
    def __init__(self, arrs):
        self.trie_root = TrieNode()
        
        # build trie
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
                fail_node = cur_node.fail
                # recursively find the node that can go further (== val in dict) or fail to root
                while (unmatch := val not in fail_node.dict) and fail_node != self.trie_root:
                    fail_node = fail_node.fail
                if unmatch:
                    next_node.fail = self.trie_root
                else:
                    next_node.fail = fail_node.dict[val]
                next_node.target |= next_node.fail.target  # inherit all match target
                # add to queue for next level
                q.append(next_node)

    def query(self, find_arr: str):
        found = []
        cur_node = self.trie_root
        for i, this_val in enumerate(find_arr):
            while (unmatch := this_val not in cur_node.dict) and cur_node != self.trie_root:
                cur_node = cur_node.fail
            if not unmatch:
                cur_node = cur_node.dict[this_val]
                for fit_p in cur_node.target:
                    found.append((i-len(fit_p)+1, fit_p))
        return found

class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        ac = Aho_Corasick(patterns)
        all_match = set(fit_word for pos, fit_word in ac.query(word))
        return sum(p in all_match for p in patterns)

s = Solution()
print("ans :",s.numOfStrings(patterns = ["a","abc","bc","d"], word = "abc")) # 
print("ans :",s.numOfStrings(patterns = ["a","b","c"], word = "aaaaabbbbb")) # 
print("ans :",s.numOfStrings(patterns = ["a","a","a"], word = "ab")) # 



