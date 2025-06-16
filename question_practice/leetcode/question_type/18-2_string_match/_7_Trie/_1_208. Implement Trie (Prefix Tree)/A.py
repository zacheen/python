# 208. Implement Trie (Prefix Tree)
# https://leetcode.com/problems/implement-trie-prefix-tree/description/

# my using template v1 : 23ms Beats97.19%
class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        now_n = self.root
        for c in word :
            if c not in now_n :
                now_n[c] = {}
            now_n = now_n[c]
        now_n[None] = None

    def search(self, word: str) -> bool:
        ret = self.find_end(word)
        return None != ret and None in ret

    def startsWith(self, prefix: str) -> bool:
        return self.find_end(prefix) != None

    # None : return at the middle
    # else : return the end node
    def find_end(self, prefix) :
        now_n = self.root
        for c in prefix :
            if c not in now_n :
                return None
            now_n = now_n[c]
        return now_n

# my template v2 : easier to read : 40ms Beats76.84%
class Trie_node:
    def __init__(self):
        self.next = {}
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

    def search(self, word: str) -> bool:
        ret = self.find_end(word)
        return ret!=None and ret.end

    def startsWith(self, prefix: str) -> bool:
        return self.find_end(prefix) != None

    # None : return at the middle
    # else : return the end node
    def find_end(self, prefix) :
        now_n = self.root
        for c in prefix :
            if c not in now_n.next :
                return None
            now_n = now_n.next[c]
        return now_n

# # my (binary search) Beats 85.4%
# class Trie:
#     def __init__(self):
#         self.mem = []

#     def insert(self, word):
#         left, right = 0, len(self.mem) 
#         while left < right:
#             mid = (left + right) // 2 
#             if self.mem[mid] == word:
#                 self.mem.insert(mid, word)
#                 return
#             elif self.mem[mid] < word:
#                 left = mid + 1
#             else:
#                 right = mid

#         self.mem.insert(left, word)

#     def search(self, word):
#         left, right = 0, len(self.mem) 
#         while left < right:
#             mid = (left + right) // 2 
#             if self.mem[mid] == word:
#                 return True
#             elif self.mem[mid] < word:
#                 left = mid + 1
#             else:
#                 right = mid

#         return False

#     def startsWith(self, prefix):        
#         left, right = 0, len(self.mem) 
#         while left < right:
#             mid = (left + right) // 2 
#             if self.mem[mid][:min(len(prefix), len(self.mem[mid]))] == prefix:
#                 return True
#             elif self.mem[mid] < prefix:
#                 left = mid + 1
#             else:
#                 right = mid

#         return left != len(self.mem) and (self.mem[left][:min(len(prefix), len(self.mem[left]))] == prefix)


