# 1035. Uncrossed Lines
# https://leetcode.com/problems/uncrossed-lines/description/

from typing import List
import functools

class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        # 從左到右 一個一個連
        # 每次一定是連最左邊的最好
        # 所以就只要判斷 要連或不要連

        @functools.lru_cache(None)
        def dfs(top, down) :
            if top == len(nums1) :
                return 0
            
            for i in range(down, len(nums2)) :
                if nums1[top] == nums2[i] :
                    return max(dfs(top+1, i+1)+1, dfs(top+1, down))
            return dfs(top+1, down)

        return dfs(0,0)
    
# # my v2 優化 : 省略一些推論可以不用做的
# # 不過看起來速度差不多
# class Solution:
#     def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
#         # 目前可以省略的 如果 dfs(x, y) 有做過了 dfs(x, y+n) 就不用試了
#         mem_min_y = [len(nums2)] * len(nums1)

#         @functools.lru_cache(None)
#         def dfs(top, down) :
#             if top == len(nums1) :
#                 return 0
            
#             if down > mem_min_y[top] :
#                 print("fast") # 看來沒有省略到任何東西
#                 return 0
            
#             for i in range(down, len(nums2)) :
#                 if nums1[top] == nums2[i] :
#                     mem_min_y[top] = i
#                     return max(dfs(top+1, i+1)+1, dfs(top+1, down))
#             mem_min_y[top] = down # 如果在 down 這個位置 top 找不到結果
#             return dfs(top+1, down)

#         ret = dfs(0,0)
#         # print(mem_min_y)
#         return ret

# given ans Beats 67.19%
# 使用 for 迴圈的 DP 方法
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i - 1][j - 1] + 1 \
                    if nums1[i - 1] == nums2[j - 1] \
                    else max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]
  

s = Solution()
print(s.maxUncrossedLines(nums1 = [1,4,2], nums2 = [1,2,4]))
print(s.maxUncrossedLines(nums1 = [2,5,1,2,5], nums2 = [10,5,2,1,5,2]))
print(s.maxUncrossedLines(nums1 = [1,3,7,1,7,5], nums2 = [1,9,2,5,1]))



