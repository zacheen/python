# 165. Compare Version Numbers
# https://leetcode.com/problems/compare-version-numbers/description/

from typing import List
from math import inf

# my 0ms
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        def trans_form(s):
            ret = [int(num_s) for num_s in s.split(".")]
            while ret and ret[-1] == 0 :
                ret.pop()
            return ret
        
        v1 = trans_form(version1)
        v2 = trans_form(version2)

        if v1 == v2 :
            return 0
        elif v2 > v1 :
            return -1
        else :
            return 1

s = Solution()
print("ans :",s.compareVersion(version1 = "1.2", version2 = "1.10")) # -1
print("ans :",s.compareVersion(version1 = "1.01", version2 = "1.001")) # 0
print("ans :",s.compareVersion(version1 = "1.0", version2 = "1.0.0.0")) # 0



