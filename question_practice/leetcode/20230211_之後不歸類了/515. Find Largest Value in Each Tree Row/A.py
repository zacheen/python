# 515. Find Largest Value in Each Tree Row
# https://leetcode.com/problems/find-largest-value-in-each-tree-row/description

from typing import List
import functools

# my 0ms Beats100.00%
class Solution:
    def largestValues(self, root) -> List[int]:
        if root == None :
            return []
        ans = []
        stack = [root]
        while stack :
            next_level = []
            this_level_val = []
            for p in stack :
                this_level_val.append(p.val)
                if p.left :
                    next_level.append(p.left)
                if p.right :
                    next_level.append(p.right)
            ans.append(max(this_level_val))
            stack = next_level
        return ans

# given ans
# directly comp when getting p.val : mx = max(mx, p.val)

s = Solution()
print("ans :",s.largestValues()) # 



