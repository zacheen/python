# my Runtime: 1732 ms, faster than 66.19% of Python3
class Solution:
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key=lambda x : x[1])  # 目前有點抓不到要用 x[0] sort 還是 x[0] ??
        print(intervals)
        last = [intervals[0][0]-1, intervals[0][0]-1]   
        ans = 0
        for each in intervals :
            if last[1] > each[0] :
                print(last, each)
                ans += 1
                continue
            last = each
        return ans

s = Solution()
print(s.eraseOverlapIntervals([[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]]))
# print(s.eraseOverlapIntervals([[1,10],[2,3],[3,4],[5,6]]))
# print(s.eraseOverlapIntervals([[1,2],[2,10],[3,4],[5,6],[7,8]]))
