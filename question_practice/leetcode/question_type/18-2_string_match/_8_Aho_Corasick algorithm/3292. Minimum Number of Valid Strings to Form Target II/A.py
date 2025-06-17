# 3292. Minimum Number of Valid Strings to Form Target II
# https://leetcode.com/problems/minimum-number-of-valid-strings-to-form-target-ii/description/
from typing import List
from math import inf
from collections import defaultdict, deque

# my modity template Aho_Corasick : 550ms Beats80.00%
class TrieNode:
    def __init__(self):
        self.dict = defaultdict(TrieNode)
        self.target = 0
        self.fail = None # fastforward path when failed

class Aho_Corasick:
    def __init__(self, arrs):
        self.trie_root = TrieNode()
        
        # build trie
        for pattern in arrs:
            cur_node = self.trie_root
            for pat_l, p in zip(range(1, len(pattern)+1),pattern):    
                cur_node = cur_node.dict[p]
                # 原本是結束的時候加完整 pattern > 現在改成紀錄目前符合最長長度
                cur_node.target = pat_l
            
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
                # 因此也不用合併 target 了
                # next_node.target |= next_node.fail.target  # inherit all match target
                # add to queue for next level
                q.append(next_node)

    def query(self, find_arr: str):
        dp = [0]+[inf]*len(find_arr)
        cur_node = self.trie_root
        for i, this_val in zip(range(1,len(find_arr)+1), find_arr):
            while (unmatch := this_val not in cur_node.dict) and cur_node != self.trie_root:
                cur_node = cur_node.fail
            if not unmatch:
                cur_node = cur_node.dict[this_val]
                dp[i] = dp[i-cur_node.target]+1 # 因為 dp 是遞增的，所以直接找最前面的就好
        return dp[-1]

class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        ac = Aho_Corasick(words)
        ret = ac.query(target) 
        return ret if ret != inf else -1

s = Solution()
print("ans :",s.minValidStrings(words = ["abc","aaaaa","bcdef"], target = "aabcdabc")) # 3
print("ans :",s.minValidStrings(words = ["abababab","ab"], target = "ababaababa")) # 2
print("ans :",s.minValidStrings(words = ["abcdef"], target = "xyz")) # -1
print("ans :",s.minValidStrings(words = ["a","babc"], target = "aacab")) # -1
print("ans :",s.minValidStrings(words = ["babc"], target = "a")) # -1
print("ans :",s.minValidStrings(words = ["cab","bacbbbbcababca","a"], target = "ccbacbbaaa")) # 6
print("ans :",s.minValidStrings(words = ["caacbbbbbcaccb","baccccb","aacabcca"], target = "aacaacbabb")) # 5 : aac, aac, ba, b, b
