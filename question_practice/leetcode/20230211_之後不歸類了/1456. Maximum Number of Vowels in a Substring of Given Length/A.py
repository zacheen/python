# 1456. Maximum Number of Vowels in a Substring of Given Length
# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/submissions/

from typing import List
import functools

# my Beats 97.87%
from collections import deque
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = set(['a', 'e', 'i', 'o', 'u'])
        stack = deque( True if c in vowel else False for c in s[:k] ) 
        # print(stack)
        count = stack.count(True)
        max_ans = count 
        for i in range(k, len(s)) :
            if stack.popleft() :
                count -= 1

            if s[i] in vowel :
                count += 1
                max_ans = max(max_ans, count)
                stack.append(True)
            else :
                stack.append(False)
        return max_ans

# given ans
# in vowel 兩次的方法 (花較少記憶體)

s = Solution()
print(s.maxVowels())



