# 1306. Jump Game III
# https://leetcode.com/problems/jump-game-iii

from typing import List
from math import inf

# my 
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        q = [start]
        while q :
            this_n = q.pop()
            val = arr[this_n]
            if val == -1 : # -1 : seen
                continue
            if val == 0 :
                return True
            arr[this_n] = -1
            add = this_n + val
            if add < len(arr) :
                q.append(add)
            sub = this_n - val
            if sub >= 0 :
                q.append(sub)
        return False

s = Solution()
print("ans :",s.canReach(arr = [4,2,3,0,3,1,2], start = 5)) # T



