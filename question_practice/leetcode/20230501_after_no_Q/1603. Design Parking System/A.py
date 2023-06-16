# 1603. Design Parking System
# https://leetcode.com/problems/design-parking-system/description/

from typing import List
import functools

# my Beats 91.61%
class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.remain = [0,big,medium,small]

    def addCar(self, carType: int) -> bool:
        if self.remain[carType] > 0 :
            self.remain[carType] -= 1
            return True
        return False

# given ans

# s = Solution()
# print(s.())



