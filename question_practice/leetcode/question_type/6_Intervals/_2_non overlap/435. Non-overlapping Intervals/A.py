# 435. Non-overlapping Intervals
# https://leetcode.com/problems/non-overlapping-intervals/description/

# my 67ms Beats84.72%
class Solution:
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key = lambda x : x[1]) # only needed sorted by x[1], not (x[1], x[0])
        ans_cou = 0
        end = intervals[0][0]
        for inter in intervals :
            if end > inter[0] :
                ans_cou += 1
            else :
                end = inter[1]
        return ans_cou

s = Solution()
print(s.eraseOverlapIntervals([[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]]))
# print(s.eraseOverlapIntervals([[1,10],[2,3],[3,4],[5,6]]))
# print(s.eraseOverlapIntervals([[1,2],[2,10],[3,4],[5,6],[7,8]]))
