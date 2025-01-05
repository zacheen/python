# 3412. Find Mirror Score of a String
# https://leetcode.com/problems/find-mirror-score-of-a-string/description/

from typing import List
import functools

from collections import defaultdict

# my 87ms Beats100.00%
# fail : closest unmarked index, I thought have to maximize the result
class Solution:
    def calculateScore(self, s: str) -> int:
        mirr = {}
        for n1,n2 in zip(range(ord('a'), ord('z')+1), range(ord('z'), ord('a')-1, -1)) :
            # print(chr(n1), chr(n2))
            mirr[chr(n1)] = chr(n2)

        cou = defaultdict(list)
        ans = 0
        for r, c in enumerate(s) :
            if len(cou[c]) > 0 :
                l = cou[c].pop()
                # print("add", l, r)
                ans += (r-l)
            else :
                cou[mirr[c]].append(r)
        return ans
                
# given ans

s = Solution()
print("ans :",s.calculateScore(s = "aczzx")) # 5
print("ans :",s.calculateScore(s = "abcdef")) # 0



