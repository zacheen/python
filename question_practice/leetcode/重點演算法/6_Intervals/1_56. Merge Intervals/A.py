# My 
# Runtime: 160 ms, faster than 79.80% of Python3 
# Runtime: 133 ms, faster than 99.79% of Python3
class Solution:
    def merge(self, intervals):
        intervals.sort(key = lambda x : x[0])
        # print(intervals)
        
        ans = []
        start = intervals[0][0]
        last = intervals[0][1]
        for each_interval in intervals :
            if each_interval[0] <= last :
                last = max(each_interval[1], last)
                # start = min(each_interval[0], start)  應該不用 因為一開始有sort了  所以第一個一定是最小的
            else :
                ans.append([start, last])
                start = each_interval[0]
                last = each_interval[1]
        ans.append([start, last])
        return ans

# given ans
# 直接紀錄在 ans 裡面
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

