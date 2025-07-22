# 1233. Remove Sub-Folders from the Filesystem
# https://leetcode.com/problems/remove-sub-folders-from-the-filesystem

from typing import List
from math import inf
from collections import defaultdict

# my 
class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word):
        now_n = self.root
        for c in word :
            if c not in now_n :
                now_n[c] = {}
            now_n = now_n[c]
            if None in now_n :
                return False
        now_n[None] = None
        return True 
    
# v1 : 39ms Beats69.82%
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()
        folder.sort(key = lambda x : x.count("/"))
        ans = []
        for f in folder :
            if trie.insert(f.split("/")) :
                ans.append(f)
        return ans

# v2 : 39ms Beats69.82%
    # when folder.length getting bigger, this is faster
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()
        # bucket sort
        bucket = defaultdict(list)
        for f in folder :
            bucket[f.count("/")].append(f)

        ans = []
        for l in range(50) :
            for f in bucket[l] :
                if trie.insert(f.split("/")) :
                    ans.append(f)
        return ans

# given ans
    # sort 後，若有子目錄，則子目錄一定會在父目錄後面
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        res = []
        for path in folder:
            if not res or not path.startswith(res[-1] + '/'):
                res.append(path)
        return res

s = Solution()
print("ans :",s.removeSubfolders(folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"])) # ['/a', '/c/d', '/c/f']
print("ans :",s.removeSubfolders(folder = ["/a","/a/b/c","/a/b/d"])) # ['/a']
print("ans :",s.removeSubfolders(folder = ["/a/b/c","/a/b/ca","/a/b/d"])) # ['/a/b/c', '/a/b/ca', '/a/b/d']



