# Aho_Corasick == Trie + Z-algorithm(LCP) (+ state machine)

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
    
# # 另外一種 Aho-Corasick template，速度差不多 (但好像短一點?)
    # 這是這題的解答
    # 3292. Minimum Number of Valid Strings to Form Target II
    # https://leetcode.com/problems/minimum-number-of-valid-strings-to-form-target-ii/description/
# from collections import defaultdict, deque
# class Trie:
#     def __init__(self):
#         self.c=defaultdict(Trie)
#         self.i=0
#         self.prev=None
#     def add(self, w):
#         cur=self
#         for i,ch in enumerate(w):
#             cur=cur.c[ch]
#             cur.i=i+1
#     def next(self, ch):
#         if ch in self.c: return self.c[ch]
#         if not self.prev: return self
#         return self.prev.next(ch)
#     def aho_corasick(self):
#         dq=deque((self, y) for y in self.c.values())
#         while dq:
#             x,y = dq.popleft()
#             y.prev=x
#             for ch in y.c: dq.append((x.next(ch), y.c[ch]))
# class Solution:
#     def minValidStrings(self, words, target) -> int:
#         trie=Trie()
#         for w in words: trie.add(w)
#         trie.aho_corasick()

#         # query
#         n=len(target)
#         pre=[0]*n
#         for i,ch in enumerate(target):
#             trie=trie.next(ch)
#             pre[i]=trie.i
#         res = 0
#         i = n-1
#         while i>=0:
#             if pre[i]==0: return -1
#             res,i=res+1, i-pre[i]
#         return res

if __name__ == "__main__":
    print("--- Test Case 1 ---")
    ac1 = Aho_Corasick(["abc", "ab", "bc", "a", "b", "c", "x"])
    text1 = "abccab"
    matches1 = ac1.query(text1)
    matches1.sort()
    print("ret:\n", matches1)

    print("--- Test Case 2 ---")
    ac3 = Aho_Corasick(["hers", "his", "she", "he"])
    text3 = "ushers" # "ushers" -> "she", "he", "hers"
    matches3 = ac3.query(text3)
    matches3.sort()
    print("ret:", matches3)