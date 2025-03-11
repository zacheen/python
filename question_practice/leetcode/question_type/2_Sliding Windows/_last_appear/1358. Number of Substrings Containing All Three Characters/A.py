# 1358. Number of Substrings Containing All Three Characters
# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters

from typing import List
from math import inf
from collections import Counter

# given ans : mem last appear position : 78ms Beats80.62%
    # Similar to 3. Longest SubWithout Repeating Characters
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ans = 0
        # lastSeen[c] := the index of the last time c appeared
        lastSeen = {c: -1 for c in 'abc'}
        for i, c in enumerate(s):
            lastSeen[c] = i
            # s[0..i], s[1..i], s[min(lastSeen)..i] are satisfied strings.
            ans += 1 + min(lastSeen.values())
        return ans

# my always include r_c : 140ms Beats26.65%
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        cou = Counter()
        acc_cou = 0
        l = 0
        ans = 0
        for r_c in s :
            cou[r_c] += 1
            if cou[r_c] == 1 :
                acc_cou += 1

            if acc_cou == 3 :
                while True :
                    l_c = s[l]
                    if cou[l_c] == 1 :
                        break
                    cou[l_c] -= 1
                    l+=1
                ans += (l+1)
        return ans

# my always include l_c : 135ms Beats28.98%
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        len_s = len(s)
        cou = Counter()
        acc_cou = 0
        r = -1
        ans = 0
        for l_c in s :
            while acc_cou < 3 :
                r += 1
                if r == len_s :
                    return ans
                r_c = s[r]
                cou[r_c] += 1
                if cou[r_c] == 1 :
                    acc_cou += 1
            
            ans += len_s-r

            cou[l_c] -= 1
            if cou[l_c] == 0 :
                acc_cou -= 1



s = Solution()
print("ans :",s.numberOfSubstrings("abcabc")) # 10
print("ans :",s.numberOfSubstrings("aaacb")) # 3
print("ans :",s.numberOfSubstrings("acb")) # 1
print("ans :",s.numberOfSubstrings("acbbcac")) # 11



