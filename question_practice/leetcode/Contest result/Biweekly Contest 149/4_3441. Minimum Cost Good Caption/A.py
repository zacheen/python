# 3441. Minimum Cost Good Caption
# https://leetcode.com/problems/minimum-cost-good-caption/description/

from typing import List
from math import inf

# combining my and given ans : 1122ms Beats80.80%
class Solution:
    def minCostGoodCaption(self, caption: str) -> str:
        if len(caption) < 3 :
            return ""
        ord_a = ord("a")
        caption = [ord(c)-ord_a for c in caption]

        def compute(i, j):
            l = sorted(caption[i:j])
            target = l[(j - i - 1) // 2]
            return sum(abs(c - target) for c in l), target
        mem = deque([["",0],["",inf],["",inf],["",inf],["",inf],["",inf]])
        end_limit = len(caption)+1
        for st in range(0, len(caption)-2):
            st_m6 = st%6
            pre_ans, pre_s = mem[st_m6]
            for en in range(st+3, min(st+6, end_limit)):
                range_l = caption[st:en]
                min_s, min_tar = compute(st, en)
                new_s = pre_s + min_s
                new_ans = pre_ans + chr(min_tar + ord_a)*(en-st)
                en_m6 = en%6
                cmp_ans, cmp_s = mem[en_m6]
                if new_s < cmp_s or (new_s == cmp_s and new_ans < cmp_ans):
                    mem[en_m6] = [new_ans, new_s]
            mem[st_m6][1] = inf
        return mem[len(caption)%6][0]

# my (for dp version) 7794ms Beats25.50%
from collections import deque
class Solution:
    def minCostGoodCaption(self, caption: str) -> str:
        if len(caption) < 3 :
            return ""
        ord_a = ord("a")
        caption = [ord(c)-ord_a for c in caption]

        mem = deque([["",0],["",inf],["",inf],["",inf],["",inf],["",inf]])
        end_limit = len(caption)+1
        for st in range(0, len(caption)-2):
            pre_ans, pre_s = mem[st%6]
            for en in range(st+3, min(st+6, end_limit)):
                range_l = caption[st:en]
                min_s = inf
                min_tar = None
                for target in range(0,26) :
                    s = sum(abs(n-target) for n in range_l)
                    if s < min_s :
                        min_s = s
                        min_tar = target
                new_s = pre_s + min_s
                new_ans = pre_ans + chr(min_tar + ord_a)*(en-st)
                if new_s < mem[en%6][1] or (new_s == mem[en%6][1] and new_ans < mem[en%6][0]):
                    mem[en%6] = [new_ans, new_s]
            mem[st%6][1] = inf
        return mem[len(caption)%6][0]

# # my (recursion dp version) : Memory Limit Exceeded
# from functools import cache
# class Solution:
#     def minCostGoodCaption(self, caption: str) -> str:
#         if len(caption) < 3 :
#             return ""
#         ord_a = ord("a")
#         caption = [ord(c)-ord_a for c in caption]

#         limit_len = len(caption) - 3
#         @cache
#         def dp(st) :
#             if st == len(caption) :
#                 return "", 0
#             if st > limit_len :
#                 return "", inf

#             out_min_s = inf
#             out_ans = ""
#             for end in range(st+3, st+6):
#                 range_l = caption[st:end]
#                 min_s = inf
#                 min_tar = None
#                 for target in range(0,26) :
#                     s = sum(abs(n-target) for n in range_l)
#                     if s < min_s :
#                         min_s = s
#                         min_tar = target
#                 new_ans, new_s = dp(end)
#                 new_s += min_s
#                 new_ans = chr(min_tar + ord_a)*(end-st) + new_ans
#                 if new_s < out_min_s or (new_s == out_min_s and new_ans < out_ans):
#                     out_min_s = new_s
#                     out_ans = new_ans
#             return out_ans, out_min_s
#         return dp(0)[0]

# given ans : direct calculate diff_sum
class Solution:
    def minCostGoodCaption(self, caption: str) -> str:
        if len(caption) < 3:
            return ""

        n = len(caption)
        dp = [(inf, "!")] * (n + 1)
        dp[0] = None
        def compute(i, j):
            l = sorted(list(caption[i:j]))
            mc = l[(j - i - 1) // 2]
            target = ord(mc)
            op = 0
            for c in l:
                op += abs(ord(c) - target)
            return op, mc * (j - i)

        for i in range(3, min(6, n + 1)):
            dp[i] = compute(0, i)
            
        for i in range(6, n + 1):
            dp[i] = (inf, "!")
            for j in range(3, 6):
                op, s = compute(i - j, i)
                dp_op, dp_s = dp[i-j]
                compare = op + dp_op
                
                if dp[i][0] > compare:
                    dp[i] = (compare, dp_s + s)
                elif dp[i][0] == compare:
                    dp[i] = (dp[i][0], min(dp[i][1], dp_s + s))
            dp[i-5] = None
            
        return dp[-1][1]


s = Solution()
# print("ans :",s.minCostGoodCaption("cdcd")) # "cccc"
# print("ans :",s.minCostGoodCaption("aca")) # "aaa"
# print("ans :",s.minCostGoodCaption("bc")) # ""
print("ans :",s.minCostGoodCaption("antwfdps")) # "nnnnnppp"
# print(sum(abs(ord(c1) - ord(c2)) for c1,c2 in zip("antwfdps", "nnnnnppp")))
# print(sum(abs(ord(c1) - ord(c2)) for c1,c2 in zip("antwfdps", "nnnppppp")))
print("ans :",s.minCostGoodCaption("oweaxihc")) # ""ooohhhhh""
# print(sum(abs(ord(c1) - ord(c2)) for c1,c2 in zip("oweaxihc", "ooohhhhh")))
# print(sum(abs(ord(c1) - ord(c2)) for c1,c2 in zip("oweaxihc", "ooooohhh")))



