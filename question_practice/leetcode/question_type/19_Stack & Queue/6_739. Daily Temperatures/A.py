from collections import deque
# my Runtime: 1258 ms, faster than 82.25% of Python3
class Solution:
    def dailyTemperatures(self, temperatures):
        stack = deque()
        ans = [0]*len(temperatures)
        for indx, tem in enumerate(temperatures) :
            
            while stack and stack[-1][0] < tem :
                top = stack.pop()
                ans[top[1]] = indx - top[1]
                
            stack.append((tem, indx))
        return ans

# given ans
# 跟我的想法一樣 只是stack裡面只存indx 我覺得這樣比較慢
# 不過還是一個很好看的寫法
# class Solution:
#     def dailyTemperatures(self, temperatures):
#         ans = [0] * len(temperatures)
#         stack = []

#         for i, t in enumerate(temperatures):
#             while stack and t > temperatures[stack[-1]]:
#                 index = stack.pop()
#                 ans[index] = i - index
#             stack.append(i)

#         return ans

s = Solution()
print(s.dailyTemperatures([73,74,75,71,69,72,76,73]))



