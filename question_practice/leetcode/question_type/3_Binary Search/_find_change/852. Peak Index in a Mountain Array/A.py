# 852. Peak Index in a Mountain Array
# https://leetcode.com/problems/peak-index-in-a-mountain-array

from typing import List
from math import inf

# my 
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = 0
        r = len(arr)-1
        while l < r-1 :
            mid = (l+r) >> 1
            if arr[mid] < arr[mid+1] :
                l = mid
            else :
                r = mid
        if arr[r] > arr[l] : return r
        else : return l

s = Solution()
print("ans :",s.peakIndexInMountainArray([0,1,0])) # 1
print("ans :",s.peakIndexInMountainArray([0,2,1,0])) # 1
print("ans :",s.peakIndexInMountainArray([0,10,5,2])) # 1



