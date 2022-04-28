# my Runtime: 72 ms, faster than 68.96% of Python3
class Solution:
    def maxProfit(self, prices):
        mem_0 = 0 # 我沒有股票 且 目前總共賺到多少錢 且 這一回合可以買股票
        mem_1 = -prices[0] # 我有一支股票 且 目前總共賺到多少錢
        # print(mem_0_F, mem_0_T, mem_1)
        
        for p in prices :
            mem_0,mem_1 = \
                max(mem_1 + p, mem_0) , \
                max(mem_0 - p, mem_1)
            
        return mem_0

# given ans 一樣

s = Solution()
print(s.())



