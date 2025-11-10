# 3025. Find the Number of Ways to Place People I
# https://leetcode.com/problems/find-the-number-of-ways-to-place-people-i

# same as
# 3027. Find the Number of Ways to Place People II
# https://leetcode.com/problems/find-the-number-of-ways-to-place-people-ii
    # but input limitation is bigger

from typing import List
from math import inf

# my 11ms Beats95.92%
class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x : (x[0], -x[1]))
        ans = 0
        for i, (fir_x, fir_y) in enumerate(points) :
            # 後面的點只要比 max_y 小，就一定會包到 max_y 這個點
            max_y = -inf
            for sec_x, sec_y in points[i+1:] :
                if max_y < sec_y <= fir_y :
                    ans += 1
                    max_y = sec_y
        return ans 

s = Solution()
print("ans :",s.numberOfPairs([[1,1],[2,2],[3,3]])) # 0
print("ans :",s.numberOfPairs([[6,2],[4,4],[2,6]])) # 2
print("ans :",s.numberOfPairs([[3,1],[1,3],[1,1]])) # 2
print("ans :",s.numberOfPairs([[0,2],[1,3],[6,1]])) # 2

