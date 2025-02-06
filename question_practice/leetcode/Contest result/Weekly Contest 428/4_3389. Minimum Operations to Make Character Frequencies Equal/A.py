# 3389. Minimum Operations to Make Character Frequencies Equal
# https://leetcode.com/problems/minimum-operations-to-make-character-frequencies-equal/description/
    # Change a character in s to its next letter in the alphabet. 
        # "b" 能變成 "c", 但 "c" 不能變成 "b"
from typing import List

from math import inf
# given ans and optimized by me : 1085ms Beats51.87%
class Solution:
    def makeStringGood(self, s: str) -> int:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1

        def dp(i, deleted):
            if (i,deleted) in mem :
                return mem[(i,deleted)]
            if i == 26:
                return 0

            x = count[i]
            if x <= target:
                # 直接刪除這個字母 (刪除的字母還可以給下一個字母用)
                ans = dp(i + 1, x) + x
                # 從前一個字母變成而來
                increase = target - x # 數量要變成 target 差多少
                change = min(deleted, increase) # 最多可以從前一個字 Change 過來
                cand = dp(i + 1, 0) + increase - change
                ans = min(ans, cand)
            else:
                # 如果數量超過一定是要刪除
                decrease = x - target
                ans = dp(i + 1, decrease) + decrease
            mem[(i,deleted)] = ans
            return ans

        ans = inf
        for target in range(max(count) + 1) :
            mem = {}
            ret = dp(0, 0)
            if ret < ans :
                ans = ret
        return ans

s = Solution()
# print("ans :",s.makeStringGood("acab")) # 1 (remove one a)
# print("ans :",s.makeStringGood("wddw")) # 0
# print("ans :",s.makeStringGood("aaabc")) # (change a to c, and add b)
# print("ans :",s.makeStringGood("abbbcc")) # (X) "aabbcc"
print("ans :",s.makeStringGood("gigigjjggjjgg")) # g:7,i:2,j:4 > g:7,j:7 # 3



