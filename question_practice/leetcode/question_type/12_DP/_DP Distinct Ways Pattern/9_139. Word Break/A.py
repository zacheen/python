# 139. Word Break
# https://leetcode.com/problems/word-break/description/

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

# My_v2  Runtime: 35 ms, faster than 95.90% of Python3
class Solution:
    def wordBreak(self, s, wordDict):
        cache = [False]* (len(s)+1)
        cache[0] = True
        def find(remainstr, index):
            if remainstr == "" :
                return True

            if cache[index] :
                return False
            
            for eachWord in wordDict :
                fit = True
                for i in range(len(eachWord)) :
                    if i>=len(remainstr) or eachWord[i] != remainstr[i] :
                        fit = False
                        break
                if fit :
                    cache[index] = True
                    if find(remainstr[len(eachWord):], index+len(eachWord)) :
                        return True

            return False

        return find(s, 1)

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