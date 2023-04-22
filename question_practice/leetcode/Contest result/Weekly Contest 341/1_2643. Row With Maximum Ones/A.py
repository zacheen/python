from typing import List
import functools

# my Beats 43.82%
# given ans 
    # 改成用 sum Beats 74.63%

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        max_row = 0
        max_count = 0
        for indx, each_row in enumerate(mat) :
            # now_count = each_row.count(1)
            # 因為只有 1 跟 0 所以可以改成用 sum
            now_count = sum(each_row)
            if now_count > max_count :
                max_count = now_count
                max_row = indx
        return [max_row, max_count]

# given ans
# 一模一樣

s = Solution()
print(s.rowAndMaximumOnes([[0,1],[1,0]]))
print(s.rowAndMaximumOnes([[0,0,0],[0,1,1]]))
print(s.rowAndMaximumOnes([[0,0],[1,1],[0,0]]))



