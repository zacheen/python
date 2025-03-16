# 3453. Separate Squares I
# https://leetcode.com/problems/separate-squares-i/description/

from typing import List
from math import inf

# my 475ms Beats94.60% O(n)
from sortedcontainers import SortedList
class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        # 其實 x 的位置沒有差
        # 重點是高度(y),以及寬度(l)
        squares.sort(key = lambda x : x[1])
        squares.append([0,10**9+1,0])
        total_area = sum(l*l for _,_,l in squares)
        half_area = total_area/2

        stack = SortedList()
        width_cou = 0
        last_pos = squares[0][1]
        for x,y,l in squares :
            # 先排除超過範圍的
            while stack and stack[0][0] <= y :
                end_y, pre_l = stack.pop(0)
                if half_area > (pop_area := (end_y-last_pos)*width_cou) :
                    half_area -= pop_area
                    width_cou -= pre_l
                    last_pos = end_y
                else :
                    break

            # 計算範圍內的
            if half_area > (pop_area := (y-last_pos)*width_cou) :
                half_area -= pop_area
                width_cou += l
                last_pos = y
            else :
                break
            
            # 加入此 squ 進 stack
            stack.add((y+l, l))
        return last_pos + (half_area/width_cou)

# my version 2 (binary search) : 3649ms Beats21.86% O(n*60)
class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        total_area = sum(l*l for _,_,l in squares)
        half_area = total_area/2
        def check(y_line):
            area_sum = 0
            for x,y,l in squares :
                if y_line > y :
                    area_sum += l*(min(l, y_line-y))
            return area_sum < half_area
    
        left = 0
        right = (10**9)*2
        for _ in range(60):
            mid = (left + right) / 2
            if check(mid) :
                left = mid
            else:
                right = mid 
        return left

# given ans : 2270ms Beats63.35%
# 把計算結果全部 * 10000
    # 這樣就會變成整數
        # 優點1 : 可以提早結束，而不是固定做 60 次
        # 優點2 : 可以丟入 bisect_left 而不用自己手動做 binarySearch
import bisect
class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        M = 100_000
        total_area = sum(l*l for _,_,l in squares)*M
        half_area = total_area//2

        def check(multi_y: int) -> bool:
            area = 0
            for _, y, l in squares:
                if y*M < multi_y:
                    area += l*min(multi_y-y*M, l*M)
            return area >= half_area

        max_y = max(y + l for _, y, l in squares)
        return bisect.bisect_left(range(max_y * M), True, key=check) / M


s = Solution()
# print("ans :",s.separateSquares([[0,0,1],[2,2,1]])) # 1.0
# print("ans :",s.separateSquares([[0,0,2],[1,1,1]])) # 1.1666666666666667
# print("ans :",s.separateSquares([[9,28,3],[7,19,1],[13,18,2]])) # 28.666666666666668
print("ans :",s.separateSquares([[999892931,999974790,6788622],[319710671,963660807,5518783],[623736653,934759633,4248549],[234214719,848813522,417010],[154771654,645515409,9370045],[965571354,998982755,10809560],[338822522,550588284,12471651],[168193362,682286828,5173004],[459856474,778674604,5635628],[806653114,860720237,1444683]])) # 21.83333



