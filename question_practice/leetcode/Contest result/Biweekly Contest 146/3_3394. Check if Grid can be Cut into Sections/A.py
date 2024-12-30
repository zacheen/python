# 3394. Check if Grid can be Cut into Sections
# https://leetcode.com/problems/check-if-grid-can-be-cut-into-sections/description/

from typing import List
import functools

# my 298ms Beats100.00%
class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        # hor
        all_range = [(startx, endx) for startx, starty, endx, endy in rectangles]
        all_range.sort()
        # print(all_range)
        # merge_overlap
        last = sum(all_range[0])/2
        count = 0
        for start, end in all_range :
            if start >= last :
                count += 1
                if count >= 2 :
                    # print("hor success", count)
                    return True
            last = max(last, end)       

        # ver
        all_range = [(starty, endy) for startx, starty, endx, endy in rectangles]
        all_range.sort()

        # merge_overlap
        last = sum(all_range[0])/2
        count = 0
        for start, end in all_range :
            if start >= last :
                count += 1
                if count >= 2 :
                    # print("ver success", count)
                    return True
            last = max(last, end) 
        return False

# given ans
# mine is better, but they use function to shorten the code like below

# my opt 271ms Beats100.00%
# adding given ans opt
class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        def check(all_range) :
            all_range.sort()
            # print(all_range)
            # merge_overlap
            last = sum(all_range[0])/2
            count = 0
            for start, end in all_range :
                if start >= last :
                    count += 1
                    if count >= 2 :
                        # print("hor success", count)
                        return True
                last = max(last, end)  
            return False     
        
        return check([(startx, endx) for startx, starty, endx, endy in rectangles]) \
            or check([(starty, endy) for startx, starty, endx, endy in rectangles])

s = Solution()
print("ans :",s.checkValidCuts(n = 5, rectangles = [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]])) # T
print("ans :",s.checkValidCuts(n = 4, rectangles = [[0,0,1,1],[2,0,3,4],[0,2,2,3],[3,0,4,3]])) # T
print("ans :",s.checkValidCuts(n = 4, rectangles = [[0,2,2,4],[1,0,3,2],[2,2,3,4],[3,0,4,2],[3,2,4,4]])) # F 



