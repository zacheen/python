from typing import List
from functools import lru_cache

# # my Time Limit Exceeded
# class Solution:
#     def minInsertions(self, s: str) -> int:
#         # 其實加入字母 跟 刪除字母的個數是一樣的
#         # 所以我就計算刪除字母的個數就好了

#         @lru_cache()
#         def dp(l,r):
#             if l >= r :
#                 return 0
#             elif s[l] == s[r] :
#                 return dp(l+1, r-1)
#             else :
#                 return min(dp(l+1, r), dp(l, r-1))+1

#         return dp(0, len(s)-1)

# # my v2 Beats 61.46%
# # v1 的 @functools.lru_cache() 改成 @cache
# # 一樣都是 cache 不知道為什麼差這麼多
# class Solution:
#     def minInsertions(self, s: str) -> int:
#         # 其實加入字母 跟 刪除字母的個數是一樣的
#         # 所以我就計算刪除字母的個數就好了

#         @cache
#         def dp(l,r):
#             if l >= r :
#                 return 0
#             elif s[l] == s[r] :
#                 return dp(l+1, r-1)
#             else :
#                 return min(dp(l+1, r), dp(l, r-1))+1

#         return dp(0, len(s)-1)
    
# my v3 Beats 61.46%
# # v1 的 @lru_cache() 改成 @lru_cache(None) 就過了??
class Solution:
    def minInsertions(self, s: str) -> int:
        # 其實加入字母 跟 刪除字母的個數是一樣的
        # 所以我就計算刪除字母的個數就好了

        @lru_cache(None)
        def dp(l,r):
            if l >= r :
                return 0
            elif s[l] == s[r] :
                return dp(l+1, r-1)
            else :
                return min(dp(l+1, r), dp(l, r-1))+1

        return dp(0, len(s)-1)

# my v4 Beats 73.84%
class Solution:
    def minInsertions(self, s: str) -> int:
        # 其實加入字母 跟 刪除字母的個數是一樣的
        # 所以我就計算刪除字母的個數就好了

        dp_mem = [[-1]*len(s) for _ in range(len(s))]
        def dp(l,r):
            if l >= r :
                return 0
            elif dp_mem[l][r] != -1 :
                return dp_mem[l][r]
            elif s[l] == s[r] :
                ret = dp(l+1, r-1)
            else :
                ret = min(dp(l+1, r), dp(l, r-1))+1

            dp_mem[l][r] = ret
            return ret

        return dp(0, len(s)-1)

# given ans
# 516. Longest Palindromic Subsequence : 是計算最長的 Palindromic Subsequence
# 所以只要 return len(s) - self.longestPalindromeSubseq(s) 就好了

s = Solution()
print(s.minInsertions("zzazz"))
print(s.minInsertions("mbadm"))
print(s.minInsertions("leetcode"))



