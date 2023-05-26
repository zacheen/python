# 2542. Maximum Subsequence Score
# https://leetcode.com/problems/maximum-subsequence-score/description/

from typing import List
import functools

# given ans Beats 44.27%
import heapq
class Solution:
    # Same as 1383. Maximum Performance of a Team
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # A = sorted([(n2, n1) for n1, n2 in zip(nums1, nums2)], reverse=True)
        A = sorted(zip(nums2, nums1), reverse=True)
        minHeap = []
        ans = 0
        nums1_sum = 0
        # 可以想成我把 Min(nums2) 固定下來，然後去找所有符合的項目，挑出最大的 nums1 
        for n2, n1 in A:
            heapq.heappush(minHeap, n1)
            nums1_sum += n1
            if len(minHeap) > k:
                nums1_sum -= heapq.heappop(minHeap)
            if len(minHeap) == k:
                ans = max(ans, nums1_sum * n2)
        return ans
    
s = Solution()
print(s.maxScore(nums1 = [1,3,3,2], nums2 = [2,1,3,4], k = 3))
print(s.maxScore(nums1 = [4,2,3,1,1], nums2 = [7,5,10,9,6], k = 1))



