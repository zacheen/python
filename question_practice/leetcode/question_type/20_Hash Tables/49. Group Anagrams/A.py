# 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams/description/

from typing import List
from math import inf

# my 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def hash(s) :
            # method 1
            return "".join(sorted(s))

            # method 2 (faster when len(s) is big)
            # cnt = [0]*26
            # for c in s :
            #     cnt[ord(c)-ord('a')] += 1
            # return tuple(cnt)

        bucket = defaultdict(list)
        for s in strs :
            bucket[hash(s)].append(s)
        return list(bucket.values())

s = Solution()
print("ans :",s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print("ans :",s.groupAnagrams([""]))
print("ans :",s.groupAnagrams(["a"]))



