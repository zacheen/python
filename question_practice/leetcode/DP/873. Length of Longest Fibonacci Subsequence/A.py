# 873. Length of Longest Fibonacci Subsequence
# https://leetcode.com/problems/length-of-longest-fibonacci-subsequence

from typing import List
from math import inf

from collections import defaultdict
# my v2 5138ms Beats5.30%
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        max_ans = 0
        dp = defaultdict(dict)
        for i,n in enumerate(arr) :
            for last_n, cou in dp[n].items() :
                cou += 1
                if cou > max_ans :
                    max_ans = cou
                dp[last_n+n][n] = max(cou, dp[last_n+n].get(n, 0))
            for pre in arr[:i] :
                dp[n+pre][n] = max(2, dp[n+pre].get(n, 0))
        return max_ans

# my v1 9025ms Beats5.30%
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        max_ans = 0
        dp = defaultdict(list)
        for i,n in enumerate(arr) :
            for last_n, cou in dp[n] :
                cou += 1
                if cou > max_ans :
                    max_ans = cou
                dp[last_n+n].append([n,cou])
            for pre in arr[:i] :
                dp[n+pre].append([n,2])
            # print(n,dp)
        return max_ans
                
# opt by given ans : 453ms Beats96.03%
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        max_ans = 0
        dp = {}
        for i,s in enumerate(arr) :
            dp[s] = {}
            for pre in arr[:i] :
                if (pre2:=s-pre) <= pre :
                    break
                if pre2 not in dp :
                    continue
                new_c = dp[pre2].get(pre, 2) + 1
                dp[s][pre2] = new_c
                if new_c > max_ans :
                    max_ans = new_c
        return max_ans

s = Solution()
print("ans :",s.lenLongestFibSubseq([1,2,3,4,5,6,7,8])) # 5 : [1,2,3,5,8]
# print("ans :",s.lenLongestFibSubseq([1,3,7,11,12,14,18])) # 3



