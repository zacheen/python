from typing import List
import functools

# # my 
# import math
# class Solution:
#     def minOperations(self, nums: List[int]) -> int:
#         # 只要有一個 1，再經過 n-1 步 其他就會變成 1
#         count_1 = nums.count(1)
#         if count_1 > 0 :
#             return len(nums) - count_1
        
#         # 應該是 BFS 但是沒想到 怎樣的步驟才算是最好的
#         # 找跟隔壁重複項目是最少的 -> 看 gcd 之後的因數分解 哪個個數最少 ??
#         print( math.gcd(10,15) )
#         return 0

# given ans 我有優化
# 這個是有關數學的 
    # 如果全部的數字的最大公因數是 1 -> 就可以透過 j - i + 1 個步數 讓其中一個數字變成 1
from math import gcd

# # original 
# class Solution:
#     def minOperations(self, nums: List[int]) -> int:
#         if 1 in nums:
#             return len(nums) - nums.count(1)
#         res = -1
#         for i in range(len(nums)):
#             for j in range(i, len(nums)):
#                 d = nums[j]
#                 for k in range(i, j):
#                     d = gcd(d, nums[k])
#                 if d == 1:
#                     if res == -1 or j - i + 1 < res:
#                         res = j - i + 1
#         if res == -1:
#             return -1
#         return len(nums) + res - 2
    
# 我優化 Beats 75%
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count_1 = nums.count(1)
        if count_1 > 0 :
            return len(nums) - count_1
        
        # 找出 i~j 最大公因數是多少 
        res = len(nums)+1
        for i in range(len(nums)):
            # 找出這個範圍內 的最大公因數
            d = nums[i]
            for j in range(i, min(len(nums), i+res)):
                d = gcd(d, nums[j])
                # 如果最大公因數是 1
                if d == 1:
                    # range length j - i + 1
                    res = min(j - i + 1, res)
                    break # 因為這一定是最小的 range
        
        if res == len(nums)+1:
            return -1
        return len(nums) + res - 2
    
# 我再再優化 sliding window Beats 56.25%
# 看起來 gcd 的時間複雜度比我想像的還要小
# 所以我這個才會比較慢
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count_1 = nums.count(1)
        if count_1 > 0 :
            return len(nums) - count_1
        
        max_l = 0
        r = 0
        d = nums[r]
        min_range = len(nums)+1 # 因為上面判斷過一定有解 所以有解的最大 range 就是全部
        for r in range(len(nums)) :
            d = gcd(d, nums[r])
            if d == 1 :
                # 尋找 l 的位置
                d = nums[r]
                last_d = d
                for l in range(r, max_l-1, -1):
                    d = gcd(d, nums[l])
                    if d == 1 :
                        min_range = min(min_range, r-l+1)
                        max_l = l
                        d = last_d
                        break
                    else :
                        last_d = d
        if min_range == len(nums)+1:
            return -1
        return len(nums) + min_range - 2

s = Solution()
print(s.minOperations([2,6,3,4])) # 4
print(s.minOperations([2,10,6,14])) # -1
print(s.minOperations([10,15,6])) # 4



