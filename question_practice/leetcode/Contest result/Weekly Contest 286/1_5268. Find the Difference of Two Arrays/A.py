# My 
# class Solution:
#     def findDifference(self, nums1, nums2):
#         l,r = 0,0
#         last = None
        
#         # 因為一開始我以為是排序好的兩個數列
#         # 如果沒有排序好 應該是用set比較快
#         nums1.sort()
#         nums2.sort()
        
#         ans1 = []
#         ans2 = []
        
#         while l < len(nums1) and r < len(nums2) :
#             if nums1[l] == nums2[r] :
#                 last = nums1[l]
#                 l += 1
#                 r += 1
#             elif nums1[l] > nums2[r] :
#                 if nums2[r] != last :
#                     ans2.append(nums2[r])
#                     last = nums2[r]
#                 r+=1
#             else :
#                 if nums1[l] != last :
#                     ans1.append(nums1[l])
#                     last = nums1[l]
#                 l+=1
                
#         # print(ans1, ans2)
        
#         # 這兩個 while 迴圈只會進其中一個
#         while l != len(nums1) :
#             if nums1[l] != last :
#                 ans1.append(nums1[l])
#                 last = nums1[l]
#             l+=1
            
#         while r != len(nums2) :
#             if nums2[r] != last :
#                 ans2.append(nums2[r])
#                 last = nums2[r]
#             r+=1
            
#         return [ans1, ans2]

# given ans
# 因為兩邊都已經轉成 set  所以也不用處理重複的項目
class Solution:
    def findDifference(self, nums1, nums2):
        a = set(nums1)
        b = set(nums2)
        return [[i for i in a if i not in b], [i for i in b if i not in a]]

s = Solution()
print(s.findDifference(nums1 = [1,2,3,3], nums2 = [1,1,2,2]))

