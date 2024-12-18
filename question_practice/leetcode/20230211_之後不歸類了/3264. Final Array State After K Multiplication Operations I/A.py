# 3264. Final Array State After K Multiplication Operations I
# https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-i/description

from typing import List
import functools

# my 3ms Beats52.21%
import heapq
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap_list = [(n,i) for i, n in enumerate(nums)]
        heapq.heapify(heap_list)
        for _ in range(k):
            n,i = heapq.heappop(heap_list)
            heapq.heappush(heap_list, (n*multiplier,i))
        for n,i in heap_list :
            nums[i] = n
        return nums

# given ans
# same but directly change original list
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int):
        pq = [(val, i) for i, val in enumerate(nums)]
        heapq.heapify(pq)

        for _ in range(k):
            _, i = heapq.heappop(pq)
            nums[i] *= multiplier
            heapq.heappush(pq, (nums[i], i))

        return nums

s = Solution()
print("ans :",s.getFinalState(nums = [2,1,3,5,6], k = 5, multiplier = 2))



