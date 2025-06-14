# 480. Sliding Window Median
# https://leetcode.com/problems/sliding-window-median/description/
from typing import List

# my template Median_twoHeap: 83ms Beats87.45%
from heapq import heappush, heappop, heapify
from collections import Counter
class Median_twoHeap:
    def __init__(self, nums):
        nums.sort()
        self.small = [-n for n in nums[:len(nums)//2]]
        heapify(self.small)
        self.big = nums[len(nums)//2:]
        heapify(self.big)
        self.bal = len(self.big)-len(self.small) # 看 big 比 small 多多少
        self.removals = Counter()

    def balance(self):
        while self.bal > 1:
            heappush(self.small, -heappop(self.big))
            self.bal -= 2
        while self.bal < 0:
            heappush(self.big, -heappop(self.small))
            self.bal += 2

        # 因為我 remove 的時候預設是放到 self.big 裡面，所以要先扣 self.big 的
        while self.big and self.removals[self.big[0]]:
            self.removals[self.big[0]] -= 1
            heappop(self.big)
        
        while self.small and self.removals[-self.small[0]]:
            self.removals[-self.small[0]] -= 1
            heappop(self.small)

    def add(self, num):
        if self.big and num >= self.big[0] :
            self.bal += 1
            heappush(self.big, num)
        else:
            self.bal -= 1
            heappush(self.small, -num)
                
    def remove(self, num):
        self.removals[num] += 1
        if num >= self.big[0] :
            self.bal -= 1
        else :
            self.bal += 1
    
    # 找中位數
    def get_median(self):
        self.balance()
        if self.bal :
            return self.big[0]
        else :
            return (self.big[0] - self.small[0])/2

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        ans = []
        med = Median_twoHeap(nums[:k])
        ans.append(med.get_median())
        for i, new_n in enumerate(nums[k:]) :
            med.add(new_n)
            med.remove(nums[i])
            ans.append(med.get_median())
        return ans

from sortedcontainers import SortedList
# my template Median_SortedList : 237ms Beats39.75%
class Median_SortedList:
    def __init__(self, nums):
        self.nums = SortedList(nums)
        self.med_i = len(nums)//2
        self.med_e_i = self.med_i-1
        self.odd_f = (len(nums)&1)

    def get_med(self):
        if self.odd_f :
            return self.nums[self.med_i]
        else :
            return (self.nums[self.med_e_i] + self.nums[self.med_i])/2
    
    def add(self, add_n):
        self.nums.add(add_n)

    def remove(self, remove_n):
        self.nums.remove(remove_n)

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        ans = []
        med = Median_SortedList(nums[:k])
        ans.append(med.get_med())
        for i, new_n in enumerate(nums[k:]) :
            med.add(new_n)
            med.remove(nums[i])
            ans.append(med.get_med())
        return ans

s = Solution()
print(s.medianSlidingWindow([1,3,-1,-3,5,3,6,7],3)) # [1, -1, -1, 3, 5, 6]
print(s.medianSlidingWindow([1,4,2,3], 4)) # [2.50000]
print(s.medianSlidingWindow([1,1,1,1], 2)) # [1.0, 1.0, 1.0]



