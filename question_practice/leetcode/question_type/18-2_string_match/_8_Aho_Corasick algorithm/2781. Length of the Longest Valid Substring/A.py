# 2781. Length of the Longest Valid Substring
# https://leetcode.com/problems/length-of-the-longest-valid-substring

from typing import List
from math import inf

# my modify template Aho_Corasick : 3201ms Beats7.06%
from collections import defaultdict, deque
class TrieNode:
    def __init__(self):
        self.dict = defaultdict(TrieNode)
        self.target = None
        self.fail = None # fastforward path when failed

class Aho_Corasick:
    def __init__(self, arrs):
        self.trie_root = TrieNode()
        
        # build trie
        for pattern in arrs:
            cur_node = self.trie_root
            for p in pattern:                
                cur_node = cur_node.dict[p]
            cur_node.target = pattern
            
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
                # next_node.target |= next_node.fail.target  # inherit all match target
                # 其實我只需要保留最短的就好了
                if next_node.fail.target != None:
                    next_node.target = next_node.fail.target
                # add to queue for next level
                q.append(next_node)

    def query(self, find_arr: str):
        max_len = 0
        max_l = -1
        cur_node = self.trie_root
        for i, this_val in enumerate(find_arr):
            while (unmatch := this_val not in cur_node.dict) and cur_node != self.trie_root:
                cur_node = cur_node.fail
            if not unmatch:
                cur_node = cur_node.dict[this_val]
                if cur_node.target:
                    fit_p = cur_node.target
                    # i 一定會愈來愈大，所以只需要考慮 i 變大的情況
                    max_len = max(max_len, (i-1)-max_l)
                    max_l = max(max_l, i-len(fit_p)+1)
        return max(max_len, (len(find_arr)-1)-max_l)
class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        ac = Aho_Corasick(forbidden)
        return ac.query(word)

# my inspire from given ans : 831ms Beats92.93%
    # 由於 1 <= forbidden[i].length <= 10，所以遍歷所有word的子串是可行的
class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        forb_set = set(forbidden)
        max_sub_len = max(len(f) for f in forb_set)
        
        max_len = 0
        max_l = 0 # sub string 包含 word[l]
        for r in range(1,len(word)+1): # sub string 不包含 word[r]
            for l in range(r-1, max(r-max_sub_len, max_l)-1, -1):
                if word[l:r] in forb_set :
                    max_l = l+1 # 因為有符合的 所以word[l]不取 且l+1一定大於max_l
                    break
            # _valid_sub_str = word[max_l:r]
            max_len = max(max_len, r-max_l)
        return max_len

s = Solution()
print("ans :",s.longestValidSubstring(word = "cbaaaabc", forbidden = ["aaa","cb"])) # 4 aabc
print("ans :",s.longestValidSubstring(word = "leetcode", forbidden = ["de","le","e"])) # 4 tcod



