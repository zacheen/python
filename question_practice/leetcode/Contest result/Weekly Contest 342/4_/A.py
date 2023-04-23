from typing import List
import functools

# my 
import math
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # 只要有一個 1，再經過 n-1 步 其他就會變成 1
        count_1 = nums.count(1)
        if count_1 > 0 :
            return len(nums) - count_1
        
        # 應該是 BFS 但是沒想到 怎樣的步驟才算是最好的
        # 找跟隔壁重複項目是最少的 -> 看 gcd 之後的因數分解 哪個個數最少 ??
        print( math.gcd(10,15) )
        return 0

# given ans

s = Solution()
print(s.minOperations([2,6,3,4])) # 4
print(s.minOperations([2,10,6,14])) # -1
print(s.minOperations([10,15,6])) # 4



