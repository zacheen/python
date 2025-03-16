# 2594. Minimum Time to Repair Cars
# https://leetcode.com/problems/minimum-time-to-repair-cars

from typing import List
from math import inf
from bisect import bisect_left
from math import isqrt
# my using template bisect : 692ms Beats52.23%
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def check(mid: int) -> bool:
            total = sum(isqrt(mid//r) for r in ranks)
            return total >= cars
        return bisect_left(range(ranks[0]*(cars**2)+1), True, key=check)

# my using template binarySearch_adv2 : 690ms Beats52.23%
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def check(mid: int) -> bool:
            total = sum(isqrt(mid//r) for r in ranks)
            return total < cars
        left, right = 0, ranks[0]*(cars**2)+1
        while left < right:
            mid = (left + right) // 2
            if check(mid) : 
                left = mid + 1 
            else:
                right = mid 
        return left

# given ans : optimized check : 223ms Beats91.57%
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def check(mid: int) -> bool:
            total = 0
            for r in ranks :
                total += isqrt(mid//r)
                if total >= cars :
                    return True
            return False
        return bisect_left(range(ranks[0]*(cars**2)+1), True, key=check)

s = Solution()
# print("ans :",s.repairCars(ranks = [4,2,3,1], cars = 10)) # 
# print("ans :",s.repairCars(ranks = [5,1,8], cars = 6)) # 
print("ans :",s.repairCars(ranks = [1,1,3,3], cars = 74)) # 



