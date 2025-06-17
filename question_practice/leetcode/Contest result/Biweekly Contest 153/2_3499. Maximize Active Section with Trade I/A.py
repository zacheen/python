# 3499. Maximize Active Section with Trade I
# https://leetcode.com/problems/maximize-active-section-with-trade-i/description/

from typing import List
from math import inf
from itertools import pairwise
from itertools import groupby

# my 699ms Beats87.32%
class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        sh_cou = []
        cou = 1
        pre_c = "1"
        for c in s :
            if pre_c == c :
                cou += 1
            else :
                sh_cou.append(cou)
                pre_c = c
                cou = 1
        if pre_c == "1" :
            sh_cou.append(cou+1)
        else :
            sh_cou.append(cou)
            sh_cou.append(1)

        # print(sh_cou)
        if len(sh_cou) <= 3 :
            # print("less than three",[cou for i, cou in enumerate(sh_cou) if i%2 == 0])
            return sum(cou for i, cou in enumerate(sh_cou) if i%2 == 0) - 2

        only_zero = [cou for i, cou in enumerate(sh_cou) if i%2 == 1]
        # print("only_zero",list(only_zero))

        max_zero = max(cou1+cou2 for cou1,cou2 in pairwise(only_zero))
        return sum(cou for i, cou in enumerate(sh_cou) if i%2 == 0) - 2 + max_zero

s = Solution()
print("ans :",s.maxActiveSectionsAfterTrade("01")) # 1
print("ans :",s.maxActiveSectionsAfterTrade("0100")) # 4
print("ans :",s.maxActiveSectionsAfterTrade("1000100")) # 7
print("ans :",s.maxActiveSectionsAfterTrade("01010")) # 4



