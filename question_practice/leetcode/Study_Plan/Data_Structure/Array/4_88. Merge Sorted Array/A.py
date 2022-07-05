# 注意 bound  
# 寫之前要先思考有沒有更優雅的寫法

# my v1
# Runtime: 26 ms, faster than 99.81% of Python3
# class Solution:
#     def merge(self, nums1, m, nums2, n):
#         nums1_p = m-1
#         nums2_p = n-1
        
#         for i in range(m+n-1,-1,-1) :
#             if nums1_p != -1 and (nums2_p == -1 or nums1[nums1_p] > nums2[nums2_p]) :
#                 nums1[i] = nums1[nums1_p]
#                 nums1_p -= 1
#             else :
#                 nums1[i] = nums2[nums2_p]
#                 nums2_p -= 1

# my v2 合併 given ans nums2 bound 的概念
class Solution:
    def merge(self, nums1, m, nums2, n):
        nums1_p = m-1
        nums2_p = n-1
        if nums2_p == -1 :
            return
        
        for i in range(m+n-1,-1,-1) :
            if nums1_p != -1 and nums1[nums1_p] > nums2[nums2_p] :
                nums1[i] = nums1[nums1_p]
                nums1_p -= 1
            else :
                nums1[i] = nums2[nums2_p]
                nums2_p -= 1
                if nums2_p == -1 :
                    break

# given ans
# 又更好的處理了 bound
    # 如果nums2沒了  nums1的數字就留在原地即可
# class Solution:
#     def merge(self, nums1, m, nums2, n):
#         i = m - 1      # nums1's index (actual nums)
#         j = n - 1      # nums2's index
#         k = m + n - 1  # nums1's index (next filled position)

#         while j >= 0:
#             if i >= 0 and nums1[i] > nums2[j]:
#                 nums1[k] = nums1[i]
#                 k -= 1
#                 i -= 1
#             else:
#                 nums1[k] = nums2[j]
#                 k -= 1
#                 j -= 1

s = Solution()
print(s.merge())



