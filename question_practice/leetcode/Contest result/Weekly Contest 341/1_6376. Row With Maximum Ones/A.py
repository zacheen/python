from typing import List
import functools

# my 
class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        max_row = 0
        max_count = 0
        for indx, each_row in enumerate(mat) :
            now_count = each_row.count(1)
            if now_count > max_count :
                max_count = now_count
                max_row = indx
        return [max_row, max_count]

# given ans

s = Solution()
print(s.rowAndMaximumOnes([[0,1],[1,0]]))
print(s.rowAndMaximumOnes([[0,0,0],[0,1,1]]))
print(s.rowAndMaximumOnes([[0,0],[1,1],[0,0]]))



