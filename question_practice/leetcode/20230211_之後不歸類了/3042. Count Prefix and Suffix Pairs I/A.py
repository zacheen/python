# 3042. Count Prefix and Suffix Pairs I
# https://leetcode.com/problems/count-prefix-and-suffix-pairs-i/description

from typing import List
import functools

# my 7ms Beats89.37%
class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        ans_cou = 0
        for i, s1 in enumerate(words) :
            for s2 in words[i+1:]:
                if s2.find(s1) == 0 and s2.rfind(s1) == (len(s2)-len(s1)) :
                    ans_cou += 1
        return ans_cou
    
# my opt 7ms Beats89.37%
from itertools import combinations
class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        ans_cou = 0
        for s1,s2 in combinations(words, 2) :
            if s2[:len(s1)] == s1 == s2[-len(s1):] :
                ans_cou += 1
        return ans_cou


# given ans

s = Solution()
print("ans :",s.countPrefixSuffixPairs()) # 



