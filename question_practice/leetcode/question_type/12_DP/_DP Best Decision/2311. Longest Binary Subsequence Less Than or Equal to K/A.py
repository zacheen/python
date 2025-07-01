# 2311. Longest Binary Subsequence Less Than or Equal to K
# https://leetcode.com/problems/longest-binary-subsequence-less-than-or-equal-to-k

from typing import List
from math import inf
from bisect import bisect_right


# my v1 : 3535ms Beats5.69%
class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        max_len = len(s)
        dp = ["1"*i for i in range(max_len+1)]
        for now_l, c in enumerate(s,1):
            for i in range(min(now_l,max_len),0,-1) :
                dp[i] = min(dp[i], dp[i-1]+c)
        # print(dp)
        for s in dp[::-1] :
            if int(s, 2) <= k :
                return len(s)
        return 0

# my v2 : 3276ms Beats5.69%
    # opt : changing to int
class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        max_len = len(s)
        dp = [(1<<i)-1 for i in range(max_len+1)]
        for now_l, c in enumerate(s,1):
            now_n = int(c)
            for i in range(min(now_l,max_len),0,-1) :
                dp[i] = min(dp[i], (dp[i-1]<<1)+now_n)
        # print(dp)
        return min(bisect_right(dp, k)-1, max_len)
    
# given ans : 0ms
class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        N = len(s)
        ans = 0
        curr = 0
        for i,x in enumerate(s[::-1]):
            if x=='1':
                curr = curr | (1<<i)
                if curr > k:
                    break
                ans+=1
        return ans + s.count('0')

s = Solution()
print("ans :",s.longestSubsequence(s = "1001010", k = 5)) # 5
print("ans :",s.longestSubsequence(s = "00101001", k = 1)) # 6
print("ans :",s.longestSubsequence(s = "1010100", k = 0)) # 4
print("ans :",s.longestSubsequence(s = "10101001", k = 0)) # 4
print("ans :",s.longestSubsequence(s = "0", k = 100)) # 1



