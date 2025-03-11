# 2707. Extra Characters in a String
# https://leetcode.com/problems/extra-characters-in-a-string/description/

from typing import List
from math import inf

# my (forward) 47ms Beats97.72%
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # dp[i] : 在 s[i] 之前最小的 del 數量
        dp = [0]+[inf]*len(s)
        for s_i, st_c in range(len(s)) :
            del_cou = dp[s_i]
            dp[s_i+1] = min(dp[s_i+1], del_cou+1)
            for di in dictionary :
                if st_c != di[0] :
                    continue
                end_i = s_i+len(di)
                if end_i<=len(s) and di == s[s_i:end_i] :
                    dp[end_i] = min(dp[end_i], del_cou)
        return dp[-1]

# my optimized by given ans (backward) 42ms Beats98.70%
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # dp[i] : 在 s[i] 之前最小的 del 數量
        dp = [inf]*len(s)+[0]
        for s_i in range(len(s)-1,-1,-1) :
            dp[s_i] = dp[s_i+1]+1
            st_c = s[s_i]
            for di in dictionary :
                if st_c != di[0] :
                    continue
                end_i = s_i+len(di)
                if end_i<=len(s) and di == s[s_i:end_i] :
                    dp[s_i] = min(dp[s_i], dp[end_i])
        return dp[0]

s = Solution()
print("ans :",s.minExtraChar(s = "leetscode", dictionary = ["leet","code","leetcode"])) # 1
print("ans :",s.minExtraChar(s = "sayhelloworld", dictionary = ["hello","world"])) # 3
print("ans :",s.minExtraChar("dwmodizxvvbosxxw", ["diz","v","o","wmo","cehy"])) # 7
                            # wmo,diz,v,v,o


