# 1792. Maximum Average Pass Ratio
# https://leetcode.com/problems/maximum-average-pass-ratio/description

from typing import List
import functools

# my 1043ms Beats70.00%
import heapq
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        classes = [((p/n - (p+1)/(n+1)),p,n) for p,n in classes]
        heapq.heapify(classes)

        for _ in range(extraStudents) :
            _,p,n = heapq.heappop(classes)
            # print(p,n)
            n += 1
            p += 1
            heapq.heappush(classes, ((p/n-(p+1)/(n+1)), p,n))
            # print((p/n-(p+1)/(n+1)), n,p)
            # print(classes)
        return sum(pass_n/stu_n for _, pass_n, stu_n in classes)/len(classes)

# given ans
# same, but (p/n-(p+1)/(n+1)) using function

s = Solution()
print("ans :",s.maxAverageRatio(classes = [[1,2],[3,5],[2,2]], extraStudents = 2)) #0.78333
print("ans :",s.maxAverageRatio(classes = [[2,4],[3,9],[4,5],[2,10]], extraStudents = 4)) #0.53485



