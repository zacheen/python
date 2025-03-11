# 3208. Alternating Groups II
# https://leetcode.com/problems/alternating-groups-ii

from typing import List
from math import inf
from collections import deque
from itertools import cycle

# my optimized 686ms Beats96.01%
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        k -= 1
        ans = 0
        prev = colors[0]
        cou = 0
        for col in colors + colors[:k] :
            if col != prev :
                cou += 1
                if cou >= k :
                    ans += 1
            else :
                cou = 0
            prev = col
        return ans

# my
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        k -= 1
        ans = 0
        prev = colors[0]
        stack = deque()
        cou = 0
        for _, col in zip(range(len(colors)+k),cycle(colors)) :
            if len(stack) >= k :
                if stack.popleft() :
                    cou -= 1
            diff_f = (col != prev)
            prev = col
            stack.append(diff_f)
            if diff_f :
                cou += 1
                if cou == k :
                    ans += 1
        return ans

s = Solution()
print("ans :",s.numberOfAlternatingGroups(colors = [0,1,0,1,0], k = 3)) # 3
print("ans :",s.numberOfAlternatingGroups(colors = [0,1,0,0,1,0,1], k = 6)) # 2
print("ans :",s.numberOfAlternatingGroups(colors = [1,1,0,1], k = 4)) # 0



