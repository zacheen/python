# my Beats 85.4%
class Trie:
    def __init__(self):
        self.mem = []

    def insert(self, word):
        left, right = 0, len(self.mem) 
        while left < right:
            mid = (left + right) // 2 
            if self.mem[mid] == word:
                self.mem.insert(mid, word)
                return
            elif self.mem[mid] < word:
                left = mid + 1
            else:
                right = mid

        self.mem.insert(left, word)

    def search(self, word):
        left, right = 0, len(self.mem) 
        while left < right:
            mid = (left + right) // 2 
            if self.mem[mid] == word:
                return True
            elif self.mem[mid] < word:
                left = mid + 1
            else:
                right = mid

        return False

    def startsWith(self, prefix):        
        left, right = 0, len(self.mem) 
        while left < right:
            mid = (left + right) // 2 
            if self.mem[mid][:min(len(prefix), len(self.mem[mid]))] == prefix:
                return True
            elif self.mem[mid] < prefix:
                left = mid + 1
            else:
                right = mid

        return left != len(self.mem) and (self.mem[left][:min(len(prefix), len(self.mem[left]))] == prefix)

# given ans Beats 61.5%
import collections
class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.isWord = True

    def search(self, word):
        node = self._find(word)
        return node and node.isWord

    def startsWith(self, prefix):
        return self._find(prefix)

    def _find(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node.children:
                return None
            node = node.children[c]
        return node

s = Solution()
# print(s.())



