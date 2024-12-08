# 3361. Shift Distance Between Two Strings
# https://leetcode.com/problems/shift-distance-between-two-strings/description/

from typing import List
import functools

# my 305ms Beats98.21%
class Solution:
    def shiftDistance(self, s: str, t: str, nextCost: List[int], previousCost: List[int]) -> int:
        # 計算出全部位置到任何位置的 cost
        cost_mem = [[0]*26 for _ in range(26)]
        # 先往右 (next)
        for st in range(26):
            total_cost = 0
            for interval in range(25):
                en = st + interval
                if en >= 26 :
                    en = en-26
                total_cost += nextCost[en]
                cost_mem[st][(en+1)%26] = total_cost
        # 再往左 (next)
        for st in range(26):
            total_cost = 0
            for interval in range(26):
                en = st - interval
                if en < 0 :
                    en = en+26
                total_cost += previousCost[en]
                cost_mem[st][(en-1)%26] = min(total_cost, cost_mem[st][(en-1)%26])
        # print(cost_mem)
        
        ans_sum = 0
        shift_num = ord("a")
        for each_s, each_t in zip(s,t):
            s_num = ord(each_s) - shift_num
            t_num = ord(each_t) - shift_num
            ans_sum += cost_mem[s_num][t_num]
    
        return ans_sum
    
# # given ans # 252ms Beats 99.43%
# It's faster, but I don't know why
# class Solution:
#     def shiftDistance(self, s: str, t: str, nextCost: List[int], previousCost: List[int]) -> int:
#         # Total unique costs - changing each letter to each other letter 
#         # which is (25 * 25)(Total combinations) * (2 * 25)-Traversing next and prevCost arrays 
#         # 4 * 10**4 (Max) - without caching 25 * 10**5
#         prevCostSum = sum(previousCost)
#         nextCostSum = sum(nextCost)

#         @cache # Cache Size - 25*25
#         def findMinCost(a, b):
#             idx1, idx2 = ord(a) - ord('a'), ord(b) - ord('a')
#             if idx1 < idx2:
#                 cost1 = sum(nextCost[idx1:idx2])
#                 cost2 = prevCostSum - sum(previousCost[idx1+1:idx2+1])
#             else:
#                 cost1 = nextCostSum - sum(nextCost[idx2:idx1])
#                 cost2 = sum(previousCost[idx2+1:idx1+1])
#             print(cost1, cost2)
#             return min(cost1, cost2)
            
#         totalCost = 0
#         n = len(s)
#         for i in range(n):
#             if s[i] != t[i]:
#                 totalCost += findMinCost(s[i], t[i])
#         return totalCost

s = Solution()
print("ans :",s.shiftDistance( s = "abab", t = "baba", nextCost = [100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], previousCost = [1,100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]))



