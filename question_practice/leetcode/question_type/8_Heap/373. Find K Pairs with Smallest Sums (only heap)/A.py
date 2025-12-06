# 373. Find K Pairs with Smallest Sums
# https://leetcode.com/problems/find-k-pairs-with-smallest-sums

from typing import List
from math import inf
from heapq import heapify, heappop, heappush

# my 
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        n2 = nums2[0]
        # method 1
        # heap = list((n1+n2, n1_i, 0) for n1_i, n1 in enumerate(nums1)) # [sum, ptr to nums1, ptr to nums2]
        # Optimization
        heap = list((n1+n2, n1_i, 0) for n1_i, n1 in enumerate(nums1[:min(k, len(nums1))])) # [sum, ptr to nums1, ptr to nums2]
        heapify(heap)

        ans = []
        for _ in range(k):
            now_sum, n1_ptr, n2_ptr = heappop(heap)
            ans.append([nums1[n1_ptr], nums2[n2_ptr]])
            n2_ptr += 1
            if n2_ptr < len(nums2) :
                new_sum = nums1[n1_ptr] + nums2[n2_ptr]
                heappush(heap, (new_sum, n1_ptr, n2_ptr))
        return ans

s = Solution()
print("ans :",s.kSmallestPairs([1,7,11],[2,4,6],3)) # 
print("ans :",s.kSmallestPairs(nums1 = [1,1,2], nums2 = [1,2,3], k = 2)) # 



