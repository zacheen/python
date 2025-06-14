# 3388. Count Beautiful Splits in an Array
# https://leetcode.com/problems/count-beautiful-splits-in-an-array/description/

from typing import List
import functools

# # my : Time Limit Exceeded
#     # calculate z : O(n^2) : 2.5*10^7
# class Solution:
#     def beautifulSplits(self, nums: List[int]) -> int:
#         len_num = len(nums)
#         z = [[0]*len_num for _ in range(len_num)]
#         for n1, this_z in enumerate(z):
#             z_box_l = z_box_r = n1
#             for n2 in range(n1+1, len_num):
#                 same_len = 0
#                 if n2 <= z_box_r :
#                     same_len = min(z_box_r-n2+1, this_z[n2-z_box_l])
#                 while n2 + same_len < len_num and nums[n1+same_len] == nums[n2+same_len]:
#                     # 這裡順序不能錯
#                     z_box_l = n2
#                     z_box_r = n2 + same_len
#                     same_len += 1
#                 this_z[n2] = same_len
#         # print(z)
        
#         total_l = len_num
#         # nums1 is nums2 prefix
#         ans = 0
#         for i in range(1, total_l):
#             n2_e = i*2
#             if n2_e >= total_l :
#                 break
#             if z[0][i]>=i :
#                 # print("1:", nums[:i], nums[i:i*2], total_l-i*2)
#                 ans += total_l-n2_e
#         # print("1T :", ans)

#         # nums2 is nums3 prefix
#         for n2_s in range(1, total_l) :
#             for n2_e in range(n2_s+1,total_l) :
#                 n3_e = n2_e+(n2_e-n2_s)
#                 if n3_e > total_l :
#                     break
#                 # print("2 :",nums[:n2_s], nums[n2_s:n2_e], nums[n2_e:])
#                 if z[n2_s][n2_e] >= (n2_e-n2_s) :
#                     if ((n2_s*2) > n2_e) or z[0][n2_s] < n2_s :
#                         # print("add 1")
#                         ans += 1
#         return ans

# given ans 1
# similar to my concept, but optimized : 7633ms Beats58.46%
    # using my template to speed up
def lcp(arr) :
    len_arr = len(arr)
    z = [0]*len_arr
    z_box_l = z_box_r = 0
    for i in range(1, len_arr):
        same_len = 0
        if i <= z_box_r :
            same_len = min(z_box_r-i+1, z[i-z_box_l])
                # z_box_r-i+1  : 如果 i~z_box_r 全部都一樣，長度會是多少
                # z[i-z_box_l] :  為了排除情況 "aabab"
            # if same_len > 0 : print("fast forward") # 應該要大於1 才會 fast forward
        while i + same_len < len_arr and arr[same_len] == arr[i+same_len]:
            # 這裡順序不能錯
            z_box_l = i
            z_box_r = i + same_len
            same_len += 1
        z[i] = same_len
    return z

class Solution:
    def beautifulSplits(self, nums: List[int]) -> int:
        size = len(nums)
        if size < 3:
            return 0

        ans = 0
        z1 = lcp(nums)
        for i in range(1, size):
            if z1[i] >= i:
                ans += size - 2 * i
                maxSize = 2 * i
            else:
                maxSize = size
            z2 = lcp(nums[i:])
            for j in range(i + 1, maxSize):
                if z2[j - i] >= j - i:
                    ans += 1
        return ans

# given ans 2 : 4173ms Beats86.79%
class Solution:
    def beautifulSplits(self, nums: List[int]) -> int:
        len_num = len_num
        mem = [[0]*(len_num+1) for _ in range(len_num+1)]

        for i in range(len_num-1, -1, -1) :
            for j in range(len_num-1, i-1, -1) :
                if nums[i] == nums[j] :
                    mem[i][j] = 1 + mem[i + 1][j + 1]

        ans = 0
        for cut_i1 in range(1, len_num-1):
            for cut_i2 in range(cut_i1+1, len_num):
                len1 = cut_i1
                len2 = cut_i2 - cut_i1
                len3 = len_num - cut_i2
                if (len1 <= len2 and mem[0][cut_i1] >= len1) or (len2 <= len3 and mem[cut_i1][cut_i2] >= len2) :
                    ans += 1
        return ans



s = Solution()
print("ans :",s.beautifulSplits([1,1,2,1])) # 2
print("ans :",s.beautifulSplits([1,2,3,4])) # 0
print("ans :",s.beautifulSplits([2,2,0,0,0,0,1,2,2,0,0,1,0])) # 17
print("ans :",s.beautifulSplits([3,3,3,1,3])) # 3



