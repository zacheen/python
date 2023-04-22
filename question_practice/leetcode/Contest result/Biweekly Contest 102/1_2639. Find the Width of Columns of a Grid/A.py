from typing import List
import functools

# my Beats 88.36%
class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        ans = []
        for i in range(len(grid[0])) :
            this_row_ans = 0
            for j in range(len(grid)) :
                this_row_ans = max(this_row_ans, len(str(grid[j][i])))
            ans.append(this_row_ans)
        return ans
    
# my 合併 Beats 99.55%
class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        return [ max(len(str(grid[j][i])) for j in range(len(grid))) for i in range(len(grid[0]))]

# given ans
# 一模一樣

s = Solution()
print(s.findColumnWidth([[1],[22],[333]]))
print(s.findColumnWidth([[-15,1,3],[15,7,12],[5,6,-2]]))



