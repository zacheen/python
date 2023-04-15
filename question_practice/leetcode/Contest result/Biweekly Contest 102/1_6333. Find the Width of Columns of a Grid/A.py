from typing import List
import functools

# my 
class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        ans = []
        for i in range(len(grid[0])) :
            this_row_ans = 0
            for j in range(len(grid)) :
                this_row_ans = max(this_row_ans, len(str(grid[j][i])))
            ans.append(this_row_ans)
        return ans

# given ans

s = Solution()
print(s.findColumnWidth([[1],[22],[333]]))
print(s.findColumnWidth([[-15,1,3],[15,7,12],[5,6,-2]]))



