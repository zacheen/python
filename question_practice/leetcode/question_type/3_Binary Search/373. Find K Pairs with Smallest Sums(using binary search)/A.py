# 373. Find K Pairs with Smallest Sums
# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/

from typing import List
from math import inf
from bisect import bisect_right

# my 
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        def check(max_sum) :
            cnt = 0
            for n1 in nums1 :
                rem = max_sum - n1
                cnt += bisect_right(nums2, rem)
                if cnt > k :
                    return False
            return True
        
        l = nums1[0] + nums2[0] -1
        r = nums1[-1] + nums2[-1]
        while l < r-1 :
            mid = (l+r) >> 1
            # print(mid, check(mid))
            if check(mid) :
                l = mid
            else :
                r = mid
        
        if check(r) :
            max_sum = r
        else :
            max_sum = l

        # print("max_sum", max_sum)
        next_larger = nums1[-1] + nums2[-1]
        next_larger_list = []
        ans = []
        for n1 in nums1 :
            rem = max_sum - n1
            end_i = bisect_right(nums2, rem)
            ans += [(n1,n2) for n2 in nums2[:end_i]]
            
            while end_i < len(nums2) :
                new_larger_sum = n1 + nums2[end_i]
                if new_larger_sum < next_larger :
                    next_larger = new_larger_sum
                    next_larger_list = [(n1, nums2[end_i])]
                elif new_larger_sum == next_larger :
                    if len(next_larger_list) < k :
                        next_larger_list.append((n1, nums2[end_i]))
                    else :
                        break
                else :
                    break
                end_i += 1

        return ans + next_larger_list[:k-len(ans)]


s = Solution()
print("ans :",s.kSmallestPairs(nums1 = [1,7,11], nums2 = [2,4,6], k = 3)) # [(1, 2), (1, 4), (1, 6)]
print("ans :",s.kSmallestPairs(nums1 = [1,1,2], nums2 = [1,2,3], k = 2)) # [(1, 1), (1, 1)]



