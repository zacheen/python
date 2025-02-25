# 1910. Remove All Occurrences of a Substring
# https://leetcode.com/problems/remove-all-occurrences-of-a-substring/description

from typing import List
from math import inf

# my 0ms Beats100.00%
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while s :
            new_s = s.replace(part,"",1)
            if len(new_s) == len(s) :
                break
            else :
                s = new_s
        return s

# given ans (optimized): 0ms Beats100.00%
    # 只比尾端
    # O(n*m)
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        part = [c for c in part]
        part_end = part[-1]
        for c in s :
            stack.append(c)
            if len(stack) >= len(part) and c == part_end:
                if stack[-len(part):] == part :
                    stack = stack[:-len(part)]
        return "".join(stack)

s = Solution()
print("ans :",s.removeOccurrences(s = "daabcbaabcbc", part = "abc")) # "dab"
print("ans :",s.removeOccurrences(s = "axxxxyyyyb", part = "xy")) # ab"



