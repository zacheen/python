# 2463. Minimum Total Distance Traveled
# https://leetcode.com/problems/minimum-total-distance-traveled/description/

from typing import List
from math import inf
from bisect import bisect_left
from functools import lru_cache

# my 1740ms Beats22.39%
class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        factory.sort()
        robot.sort()
        # print(factory, robot)

        @lru_cache(None)
        def dp(ro_i, fac_i, remain):
            if ro_i == len(robot) :
                return 0
            while remain == 0 :
                fac_i += 1
                if fac_i == len(factory) :
                    return inf
                remain = factory[fac_i][1]
            
            # use this factory
            ret = dp(ro_i+1, fac_i, remain-1) + abs(robot[ro_i] - factory[fac_i][0])
            # dont use this factory
            if (r:=dp(ro_i, fac_i, 0)) < ret :
                ret = r
            return ret
        return dp(0,-1,0)

from collections import deque
# given ans : 31ms Beats99.00%
# 使用 queue 存放目前最佳結果，如果此結果不符合就移除
class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        len_r, len_f = len(robot), len(factory)
        dp = [[0]*(len_f) + [inf] for _ in range(len_r + 1)]
        for f_i in range(len_f - 1, -1, -1):
            fac_pos, fac_limit = factory[f_i]
            prefix = 0
            qq = deque([(len_r, 0)])
            for r_i in range(len_r - 1, -1, -1):
                prefix += abs(robot[r_i] - fac_pos) # prefix : 若第r_i個以後全部的robot放入此factory, 總距離是多少
                if qq[0][0]-r_i > fac_limit: # 如果已經放入的 robot 數量超過限制
                    qq.popleft()
                new_res = dp[r_i][f_i+1]-prefix # 一樣的放入的 robot 數量(r_i), 使用這個方法進步多少
                while qq and qq[-1][1] >= new_res:
                    qq.pop() # 拿掉較小的結果，讓q是嚴格遞增
                qq.append((r_i, new_res))
                dp[r_i][f_i] = qq[0][1]+prefix
        return dp[0][0]

s = Solution()
# print("ans :",s.minimumTotalDistance(robot = [0,4,6], factory = [[2,2],[6,2]])) # 
# print("ans :",s.minimumTotalDistance(robot = [0,4,7], factory = [[2,2],[6,2]])) # 
print("ans :",s.minimumTotalDistance(robot = [1,-1], factory = [[-2,1],[2,1]])) # 
# print("ans :",s.minimumTotalDistance(robot = [-840831288, -671200998, -600989788, -592135328, 209726656, 529140594, 789300819], factory = 
#     [[-912630111, 0], [-865262624, 6], [-769206598, 2], [-717666169, 0], [-467185764, 3], [-299780916, 4], [-292158515, 6], [-235385712, 2], [-159433745, 5], [54441577, 3], [75791769, 3], [83034539, 2], [258278787, 0], [270903707, 3], [449443632, 3], [725929046, 2], [849991650, 7], [940410553, 6]])) # 



