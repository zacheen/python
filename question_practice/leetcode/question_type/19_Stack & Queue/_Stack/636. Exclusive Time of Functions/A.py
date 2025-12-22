# 636. Exclusive Time of Functions
# https://leetcode.com/problems/exclusive-time-of-functions

from typing import List
from math import inf

# my v2 I know raise Exception will not be executed
    # 2ms Beats97.63%
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = [[0, 0]]
        cnt = [0]*n
        for s in logs :
            tid, act, t = s.split(":")
            tid = int(tid)
            t = int(t)
            if act == "start" :
                stack.append( [t, 0] )
            else :
                st_t, interrupt = stack.pop()
                total_period = (t-st_t+1)
                cnt[tid] += total_period - interrupt
                stack[-1][-1] += total_period
        return cnt

# class Solution:
#     def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
#         stack = [[-1, 0, 0]]
#         cnt = [0]*n
#         for s in logs :
#             tid, act, t = s.split(":")
#             tid = int(tid)
#             t = int(t)
#             if act == "start" :
#                 stack.append( [tid, t, 0] )
#             else :
#                 pre_tid, st_t, interrupt = stack.pop()
#                 if tid != pre_tid :
#                     raise Exception
#                 total_period = (t-st_t+1)
#                 cnt[tid] += total_period - interrupt
#                 stack[-1][-1] += total_period
#         return cnt


s = Solution()
print("ans :",s.exclusiveTime(2, ["0:start:0","1:start:2","1:end:5","0:end:6"])) # [3,4]
print("ans :",s.exclusiveTime(n = 1, logs = ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"])) # 
print("ans :",s.exclusiveTime(n = 2, logs = ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"])) # 
print("ans :",s.exclusiveTime(n = 3, logs = ["0:start:0","1:start:2","1:end:5","2:start:6","2:end:7","0:end:10"])) # 



