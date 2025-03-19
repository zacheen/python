# 686. Repeated String Match
# https://leetcode.com/problems/repeated-string-match/

from typing import List
from math import inf, ceil

# # my : 4ms Beats33.84%
# from bisect import bisect_left
# class Solution:
#     def repeatedStringMatch(self, a: str, b: str) -> int:
#         if b == "" : return 0
#         def check(mid: int) -> bool:
#             return b in a*mid
#         max_rep = len(b)//len(a)+3
#         ret = bisect_left(range(max_rep), True, key=check)
#         return ret if ret != max_rep else -1

# given ans : improve the range from above : 0ms
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        n = ceil(len(b) / len(a))
        s = a * n
        if b in s:
            return n
        if b in s + a:
            return n + 1
        return -1
    
# given ans : 單次 kmp (有修改)
    # https://leetcode.cn/problems/repeated-string-match/solutions/1170235/zhong-fu-die-jia-zi-fu-chuan-pi-pei-by-l-vnye/
class Solution:
    def strstr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        if m == 0:
            return 0

        pi = [0] * m
        j = 0
        for i in range(1, m):
            while j > 0 and needle[i] != needle[j]:
                j = pi[j - 1]
            if needle[i] == needle[j]:
                j += 1
            pi[i] = j

        i, j = 0, 0
        while i - j < n:
            while j > 0 and haystack[i % n] != needle[j]:
                j = pi[j - 1]
            if haystack[i % n] == needle[j]:
                j += 1
            if j == m:
                return i - m + 1
            i += 1
        return -1

    def repeatedStringMatch(self, a: str, b: str) -> int:
        n, m = len(a), len(b)
        index = self.strstr(a, b)
        if index == -1:
            return -1
        if n - index >= m:
            return 1
        return (m + index - n - 1) // n + 2

s = Solution()
print("ans :",s.repeatedStringMatch(a = "abcd", b = "cdabcdab")) # 3
print("ans :",s.repeatedStringMatch(a = "a", b = "aa")) # 2
print("ans :",s.repeatedStringMatch(a = "abaa", b = "xabaax")) # 2
print("ans :",s.repeatedStringMatch(a = "abaa", b = "aabaa")) # 2
print("ans :",s.repeatedStringMatch(a = "abab", b = "bababa")) # 2



