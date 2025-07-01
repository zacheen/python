# 139. Word Break
# https://leetcode.com/problems/word-break/description/

# my using template C_Knap_reach v2 : 0ms
class Solution:
    def wordBreak(self, s, wordDict):
        dp = [True]+[False]*len(s)
        for i in range(len(dp)-1) :
            if dp[i] :
                for word in wordDict :
                    if s[i:i+len(word)] == word :
                        dp[i+len(word)] = True
        # print(dp)
        return dp[-1]

from functools import lru_cache
# my practice again : 4ms Beats41.52%
class Solution:
    def wordBreak(self, s, wordDict):
        wordDict = set(wordDict)
        @lru_cache
        def dp(st_i):
            for i in range(st_i+1, len(s)):
                if s[st_i : i] in wordDict :
                    if dp(i) :
                        return True
            if s[st_i:] in wordDict :
                return True
            return False
        return dp(0)

# given ans
# 完美的縮寫 (O)
class Solution:
    def wordBreak(self, s, wordDict):
        wordSet = set(wordDict)

        @lru_cache(None)  # 因為尾端比較常被呼叫到
        def wordBreak(s):
            if s in wordSet:
                return True
            return any(s[:i] in wordSet and wordBreak(s[i:]) for i in range(len(s)))

        return wordBreak(s)

s = Solution()
print(s.wordBreak(
    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
, wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa"]))
# print(s.wordBreak(
#     s = "leetcod"
# , wordDict = ["leet","cod"]))