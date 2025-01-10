# 2981. Find Longest Special Substring That Occurs Thrice I
# https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-i/description

from typing import List
import functools

# my + opt from ans 7ms Beats90.54%
from collections import defaultdict
from itertools import accumulate
class Solution:
    def maximumLength(self, s: str) -> int:
        # 最長重複字串 "..aaaaa.."
        # 重複3次 最長重複字串 "..aaa..aaa..aaa.."
        s_len = len(s)
        mem = defaultdict(lambda: [0]*(s_len+1))
        now_count = 0
        now_c = ""
        for c in s :
            if c != now_c :
                now_c = c
                now_count = 0
            now_count += 1
            mem[now_c][now_count] += 1
        max_ans = -1
        for key, cou_list in mem.items() :
            cou_list.reverse()
            for n, cou in zip(range(s_len,max_ans,-1), accumulate(cou_list)) :
                if cou >= 3 :
                    max_ans = max(max_ans, n)
        return max_ans

# # my 14ms Beats65.41%
# from collections import defaultdict
# from itertools import accumulate
# class Solution:
#     def maximumLength(self, s: str) -> int:
#         # 最長重複字串 "..aaaaa.."
#         # 重複3次 最長重複字串 "..aaa..aaa..aaa.."
#         mem = defaultdict(lambda: [0]*51)
#         now_count = 0
#         now_c = ""
#         for c in s :
#             if c != now_c :
#                 now_c = c
#                 now_count = 0
#             now_count += 1
#             mem[now_c][now_count] += 1
#         max_ans = 0
#         for key, cou_list in mem.items() :
#             cou_list.reverse()
#             for n, cou in zip(range(50,max_ans-2,-1), accumulate(cou_list)) :
#                 if cou >= 1 :
#                     if cou >= 3 :
#                         max_ans = max(max_ans, n)
#                         break
#                     else :
#                         max_ans = max(max_ans, n-2)
#         return max_ans if max_ans!=0 else -1

# # given ans : same concept
# # opt 1 : not 50, use len(s) instead
# # opt 2 : just > 3
# import string
# class Solution:
#     def maximumLength(self, s: str) -> int:
#         n = len(s)
#         runningLen = 0
#         prevLetter = '@'
#         # counts[i][j] := the frequency of ('a' + i) repeating j times
#         counts = [[0] * (n + 1) for _ in range(26)]
#         for c in s:
#             if c == prevLetter:
#                 runningLen += 1
#                 counts[string.ascii_lowercase.index(c)][runningLen] += 1
#             else:
#                 runningLen = 1
#                 counts[string.ascii_lowercase.index(c)][runningLen] += 1
#                 prevLetter = c

#         def getMaxFreq(count: list[int]) -> int:
#             """Returns the maximum frequency that occurs more than three times."""
#             times = 0
#             for freq in range(n, 0, -1):
#                 times += count[freq]
#                 if times >= 3:
#                     return freq
#             return -1

#         return max(getMaxFreq(count) for count in counts)

s = Solution()
# print("ans :",s.maximumLength(s = "aaaa")) # 2
# print("ans :",s.maximumLength(s = "abcdef")) # -1
# print("ans :",s.maximumLength(s = "abcaba")) # 1
# print("ans :",s.maximumLength(s = "acc")) # -1
print("ans :",s.maximumLength(s = "abcccccdddd")) # 3



