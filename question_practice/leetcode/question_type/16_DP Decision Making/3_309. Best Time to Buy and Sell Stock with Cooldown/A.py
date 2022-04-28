# my 39 Runtime: 44 ms, faster than 86.41% of Python3
class Solution:
    def maxProfit(self, prices):
        mem_0_F = 0 # 我沒有股票 且 目前總共賺到多少錢 且 這一回合可以買股票
        mem_0_T = 0 # 我沒有股票 且 目前總共賺到多少錢 且 這一回合cooldown
        mem_1 = -prices[0] # 我有一支股票 且 目前總共賺到多少錢
        # print(mem_0_F, mem_0_T, mem_1)
        
        for p in prices[1:] :
            mem_0_F,mem_0_T,mem_1 = \
                max(mem_0_T, mem_0_F) , \
                mem_1 + p , \
                max(mem_0_F - p, mem_1)
            
            # print(mem_0_F, mem_0_T, mem_1)
            
        return max(mem_0_F, mem_0_T)

# given ans 概念一樣
# 我是把第一步先做好
# given ans 是 for 每個 price
# class Solution:
#     def maxProfit(self, prices):
#         sell = 0
#         hold = -math.inf
#         prev = 0

#         for price in prices:
#             cache = sell
#             sell = max(sell, hold + price)
#             hold = max(hold, prev - price)
#             prev = cache
#         return sell

s = Solution()
print(s.maxProfit([1,2,3,0,2]))
print(s.maxProfit([1]))
print(s.maxProfit([1,2,4]))



