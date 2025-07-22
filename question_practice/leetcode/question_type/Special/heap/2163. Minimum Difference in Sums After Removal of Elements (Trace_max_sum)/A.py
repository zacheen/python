# 2163. Minimum Difference in Sums After Removal of Elements
# https://leetcode.com/problems/minimum-difference-in-sums-after-removal-of-elements

from typing import List
from math import inf
from heapq import heapify, heappush, heappop

# my : 369ms Beats70.88%
class Trace_max_sum:
    def __init__(self, nums):
        self.heap = nums
        heapify(self.heap)
        self.sum = sum(nums)
    
    def add(self, n):
        heappush(self.heap, n)
        self.sum += n - heappop(self.heap)

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        len_n = len(nums) // 3

        # 前半部是要愈小愈好 > 每次都是丟掉最大的
        max_s = Trace_max_sum(list(-n for n in nums[:len_n]))
        mem_front = []
        mem_front.append(-max_s.sum)
        for n in nums[len_n:-len_n] :
            max_s.add(-n)
            mem_front.append(-max_s.sum)
        # print(mem_front)
        
        # 後半部是要愈大愈好
        max_s = Trace_max_sum(nums[-len_n:])
        min_ans = mem_front.pop()-max_s.sum
        for n in nums[-len_n-1:len_n-1:-1] :
            max_s.add(n)
            if (new_ans := mem_front.pop()-max_s.sum) < min_ans :
                min_ans = new_ans
        return min_ans

# given ans : concept is the same, but the implementation is different
    # might because I use class to implement, so the speed is slower

s = Solution()
print("ans :",s.minimumDifference([3,1,2])) # [1] - [2] > -1
print("ans :",s.minimumDifference([7,9,5,8,1,3])) # [7,5] - [8,3] > 1
# print("ans :",s.minimumDifference()) # 



