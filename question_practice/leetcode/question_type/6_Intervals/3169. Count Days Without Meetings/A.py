# 3169. Count Days Without Meetings
# https://leetcode.com/problems/count-days-without-meetings
    # 其實跟 # 763. Partition Labels 很像
from typing import List
from math import inf

# my v2 : 75ms Beats94.46%
class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort(key = lambda x : x[0])
        ans = 0
        last_end = 0
        for st, en in meetings :
            if st > last_end :
                ans += (st-last_end-1)
            if en > last_end :
                last_end = en
        return ans + (days-last_end) # last meeting to days

# given ans

# # my v1 : Memory Limit Exceeded (didn't notice range)
#     # but this method would be faster, if "meetings.length" and "days" limit are the same
# from itertools import accumulate
# class Solution:
#     def countDays(self, days: int, meetings: List[List[int]]) -> int:
#         # starting from day 1 > days + 1 and ans -1
#         # end is includeed > additional days + 1 and ans -1
#         days += 2
#         mem = [0]*(days)
#         for st, end in meetings :
#             mem[st] += 1
#             mem[end+1] -= 1

#         ans = 0
#         for cou in accumulate(mem) :
#             if cou == 0 :
#                 ans += 1

#         ans -= 2
#         return ans

s = Solution()
print("ans :",s.countDays(days = 10, meetings = [[5,7],[1,3],[9,10]])) # 2
print("ans :",s.countDays(days = 5, meetings = [[2,4],[1,3]])) # 1
print("ans :",s.countDays(days = 6, meetings = [[1,6]])) # 0



