# 3409. Longest Subsequence With Decreasing Adjacent Difference
# https://leetcode.com/problems/longest-subsequence-with-decreasing-adjacent-difference/description/

from typing import List
import functools

# my 8943ms Beats65.10% # Ref No.1
max_n = 300
class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        # mem[last_num][min_diff] = longest subsequence length
        mem = [[0]*(max_n+1) for _ in range(max_n+1)]
        for n in nums :
            max_len = mem[n][max_n]
            for diff in range(max_n-1,-1,-1):
                # max_len = max(max_len, mem[n][diff]) # already include below
                # new two comb
                # 1
                last_n = n+diff
                if last_n > 0 and last_n <= max_n :
                    max_len = max(max_len, mem[last_n][diff] + 1)
                # 2
                last_n = n-diff
                if last_n > 0 and last_n <= max_n :
                    max_len = max(max_len, mem[last_n][diff] + 1)
                # update
                mem[n][diff] = max_len
        return max(mem[n][0] for n in range(1, max_n+1))

# given ans (combine two for loop)
# 5827ms Beats91.43%
max_n = 300
class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        # mem[last_num][min_diff] = longest subsequence length
        mem = [[0]*(max_n+1) for _ in range(max_n+1)]
        for n in nums :
            max_len = mem[n][max_n]
            for diff in range(max_n-1,-1,-1):
                # max_len = max(max_len, mem[n][diff]) # already include below
                # new two comb
                # 1
                last_n = n+diff
                if last_n >= 0 and last_n <= max_n :
                    max_len = max(max_len, mem[last_n][diff] + 1)
                # 2
                last_n = n-diff
                if last_n >= 0 and last_n <= max_n :
                    max_len = max(max_len, mem[last_n][diff] + 1)
                # update
                mem[n][diff] = max_len
        return max(mem[n][0] for n in range(1, max_n+1))

s = Solution()
# print("ans :",s.longestSubsequence([16,6,3])) # [16, 6, 3] : 3
# print("ans :",s.longestSubsequence([6,5,3,4,2,1])) # [6, 4, 2, 1] : 4
# print("ans :",s.longestSubsequence([10,20,10,19,10,20])) # [10, 20, 10, 19, 10] : 5
print("ans :",s.longestSubsequence([17,162,72,225,300,73,41,26,53,282,232,240,274,25,127,63,116,131,147,42,9,127,279,105,254,236,60,65,269,10,291,264,106,158,250,82,93,96,190,87,141,146,240,272,6,29,288,162,116,83,139,187,100,295,164,80,156,116,24,110,49,140,69,219,3,251,113,128,153,2,197,200,23,83,142])) # 20

# print("ans :",s.longestSubsequence([3,5]))
