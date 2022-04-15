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

# given ans
# 概念是一樣的 只是實作的方法不一樣
# class Solution:
#     def numDecodings(self, s):
#         n = len(s)
#         # dp[i] := # of ways to decode s[i..n)
#         dp = [0] * n + [1]

#         def isValid(a, b=None):
#             if b:
#                 return a == '1' or a == '2' and b < '7'
#             return a != '0'

#         if isValid(s[-1]):
#             dp[n - 1] = 1

#         for i in reversed(range(n - 1)):
#             if isValid(s[i]):
#                 dp[i] += dp[i + 1]
#             if isValid(s[i], s[i + 1]):
#                 dp[i] += dp[i + 2]

#         return dp[0]

s = Solution()
print(s.numDecodings("12"))
print(s.numDecodings("226"))
print(s.numDecodings("06"))
print(s.numDecodings("0"))
