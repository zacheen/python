# 3606. Coupon Code Validator
# https://leetcode.com/problems/coupon-code-validator

from typing import List
from math import inf

# my 7ms Beats100.00%
def check_code(code):
    for c in code :
        if not (c.isalpha() or c.isnumeric() or c == "_") :
            return False
    return True

class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        ret = []
        all_b = {"electronics":0, "grocery":1, "pharmacy":2, "restaurant":3}
        for c, b, a in zip(code, businessLine, isActive) :
            if not a :
                continue
            if not (b in all_b) :
                continue
            if c == "" :
                continue
            if check_code(c) :
                ret.append( (c, all_b[b]) )
        ret.sort(key = lambda x : (x[1], x[0]))
        return [c for c,b in ret]

s = Solution()
print("ans :",s.validateCoupons(code = ["SAVE20","","PHARMA5","SAVE@20"], 
                                businessLine = ["restaurant","grocery","pharmacy","restaurant"], 
                                isActive = [True,True,True,True])) # 
print("ans :",s.validateCoupons(code = ["GROCERY15","ELECTRONICS_50","DISCOUNT10"], 
                                businessLine = ["grocery","electronics","invalid"], 
                                isActive = [False,True,True])) # 



