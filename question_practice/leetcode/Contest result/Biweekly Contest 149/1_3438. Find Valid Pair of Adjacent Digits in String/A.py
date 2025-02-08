# 3438. Find Valid Pair of Adjacent Digits in String
# https://leetcode.com/problems/find-valid-pair-of-adjacent-digits-in-string/description/

from typing import List
from math import inf

from collections import Counter
from itertools import pairwise
# my 
class Solution:
    def findValidPair(self, s: str) -> str:
        cou = Counter(s)
        val = set()
        for i in range(1,10):
            if i == cou[str(i)] :
                val.add(str(i))

        for c1,c2 in pairwise(s) :
            if c1 != c2 and c1 in val and c2 in val :
                return c1+c2
        return ""

