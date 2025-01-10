# 56. Merge Intervals
# https://leetcode.com/problems/merge-intervals/

# My 5ms Beats82.76%
class Solution:
    def merge(self, intervals):
        intervals.sort()
        last = intervals[0]
        ans = []
        for inter in intervals :
            if last[1] >= inter[0] :
                last[1] = max(last[1], inter[1])
            else :
                ans.append(last)
                last = inter
        ans.append(last)
        return ans

# # given ans
# # 直接紀錄在 ans 裡面, but it takes time to get ans[-1][1]
# class Solution:
#     def merge(self, intervals):
#         ans = []
#         for interval in sorted(intervals):
#             if not ans or ans[-1][1] < interval[0]:
#                 ans.append(interval)
#             else:
#                 ans[-1][1] = max(ans[-1][1], interval[1])
#         return ans

s = Solution()
print(s.merge(intervals = [[1,3],[2,6],[8,10],[15,18]]))

