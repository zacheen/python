# my Beats Beats 99.63%
import math
class Solution:
    def mincostTickets(self, days, costs):
        max_day = max(days)
        need_days = set(days)
        mem = [0]+[math.inf] * max_day
        # 計算到此天 最少的買法 
        for d in range(1,max_day+1) :
            if d in need_days :
                buy1 = costs[0] + mem[d-1]
                buy7 = costs[1]
                buy30 = costs[2]
                if (d-7) >= 0 : 
                    buy7 += mem[d-7]
                    if (d-30) >= 0 : 
                        buy30 += mem[d-30]
                mem[d] = min(buy1, buy7, buy30)
            else :
                mem[d] = mem[d-1]
            # print(mem)

        return mem[-1]

# given ans Beats 99.26%
# 是針對要去的天數去找最佳解
    # 紀錄 N 天後 各種買法 需要多少錢
    # 把今天的金額取出 找出最小的
from collections import deque
class Solution:
    def mincostTickets(self, days, costs):
        ans = 0
        last7 = deque()
        last30 = deque()

        for day in days:
            while last7 and (last7[0][0] + 7) <= day:
                last7.popleft()
            while last30 and (last30[0][0] + 30) <= day:
                last30.popleft()
            # 把 N 天後所需的花費加入 List 中
            last7.append((day, ans + costs[1]))
            last30.append((day, ans + costs[2]))
            ans = min(ans + costs[0], last7[0][1], last30[0][1])

        return ans
  
s = Solution()
print(s.mincostTickets(days = [1,4,6,7,8,20], costs = [2,7,15]))
# print(s.mincostTickets(days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]))
# print(s.mincostTickets(days = [1,4,6,7,8,20], costs = [7,2,15]))



