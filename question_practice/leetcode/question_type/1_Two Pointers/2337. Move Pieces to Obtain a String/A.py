# https://leetcode.com/problems/move-pieces-to-obtain-a-string/description

from typing import List
import functools

# my v1 71ms Beats96.77%
class Solution:
    def canChange(self, start: str, target: str) -> bool:
        add_L = 0
        add_R = 0
        for c_s, c_t in zip(start, target) :
            if c_t == "L" :
                add_L += 1
                if add_R > 0 :
                    return False
            if c_s == "R" :
                add_R += 1
                if add_L > 0 :
                    return False
            elif c_s == "L" :
                add_L -= 1
                if add_L < 0 :
                    return False
            if c_t == "R" :
                add_R -= 1
                if add_R < 0 :
                    return False
        return add_L == 0 and add_R == 0

# two pointer
# my v2 155ms Beats49.19% 
class Solution:
    def canChange(self, start: str, target: str) -> bool:
        indx_s = 0
        indx_t = 0
        while True :
            while indx_s < len(start) and start[indx_s] == "_" :
                indx_s += 1
            while indx_t < len(target) and target[indx_t] == "_" :
                indx_t += 1
            if not(indx_s < len(start) and indx_t < len(target)) :
                break
            if start[indx_s] != target[indx_t] :
                return False
            if start[indx_s] == "R" and indx_s > indx_t :
                return False
            if start[indx_s] == "L" and indx_s < indx_t :
                return False
            indx_s += 1
            indx_t += 1

        return indx_s == len(start) and indx_t == len(target)

# given ans

s = Solution()
print("ans :",s.canChange(start = "_L__R__R_", target = "L______RR"))
print("ans :",s.canChange(start = "R_L_", target = "__LR"))
print("ans :",s.canChange(start = "_R", target = "R_"))
print("ans :",s.canChange(start = "_L__R__R_L", target = "L______RR_"))



