# 2285. Maximum Total Importance of Roads
# https://leetcode.com/problems/maximum-total-importance-of-roads

from typing import List
import functools

# my 1193ms Beats86.48%
class Solution:
    def maximumImportance(self, n, roads):
        counter = [0]*n
        for p1,p2 in roads :
            counter[p1] += 1
            counter[p2] += 1
        
        counter.sort()
        # print(counter)

        # [(indx+1)*cou for indx, cou in enumerate(counter)]
        return sum([indx*cou for indx, cou in zip(range(1,n+1), counter)])

# given ans
# the same

s = Solution()
print(s.maximumImportance(n = 5, roads = [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]))
print(s.maximumImportance(n = 5, roads = [[0,3],[2,4],[1,3]]))



