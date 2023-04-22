from typing import List
import functools

# my 
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        small_len = min(len(word1), len(word2))
        ans = ""
        for w1,w2 in zip(word1[:small_len], word2[:small_len]):
            ans = ans + w1 + w2
        ans = ans + word1[small_len:] + word2[small_len:]
        return ans

from itertools import zip_longest
# given ans
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return ''.join(a + b for a, b in zip_longest(word1, word2, fillvalue=''))
  
s = Solution()
print(s.mergeAlternately(word1 = "abc", word2 = "pqr"))
print(s.mergeAlternately(word1 = "ab", word2 = "pqrs"))
print(s.mergeAlternately(word1 = "abcd", word2 = "pq"))



