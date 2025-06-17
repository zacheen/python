# 2616. Minimize the Maximum Difference of Pairs
# https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs
from typing import List
import functools
from bisect import bisect_left

# binary search :
    # 檢測 c 這個距離，能不能夠有足夠的 distance 可以符合條件
        # 因為已經 sort ，所以可以 greedy
            # n1, n2, n3 
            # 不知道 (n2-n1) ? (n3-n2)
            # 但是絕對 (n2-n1) < (n3-n1)
            # 所以如果 (n2-n1) 符合條件，絕對就可以符合
# my using bisect template : 308ms Beats92.71%
class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        for_lim_i = len(nums)-1
        # 使用二分法 找到最小可能的 diff
        def mid_too_small(mid):
            cou = 0
            i = 0
            while i < for_lim_i :
                if (nums[i+1] - nums[i]) <= mid :
                    cou += 1
                    i += 2
                else :
                    i += 1
            return cou >= p
        ret = bisect_left(range(nums[-1]-nums[0]+1), True, key=mid_too_small)
        return ret
    
# my v2 opt : 293ms Beats95.14%
class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0 : return 0
        nums.sort()
        for_lim_i = len(nums)-1
        # 使用二分法 找到最小可能的 diff
        def mid_too_small(mid):
            cou = 0
            i = 0
            while i < for_lim_i :
                if (nums[i+1] - nums[i]) <= mid :
                    cou += 1
                    if cou >= p :
                        return True
                    i += 2
                else :
                    i += 1
            return False
        ret = bisect_left(range(nums[-1]-nums[0]+1), True, key=mid_too_small)
        return ret

# heappop > check valid > merge (fail)
# 1,3,3,5 > 3,3 would pop first > 1,5 pop next > min diff 4
    # but acutally 1,3 , 3,5 is available, so 2 is min diff
# 如果可以重複使用 用 heap 應該比較快

s = Solution()
print(s.minimizeMax(nums = [10,1,2,7,1,3], p = 2))
print(s.minimizeMax(nums = [4,2,1,2], p = 1))
print(s.minimizeMax(nums = [3,4,2,3,2,1,2], p = 3))
print(s.minimizeMax(nums = [3,4,2,3,2,2,2], p = 3))
print(s.minimizeMax(nums = [3,5,2,2,2,2], p = 3))



