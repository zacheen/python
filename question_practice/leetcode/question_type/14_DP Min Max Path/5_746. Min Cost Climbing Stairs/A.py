# my Runtime: 69 ms, faster than 68.26% of Python3
# class Solution:
#     def minCostClimbingStairs(self, cost):
#         dp = [0]*len(cost)
#         dp[0] = cost[0]
#         dp[1] = cost[1]
        
#         for i in range(2,len(cost)) :
#             dp[i] = cost[i] + min(dp[i-1], dp[i-2])
            
#         return min(dp[-1], dp[-2])

# given ans
# 使用原本的 List
class Solution:
    def minCostClimbingStairs(self, cost):
        # cost.append(0)
        for i in range(2, len(cost)):
            cost[i] += min(cost[i - 1], cost[i - 2])
        return min(cost[-1], cost[-2])

s = Solution()
print(s.minCostClimbingStairs([10,15,20]))
print(s.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))



