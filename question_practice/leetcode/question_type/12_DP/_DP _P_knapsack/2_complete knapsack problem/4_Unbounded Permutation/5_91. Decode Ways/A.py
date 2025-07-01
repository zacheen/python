# 91. Decode Ways
# https://leetcode.com/problems/decode-ways/description/

# my using template knapsack
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [1]
        dp.append(0 if s[0] == '0' else 1)
        for end_i in range(1,len(s)) :
            cou = 0
            if '1' <= s[end_i] <= '9' :
                cou = dp[-1]
            if '10' <= s[end_i-1:end_i+1] <= '26' :
                cou += dp[-2]
            dp.append(cou)
        # print(dp)
        return dp[-1]

# my Runtime: 36 ms, faster than 82.07% of Python3
class Solution:
    def numDecodings(self, s):

        bond = len(s)-1
        # s[i:] 一共有幾種組合
        # @cache
        def dp(i):
            if i == len(s) :
                return 1

            if s[i] == "0" :
                return 0

            if i == bond :
                return 1

            # 每次選擇可以挑一個數次 或 挑兩個數字
            if int(s[i:i+2]) <= 26 :
                return dp(i+1) + dp(i+2)
            else :
                return dp(i+1)

        return dp(0)

s = Solution()
print(s.numDecodings("12"))
print(s.numDecodings("226"))
print(s.numDecodings("06"))
print(s.numDecodings("0"))
