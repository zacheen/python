# 96. Unique Binary Search Trees
# https://leetcode.com/problems/unique-binary-search-trees

# class cache:
#     def __init__(self, func):
#         self.func = func
#         self.data = {}

#     def __call__(self, *args, **kwargs):
#         func = self.func
#         data = self.data
#         key = f'{func.__name__}-{str(args)}-{str(kwargs)})'
#         if key in data:
#             result = data.get(key)
#             # print('cached')
#         else:
#             result = func(*args, **kwargs)
#             data[key] = result
#             # print('calculated')
#         return result

# 這題其實不是 Binary Search Trees
# 只是要計算出 有幾種 Binary Search Trees
# my Runtime: 34 ms, faster than 75.05% of Python3
# class Solution:
#     def numTrees(self, n):
        
#         @cache
#         def dp(n) :
#             if n == 1 or n == 0 :
#                 return 1
            
#             total = 0
#             # 扣除中間那一個 左邊可能的組合*右邊可能的組合
#             for i in range(n):
#                 total += dp(i)*dp(n-i-1)
#             return total

#         return dp(n)

# my 嘗試用for來寫
# Runtime: 26 ms, faster than 95.48% of Python3
class Solution:
    def numTrees(self, n):
        dp = [1]
        for i in range(1,n+1) :
            dp.append( sum(dp[now]*dp[i-now-1] for now in range(i)) )
        # print(dp)
        return dp[-1]

s = Solution()

print(s.numTrees(3))
print(s.numTrees(4))



