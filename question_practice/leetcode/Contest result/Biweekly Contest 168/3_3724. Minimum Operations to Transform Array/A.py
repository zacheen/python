# 3724. Minimum Operations to Transform Array
# https://leetcode.com/problems/minimum-operations-to-transform-array/

from typing import List
from math import inf
from bisect import bisect_right

# my v2 : 52ms Beats95.27%
    # remove certain function to just fit this question
class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        ret = 0
        min_diff = inf
        last_num2 = nums2[-1]
        for n1, n2 in zip(nums1, nums2) :
            ret += abs(n1-n2)
            if min_diff != 0 :
                if n1 > n2 :
                    n1,n2 = n2,n1
                if n1 <= last_num2 <= n2 :
                    min_diff = 0
                else :
                    min_diff = min( min_diff, abs(last_num2-n1), abs(last_num2-n2) )
        # print(ret, min_diff)
        return ret + min_diff +1 # +1 for append

# my v1 : 587ms Beats5.08%
    # this version works with multiple append with in nlogn
class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        interval = []
        ret = 0
        for n1, n2 in zip(nums1, nums2) :
            if n1 >= n2 :
                ret += n1-n2
                interval.append((n2,1))
                interval.append((n1+1, -1))
            else :
                ret += n2-n1
                interval.append((n1,1))
                interval.append((n2+1, -1))
        interval.sort()

        merge_interval = [(-inf,-inf)]
        acc = 0
        st = None
        for r, inc in interval :
            if st == None :
                st = r
            acc += inc
            if acc == 0 :
                merge_interval.append((st, r-1))
                st = None
        merge_interval.append((inf,inf))
        # print(merge_interval)

        for n in nums2[len(nums1):] :
            ret_i = bisect_right(merge_interval, (n,0))-1
            _, left_int_en = merge_interval[ret_i]
            if n <= left_int_en :
                # no additional operation needed
                continue
            else :
                ret += min(n-left_int_en, merge_interval[ret_i+1][0]-n)

        return ret + (len(nums2)-len(nums1))
            

s = Solution()
print("ans :",s.minOperations(nums1 = [2,8], nums2 = [1,7,3])) # 
print("ans :",s.minOperations(nums1 = [1,3,6], nums2 = [2,4,5,3])) # 
print("ans :",s.minOperations(nums1 = [2], nums2 = [3,4])) # 

