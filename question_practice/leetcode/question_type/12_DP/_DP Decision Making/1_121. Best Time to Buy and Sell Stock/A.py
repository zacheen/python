# my Runtime: 1435 ms, faster than 40.55% of Python3
class Solution:
    def maxProfit(self, prices):
        # min_p = prices[0]  # 不懂為什麼用inf比較快 ?
        # 明明 初始化inf比較慢 max,min也是inf比較慢
        min_p = math.inf
        max_pro = 0
        for p in prices:
            min_p = min(min_p, p)
            max_pro = max(max_pro, p - min_p)
        return max_pro

# given ans
class Solution:
    def maxProfit(self, prices):
        sellOne = 0
        holdOne = -math.inf

        for price in prices:
            sellOne = max(sellOne, holdOne + price)
            holdOne = max(holdOne, -price)

        return sellOne

s = Solution()
print(s.())



