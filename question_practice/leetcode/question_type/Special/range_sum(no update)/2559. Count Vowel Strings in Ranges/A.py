# 2559. Count Vowel Strings in Ranges
# https://leetcode.com/problems/count-vowel-strings-in-ranges/description

from typing import List
import functools

# my 11ms Beats99.35%
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowel = set(['a', 'e', 'i', 'o', 'u'])
        mem = [0]
        prev = 0
        for w in words :
            if w[0] in vowel and w[-1] in vowel :
                prev += 1
            mem.append(prev)
        # print(mem)
        return [mem[q2+1] - mem[q1] for q1,q2 in queries]

# my SegTree version : 182ms Beats6.02%
class SegTree:
    def __init__(self, nums):
        self.n = len(nums)
        # init
        self.tree = [0] * 2 * self.n
        for i,n in zip(range(self.n, 2 * self.n) , nums):
            self.tree[i] = n
        for i in range(self.n-1, 0, -1):
            # execute def
            self.tree[i] = self.tree[2*i] + self.tree[2*i+1]

    def query(self, left, right):
        # include
        left += self.n
        right += self.n
        res = 0
        while left <= right:
            if left & 1 :
                # combine result
                res += self.tree[left]
                left += 1
            if not (right & 1) :
                # combine result
                res += self.tree[right]
                right -= 1
            left >>= 1
            right>>= 1
        return res

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowel = set(['a', 'e', 'i', 'o', 'u'])
        segT = SegTree(list(1 if (w[0] in vowel and w[-1] in vowel) else 0 for w in words))
        return [segT.query(q1,q2) for q1,q2 in queries]

s = Solution()
# print("ans :",s.vowelStrings(words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]])) # [2,3,0]
# print("ans :",s.vowelStrings(words = ["a","e","i"], queries = [[0,2],[0,1],[2,2]])) # [3,2,1]
# print("ans :",s.vowelStrings(words = ["b","e","b","e","b"], queries = [[0,2],[1,3],[0,1],[2,2],[3,3]])) # [1, 2, 1, 0, 1]



