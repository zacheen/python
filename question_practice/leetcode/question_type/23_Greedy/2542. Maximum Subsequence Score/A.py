# 2542. Maximum Subsequence Score
# https://leetcode.com/problems/maximum-subsequence-score/description/
    # Same as 1383. Maximum Performance of a Team，不過這題是固定長度
from typing import List
import functools
from heapq import heapify, heapreplace

# my : 123ms Beats98.98%
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        score_p = [(n2,n1) for n2,n1 in zip(nums2, nums1)]
        score_p.sort(reverse = True)
        # e 會從大取到小 > 所以 e 就會是每次的 min_eff
        best_n1 = [n1 for n2,n1 in score_p[:k]]
        heapify(best_n1)
        now_n1_sum = sum(best_n1)
        ans = now_n1_sum*score_p[k-1][0]
        for n2,n1 in score_p[k:] :
            if n1 > best_n1[0] :
                now_n1_sum += n1-heapreplace(best_n1, n1)
                ans = max(ans, n2*now_n1_sum)
        return ans
    
s = Solution()
print(s.maxScore(nums1 = [1,3,3,2], nums2 = [2,1,3,4], k = 3)) # 12
print(s.maxScore(nums1 = [4,2,3,1,1], nums2 = [7,5,10,9,6], k = 1)) # 30



