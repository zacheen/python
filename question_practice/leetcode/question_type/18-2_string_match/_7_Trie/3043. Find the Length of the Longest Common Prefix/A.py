# 3043. Find the Length of the Longest Common Prefix
# https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/description/

from typing import List
from math import inf

# my 275ms Beats68.77%
class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word):
        now_n = self.root
        for c in word :
            if c not in now_n :
                now_n[c] = {}
            now_n = now_n[c]
        now_n[None] = None

    # None : return at the middle
    # else : return the end node
    def find_end(self, prefix) :
        now_n = self.root
        for i, c in enumerate(prefix) :
            if c not in now_n :
                return i
            now_n = now_n[c]
        return len(prefix)

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        trie = Trie()
        for n in arr1 :
            trie.insert(str(n))
        return max( trie.find_end(str(n)) for n in arr2 )

# my v2 123ms Beats99.35%
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        # all comb of arr1
        comb_arr1 = set()
        for num in arr1 :
                # num not in comb_arr1 可以讓迴圈提早跳出，因此更快
            while num not in comb_arr1 and num > 0 : 
                comb_arr1.add(num)
                num //= 10

        # all comb of arr2
        ans = -1
        for num in arr2 :
            while num > 0 :
                if num in comb_arr1 :
                    ans = max(ans, num)
                    break
                num //= 10
        if ans == -1 : return 0
        else : return len(str(ans))

s = Solution()
print("ans :",s.longestCommonPrefix(arr1 = [1,10,100], arr2 = [1000])) # 3
print("ans :",s.longestCommonPrefix(arr1 = [1,2,3], arr2 = [4,4,4])) # 0



