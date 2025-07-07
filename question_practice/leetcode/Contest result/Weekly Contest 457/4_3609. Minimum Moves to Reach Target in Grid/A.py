# 3609. Minimum Moves to Reach Target in Grid
# https://leetcode.com/problems/minimum-moves-to-reach-target-in-grid/description/

from typing import List
from math import inf

# my inspire by given ans : 0ms
    # 要從結果推回來
class Solution:
    def minMoves(self, sx: int, sy: int, tx: int, ty: int) -> int:
        ans = 0
        while tx >= sx and ty >= sy:
            if tx == sx and ty == sy :
                return ans
            
            if tx == ty : # 如果相等 要看sx跟sy哪個是0
                if sx == 0 :
                    tx = 0
                else :
                    ty = 0
                ans += 1
                continue
            
            switch = False
            if tx < ty :
                tx, ty = ty, tx
                switch = True
            # tx must > ty
            if tx-ty >= ty : # 一定是大的加到大的那邊
                if tx & 1 :
                    return -1
                tx = tx//2
            else :
                tx -= ty
            
            if switch :
                tx, ty = ty, tx
            ans += 1
        return -1

s = Solution()
print("ans :",s.minMoves(sx = 1, sy = 2, tx = 5, ty = 4)) # 2
print("ans :",s.minMoves(sx = 0, sy = 1, tx = 2, ty = 3)) # 3
print("ans :",s.minMoves(sx = 1, sy = 1, tx = 2, ty = 2)) # -1
print("ans :",s.minMoves(sx = 1, sy = 0, tx = 4480, ty = 36448)) # -1



