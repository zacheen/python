# 1415. The k-th Lexicographical String of All Happy Strings of Length n
# https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n

from typing import List
from math import inf

# my 44ms Beats40.92%
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        poss_c = ['a', 'b', 'c']
        ord_c = 0
        ans = ""
        def dfs(now_s):
            nonlocal ans, ord_c
            if len(now_s) > n :
                ord_c += 1
                if ord_c == k :
                    ans = "".join(now_s)
                return 
            for next_c in poss_c :
                if next_c == now_s[-1] :
                    continue
                now_s.append(next_c)
                dfs(now_s)
                now_s.pop()
        dfs([""])
        return ans

# my 56ms Beats26.26%
# adding fast forward
from functools import cache
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        @cache
        def cal_comb(len_n):
            return 2**(n-len_n)
        
        poss_c = ['a', 'b', 'c']
        ord_c = 0
        ans = ""
        def dfs(now_s):
            nonlocal ans, ord_c, k
            if len(now_s) > n :
                ord_c += 1
                if ord_c == k :
                    ans = "".join(now_s)
                return 
            for next_c in poss_c :
                if next_c == now_s[-1] :
                    continue
                # fast forward
                comb = cal_comb(len(now_s))
                if comb < k :
                    k -= comb
                    continue
                else :
                    now_s.append(next_c)
                    dfs(now_s)
                    now_s.pop()
        dfs([""])
        return ans

# # given ans
# class Solution:
#     def getHappyString(self, n: int, k: int) -> str:
#         total_happy = 3 * (2**(n-1))

#         res = []
#         choices = "abc"
#         left, right = 1, total_happy

#         for i in range(n):
#             cur = left
#             partition_size = (right - left + 1) // len(choices)
#             # Polling: 1 - 4, 5 - 8, 9 - 12

#             for c in choices:
#                 # cur <= k < cur + partition_size
#                 if k in range(cur, cur + partition_size):
#                     res.append(c)
#                     left = cur
#                     right = cur + partition_size - 1
#                     choices = "abc".replace(c, "")
#                     break
#                 cur += partition_size

#         return "".join(res)

s = Solution()
print("ans :",s.getHappyString(n = 1, k = 3)) # "c"
print("ans :",s.getHappyString(n = 1, k = 4)) # ""
print("ans :",s.getHappyString(n = 3, k = 9)) # "cab"



