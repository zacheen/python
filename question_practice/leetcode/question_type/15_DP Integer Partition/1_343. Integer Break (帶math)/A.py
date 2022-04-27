# my Runtime: 32 ms, faster than 92.26% of Python3
class Solution:
    def integerBreak(self, n):
        # @cache
        def dp(i):
            max_product = i
            for part in range(1,i):
                # print(part, (i-part), dp(part))
                max_product = max(dp(part)*(i-part), max_product)
            
            print(i, max_product)
            return max_product
        
        # 因為一定要拆一次
        return max([dp(i)*(n-i) for i in range(1,n)])

# given ans
# 用有關數學的方式計算的
# class Solution:
#     def integerBreak(self, n):
#         if n == 2:
#             return 1
#         if n == 3:
#             return 2

#         ans = 1

#         while n > 4:
#             n -= 3
#             ans *= 3
#         ans *= n

#         return ans

s = Solution()
# print(s.integerBreak(2)) # 1
# print(s.integerBreak(3)) # 2
# print(s.integerBreak(4)) # 2
print(s.integerBreak(10)) # 36



