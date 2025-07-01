# 2040. Kth Smallest Product of Two Sorted Arrays
# https://leetcode.com/problems/kth-smallest-product-of-two-sorted-arrays

from typing import List
from math import inf
from bisect import bisect_left, bisect_right

# my v2, using template binarySearch_adv2 : 1677ms Beats85.07%
    # opt : making cou_smaller O(n+m) instead of O(nlogm)
class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n1_zi_f = bisect_left(nums1, 0)
        n1_zi_b = bisect_right(nums1, 0)
        neg_n1 = nums1[:n1_zi_f]
        rev_neg_n1 = neg_n1[::-1]
        n1_0_cou = n1_zi_b - n1_zi_f
        pos_n1 = nums1[n1_zi_b:]
        rev_pos_n1 = pos_n1[::-1]

        n2_zi_f = bisect_left(nums2, 0)
        n2_zi_b = bisect_right(nums2, 0)
        neg_n2 = nums2[:n2_zi_f]
        n2_0_cou = n2_zi_b - n2_zi_f
        pos_n2 = nums2[n2_zi_b:]

        sma_0_cou = \
            (len(neg_n1)+n1_0_cou)*(len(pos_n2)+n2_0_cou) \
            + (len(neg_n2)+n2_0_cou)*(len(pos_n1)+n1_0_cou) \
            - n1_0_cou*n2_0_cou
        
        def cal_comb(list1, list2, mid):
            p = 0
            cou = 0
            for n1 in list1 :
                while p < len(list2) and list2[p]*n1 > mid :
                    p += 1
                cou += len(list2) - p
            return cou
        
        def cou_smaller(mid): # include mid
            if mid == 0 :
                return sma_0_cou
            elif mid > 0 :
                cou = sma_0_cou
                cou += cal_comb(pos_n2, rev_pos_n1, mid)
                cou += cal_comb(rev_neg_n1, neg_n2, mid)
                return cou
            else :
                cou = cal_comb(neg_n2, pos_n1, mid)
                cou += cal_comb(neg_n1, pos_n2, mid)
                return cou

        def binarySearch_adv2():
            left, right = -10**10, 10**10 # right 通常會超出界線(因為執行的時候不會執行到這個數字) # 但是最後 l 有可能會超出範圍
            while left < right:
                mid = (left + right) // 2
                if cou_smaller(mid) < k : # 條件 (如果 == target 的情況 要是 False)
                    # 沒通過 或 數字應該要往大的方向跑(目標沒有在 left 跟 mid 之間)
                    left = mid + 1 # 需注意 left 不會停留在 mid !
                else:
                    # 通過(包含 == target 的情況)
                    right = mid
            return left
        return binarySearch_adv2()

# my 3482ms Beats28.86%
class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        if len(nums1) > len(nums2) :
            nums1, nums2 = nums2, nums1
        
        len_n2 = len(nums2)
        def cou_smaller(mid): # include mid
            ret = 0
            for n1 in nums1 :
                if n1 == 0 :
                    if mid >= 0 :
                        ret += len_n2
                    if ret >= k :
                        return False
                    continue
                tar_n2 = mid / n1
                if n1 < 0 :
                    ret_i = bisect_left(nums2, tar_n2)
                    ret += (len_n2-ret_i)
                else : # n1 是正的，所以愈乘愈大
                    ret_i = bisect_right(nums2, tar_n2)
                    ret += ret_i
                if ret >= k :
                    return False
            return ret < k

        def binarySearch_adv2():
            left, right = -10**10, 10**10 # right 通常會超出界線(因為執行的時候不會執行到這個數字) # 但是最後 l 有可能會超出範圍
            while left < right:
                mid = (left + right) // 2
                if cou_smaller(mid) : # 條件 (如果 == target 的情況 要是 False)
                    # 沒通過 或 數字應該要往大的方向跑(目標沒有在 left 跟 mid 之間)
                    left = mid + 1 # 需注意 left 不會停留在 mid !
                else:
                    # 通過(包含 == target 的情況)
                    right = mid 
            return left
        
        return binarySearch_adv2()

s = Solution()
print("ans :",s.kthSmallestProduct(nums1 = [2,5], nums2 = [3,4], k = 2)) # 8
print("ans :",s.kthSmallestProduct(nums1 = [-4,-2,0,3], nums2 = [2,4], k = 6)) # 0
print("ans :",s.kthSmallestProduct(nums1 = [-2,-1,0,1,2], nums2 = [-3,-1,2,4,5], k = 3)) # -6
print("ans :",s.kthSmallestProduct(nums1 = [-9,-9,-8,-6,-1,0,5,8,10,10], nums2 = [0,4,9], k = 19)) # 0



