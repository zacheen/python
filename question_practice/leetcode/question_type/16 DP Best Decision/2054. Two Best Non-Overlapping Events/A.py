# 2054. Two Best Non-Overlapping Events
# https://leetcode.com/problems/two-best-non-overlapping-events/description
# 這題是最多的兩個 不是任意個

from typing import List
import functools

# my 151ms Beats77.67%
class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        # 新的一個 看在這之前最大是多少
        # 為了看最大是多少 要記錄到目前為止已經end的value
        sta_list = [(st,val) for st,en,val in events]
        sta_list.sort()
        en_list = [(en,val) for st,en,val in events]
        en_list.sort(reverse=True)
        max_ans = 0
        now_end_max = 0
        for st,st_val in sta_list :
            while en_list[-1][0] < st :
                en, ev_val = en_list.pop()
                now_end_max = max(now_end_max, ev_val)
            max_ans = max(max_ans, now_end_max + st_val)
        return max(max_ans, max(ev_val for en, ev_val in en_list))

# my opt 136ms Beats91.26%
    # using original list
class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        # 新的一個 看在這之前最大是多少
        # 為了看最大是多少 要記錄到目前為止已經end的value
        en_list = [(en,val) for st,en,val in events]
        en_list.sort(reverse=True)
        events.sort()
        max_ans = 0
        now_end_max = 0
        for st,_,st_val in events :
            while en_list[-1][0] < st :
                now_end_max = max(now_end_max, en_list.pop()[1])
            max_ans = max(max_ans, now_end_max + st_val)
        return max(max_ans, max(ev_val for en, ev_val in en_list))

# # given ans
# # same concept, but slower
# class Solution:
#     def maxTwoEvents(self, events: List[List[int]]) -> int:
#         ans = 0
#         maxValue = 0
#         evts = []    # (time, isStart, value)

#         for s, e, v in events:
#             evts.append((s, 1, v))
#             evts.append((e + 1, 0, v))

#         # When two events have the same time, the one is not start will be in the front
#         evts.sort()

#         for _, isStart, value in evts:
#             if isStart:
#                 ans = max(ans, value + maxValue)
#             else:
#                 maxValue = max(maxValue, value)
#             print(_, isStart, value, ans, maxValue)

#         return ans



s = Solution()
print("ans :",s.maxTwoEvents(events = [[1,3,2],[4,5,2],[2,4,3]])) # 4
print("ans :",s.maxTwoEvents(events = [[1,3,2],[4,5,2],[1,5,5]])) # 5
print("ans :",s.maxTwoEvents(events = [[1,5,3],[1,5,1],[6,6,5]])) # 8
print("ans :",s.maxTwoEvents(events = [[1,5,3],[1,5,1],[6,6,5]])) # 8
print("ans :",s.maxTwoEvents(events = [[1,2,2],[3,4,3],[5,6,4],[2,5,7]]))
    # not 9 because just choosing 2
# print("ans :",s.maxTwoEvents(events = [[1,3,2],[3,5,2],[2,4,3]]))
print("ans :",s.maxTwoEvents(events = [[22,44,9],[93,96,48],[56,90,3],[80,92,45],[63,73,69],[73,96,33],[11,23,84],[59,72,29],[89,100,46]]))
# print("ans :",s.maxTwoEvents())



