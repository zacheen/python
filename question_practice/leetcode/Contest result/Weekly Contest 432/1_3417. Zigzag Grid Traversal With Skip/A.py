# 3417. Zigzag Grid Traversal With Skip
# https://leetcode.com/problems/zigzag-grid-traversal-with-skip/description/

from typing import List
import functools

# my 4ms Beats100.00%
class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        ans = []
        for i1, this_row in enumerate(grid):
            if i1 % 2 :
                # i1 odd
                if (len(this_row) + i1) % 2 :
                    start_i = len(this_row)-1
                else :
                    start_i = len(this_row)-2
                ans += [this_row[i2] for i2 in range(start_i, -1, -2)]
            else :
                # i2 even
                ans += [n for i2, n in enumerate(this_row) if i2%2 == 0]
        return ans
                        
# given ans No.1
# directly link all the items and pick [::2]
class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        ans = []
        f = True
        for v in grid:
            if f: ans.extend(v)
            else: ans.extend(v[::-1])
            f = not f
        return ans[::2]

s = Solution()
print("ans :",s.zigzagTraversal( grid = [[1,2],[3,4]] )) # [1,4]
print("ans :",s.zigzagTraversal( grid = [[2,1],[2,1],[2,1]] )) #  [2,1,2]



