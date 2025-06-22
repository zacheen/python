# 3085. Minimum Deletions to Make String K-Special
# https://leetcode.com/problems/minimum-deletions-to-make-string-k-special

from typing import List
from math import inf
from collections import Counter
from itertools import accumulate

# my 58ms Beats66.67%
class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        cou = list(Counter(word).values())
        cou.sort()
        len_cou = len(cou)
        cou_acc = [0]+list(accumulate(cou))

        r = 0
        min_ans = inf
        for l, (l_n, front_del) in enumerate(zip(cou, cou_acc)) :
            while r < len_cou and cou[r]-l_n <= k : # cou[r] 是超出的開始位置
                r += 1
            min_ans = min(min_ans, (cou_acc[-1]-cou_acc[r])-((len_cou-r)*(l_n+k)) + front_del)
        return min_ans

s = Solution()
print("ans :",s.minimumDeletions(word = "aabcaba", k = 0)) # 3
print("ans :",s.minimumDeletions(word = "dabdcbdcdcd", k = 2)) # 2
print("ans :",s.minimumDeletions(word = "aaabaaa", k = 2)) # 1



