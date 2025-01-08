# 1422. Maximum Score After Splitting a String
# https://leetcode.com/problems/maximum-score-after-splitting-a-string/description

from typing import List
import functools

# my 
class Solution:
    def maxScore(self, s: str) -> int:
        l = 0
        r = s.count("1")
        max_ans = 0
        for c in s[:-1] :
            if c == "0" :
                l += 1
            else :
                r -= 1
            max_ans = max(max_ans, l+r)
        return max_ans

# given ans
# same

s = Solution()
print("ans :",s.maxScore("000")) # 2



