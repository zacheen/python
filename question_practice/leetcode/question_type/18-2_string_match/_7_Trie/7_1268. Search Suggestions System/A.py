# 1268. Search Suggestions System
# https://leetcode.com/problems/search-suggestions-system/description/

from typing import List
from math import inf

# my 250ms Beats22.19%
class Trie_node:
    def __init__(self):
        self.next = {}
        self.sort_keys = None
        self.end = False

class Trie:
    def __init__(self):
        self.root = Trie_node()

    def insert(self, word: str) -> None:
        now_n = self.root
        for c in word :
            if c not in now_n.next :
                now_n.next[c] = Trie_node()
            now_n = now_n.next[c]
        now_n.end = True

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        for p in products :
            trie.insert(p)

        ans = [[] for _ in range(len(searchWord))]
        def find_sm_3(node, pre_s, i):
            if len(ans[i]) == 3 :
                return
            if node.end :
                ans[i].append(pre_s)
            
            if node.sort_keys == None :
                node.sort_keys = sorted(node.next.keys())
            for c in node.sort_keys :
                find_sm_3(node.next[c], pre_s+c, i)
        
        now_n = trie.root
        for i, c in enumerate(searchWord) :
            if c not in now_n.next :
                break
            now_n = now_n.next[c]
            find_sm_3(now_n, searchWord[:i+1], i)
        return ans

# inspire by given ans : 71ms Beats55.34%
    # sort the product, so the smaller one can insert first
    # only save the smallest three suggestion
class Trie_node:
    def __init__(self):
        self.next = {}
        self.sug = []

class Trie:
    def __init__(self):
        self.root = Trie_node()

    def insert(self, word: str) -> None:
        now_n = self.root
        for c in word :
            if c not in now_n.next :
                now_n.next[c] = Trie_node()
            now_n = now_n.next[c]
            if len(now_n.sug) < 3 :
                now_n.sug.append(word)
        now_n.end = True

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        products.sort()
        for p in products :
            trie.insert(p)

        ans = [[] for _ in range(len(searchWord))]
        now_n = trie.root
        for i, c in enumerate(searchWord) :
            if c not in now_n.next :
                break
            now_n = now_n.next[c]
            ans[i] = now_n.sug
        return ans

# given ans : 4ms Beats91.31%
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        res = []
        start, end = 0, len(products)-1
        for i, c in enumerate(searchWord):
            while start <= end and (i>=len(products[start]) or products[start][i]<c):
                start += 1
            while start <= end and (i>=len(products[end]) or products[end][i]>c):
                end -= 1
            if start <= end:
                res.append(products[start : min(start+3, end+1)])
            else:
                res.append([])
        return res

s = Solution()
print("ans :",s.suggestedProducts(products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse")) # 
print("ans :",s.suggestedProducts(products = ["havana"], searchWord = "havana")) # 
# print("ans :",s.suggestedProducts()) # 



