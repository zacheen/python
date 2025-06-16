# 3213. Construct String with Minimum Cost
# https://leetcode.com/problems/construct-string-with-minimum-cost/description/

from typing import List
from math import inf
from collections import defaultdict
from random import randint

# my using template Aho_Corasick : 10607ms Beats44.55%
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

    def query(self, find_arr, cost_dict):
        dp = [0] + [inf]*len(find_arr)
        cur_node = self.trie_root
        for i, this_val in enumerate(find_arr):
            while (unmatch := this_val not in cur_node.dict) and cur_node != self.trie_root:
                cur_node = cur_node.fail
            if not unmatch:
                cur_node = cur_node.dict[this_val]
                for fit_p in cur_node.target:
                    pos_i = i-len(fit_p)+1
                    end_pos = pos_i + len(fit_p)
                    dp[end_pos] = min(dp[end_pos], dp[pos_i] + cost_dict[fit_p])
        return dp[-1] if dp[-1] != inf else -1

class Solution:
    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:
        ac = Aho_Corasick(words)

        cost_dict = defaultdict(lambda : inf)
        for w,c in zip(words, costs) :
            cost_dict[w] = min(cost_dict[w], c)
        return ac.query(target, cost_dict)

s = Solution()
print("ans :",s.minimumCost(target = "abcdef", 
    words = ["abdef","abc","d","def","ef"], 
    costs = [100,1,1,10,5])) # 7
print("ans :",s.minimumCost( target = "aaaa", 
    words = ["z","zz","zzz"], costs = [1,10,100])) # -1



