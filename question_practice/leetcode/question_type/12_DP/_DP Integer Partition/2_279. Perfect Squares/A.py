# my Runtime: 3864 ms, faster than 53.59% of Python3
class Solution:
    def numSquares(self, n):
        square = []
        i = 1
        while True :
            now_squ = i**2
            if now_squ > n :
                break
            square.append(now_squ)
            i+=1
        # print(square)
        
        ll = [0]+[n]*n
        for num in reversed(square) : 
            for ii in range(num, n+1):
                ll[ii] = min(ll[ii], ll[ii-num]+1)
        
        # print(ll)
        return ll[n]

# given ans 我的比較快
# Runtime: 5277 ms, faster than 5.02% of Python3
# class Solution:
#     def numSquares(self, n):
#         dp = [n+1] * (n + 1)

#         dp[0] = 0
#         dp[1] = 1

#         for i in range(2, n + 1):
#             j = 1
#             while j * j <= i:
#                 dp[i] = min(dp[i], dp[i - j * j] + 1)
#                 j += 1

#         print(dp)
#         return dp[n]

s = Solution()
# print(s.numSquares(12)) # 3
# print(s.numSquares(13)) # 2
print(s.numSquares(20))



