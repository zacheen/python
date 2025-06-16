# 1408. String Matching in an Array
# https://leetcode.com/problems/string-matching-in-an-array/description

from typing import List
import functools

# my using template Aho_Corasick
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
        self.ans = set()

    def query(self, find_arr: str):
        cur_node = self.trie_root
        for i, this_val in enumerate(find_arr):
            while (unmatch := this_val not in cur_node.dict) and cur_node != self.trie_root:
                cur_node = cur_node.fail
            if not unmatch:
                cur_node = cur_node.dict[this_val]
                for fit_p in cur_node.target:
                    if len(fit_p) < len(find_arr) :
                        self.ans.add(fit_p)

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ac = Aho_Corasick(words)
        for w in words :
            ac.query(w)
        return list(ac.ans)

# my 0ms Beats100.00%
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=lambda x : len(x), reverse = True)
        # print(words)

        stack = []
        ans = []
        for w in words :
            not_ans = True
            for s in stack :
                if w in s :
                    ans.append(w)
                    not_ans = False
                    break
            if not_ans :
                stack.append(w)
        # print(stack)
        return ans
    


s = Solution()
print("ans :",s.stringMatching()) # 



