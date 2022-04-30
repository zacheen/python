# my Runtime: 80 ms, faster than 78.66% of Python3
class Solution:
    def findMinDifference(self, timePoints):

        def change(s):
            s = s.split(":")
            return int(s[0])*60 + int(s[1])

        def diff(num1, num2) :
            d = abs(num1-num2)
            return min(d, 1440-d)

        timePoints = [change(s) for s in timePoints]
        timePoints.sort()
        # print(timePoints)
        mini = 1440
        for t1, t2 in zip(timePoints, timePoints[1:]+[timePoints[0]]) :
            mini = min(mini, diff(t1, t2))
        
        return mini

# given ans
# 概念一樣 但優化abs
# 只是因為sort完 b一定大於a 所以其實不需要 abs
# class Solution:
#     def findMinDifference(self, timePoints):
#         ans = 24 * 60
#         nums = sorted([int(timePoint[:2]) * 60 + int(timePoint[3:])
#                     for timePoint in timePoints])

#         for a, b in zip(nums, nums[1:]):
#             ans = min(ans, b - a)

#         return min(ans, 24 * 60 - nums[-1] + nums[0])

s = Solution()
# print(s.findMinDifference(["01:02","00:00"]))
print(s.findMinDifference(["00:00","23:59","00:00"]))



