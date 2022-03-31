from bisect import bisect_right
# My Runtime: 90 ms, faster than 77.67% of Python3
class Solution:
    def insert(self, intervals, newInterval):
        # corner case
        if len(intervals) == 0:
            return [newInterval]
        
        insert_place = bisect_right(intervals, newInterval)
        # 或使用下面 因為 key 經過 lambda 運算是int 所以 newInterval 只能傳newInterval[0] 進去
        # insert_place = bisect_right(intervals, newInterval[0] , key = lambda x : x[0]) 

        # print("insert_place :",insert_place)

        # corner case 被包起來
        if intervals[insert_place-1][0] < newInterval[0] and intervals[insert_place-1][1] > newInterval[1] :
            return intervals

        while insert_place < len(intervals) :
            if newInterval[1] >= intervals[insert_place][0] :
                # 後面的項目有重疊
                newInterval[1] = max(newInterval[1], intervals[insert_place][1])
                del(intervals[insert_place])
            else :
                break
        # print(intervals)
    
        left = insert_place-1
        while left > -1:
            if newInterval[0] <= intervals[left][1] :
                # 前面的項目有重疊
                newInterval[0] = min(newInterval[0], intervals[left][0])
                del(intervals[left])
                left -= 1
            else :
                break

        intervals.insert(left+1, newInterval)
        return intervals

# 另外一個想法 是從兩邊找回來 相交代表都沒有重疊
# 好處是不用處理 corner case

# given ans
# 跟我第二個想法很像 不過更好 而且我沒有想到newInterval會變的事情
# class Solution:
#     def insert(self, intervals, newInterval):
#         n = len(intervals)
#         ans = []
#         i = 0

#         # 找要保留的左邊項目
#         while i < n and intervals[i][1] < newInterval[0]:
#             ans.append(intervals[i])
#             i += 1

#         # 找要合併的中間項目
#         while i < n and intervals[i][0] <= newInterval[1]:
#             newInterval[0] = min(newInterval[0], intervals[i][0])
#             newInterval[1] = max(newInterval[1], intervals[i][1])
#             i += 1

#         ans.append(newInterval)

#         # 加回要保留的右邊項目
#         while i < n:
#             ans.append(intervals[i])
#             i += 1

#         return ans

s = Solution()
# print(s.insert(intervals = [[1,3],[6,9]], newInterval = [2,5]))
# print(s.insert(intervals = [[2,3],[6,9]], newInterval = [0,1]))
# print(s.insert(intervals = [[2,3],[6,9]], newInterval = [10,11]))
# print(s.insert(intervals = [[2,3],[6,9]], newInterval = [0,2]))
# print(s.insert(intervals = [[2,3],[6,9]], newInterval = [9,11]))
print(s.insert(intervals = [[1,5]], newInterval = [2,3]))  # 被包圍
