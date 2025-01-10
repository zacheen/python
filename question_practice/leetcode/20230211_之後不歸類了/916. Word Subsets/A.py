# 916. Word Subsets
# https://leetcode.com/problems/word-subsets/description

from typing import List
import functools

# my 1111ms Beats5.18%
from collections import Counter
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        list_a_z = [chr(i) for i in range(ord('a'), ord('z')+1)]
        max_w = Counter()
        for w2 in words2 :
            cou_w2  = Counter(w2)
            for c in list_a_z :
                max_w[c] = max(max_w[c], cou_w2[c])
        
        ans = []
        for w1 in words1 :
            ans.append(w1)
            cou_w1 = Counter(w1)
            for c in list_a_z :
                if max_w[c] > cou_w1[c] :
                    ans.pop()
                    break
        return ans

# given ans 638ms Beats10.76%
# same concept, better implement method
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        max_w = Counter()
        for w2 in words2 :
            max_w = max_w | Counter(w2)
        return [w1 for w1 in words1 if Counter(w1) >= max_w]

s = Solution()
print("ans :",s.wordSubsets(words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"])) # ["facebook","google","leetcode"] 
print("ans :",s.wordSubsets(words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["l","e"])) # ["apple","google","leetcode"]



