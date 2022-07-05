# my 
# class Solution:
#     def intersect(self, nums1, nums2):
#         c = Counter(nums2)
#         ans = []
#         for n in nums1 :
#             if c[n] > 0 :
#                 ans.append(n)
#                 c[n] -= 1
#         return ans

# given ans
class Solution:
    def intersect(self, nums1, nums2):
        # given ans 多這裡
        # 讓比較複雜的部份每次都做比較少次 (O)
        # 雖然這裡速度沒有差很多 但是觀念很好
        if len(nums1) < len(nums2) :
            return intersect(nums2, nums1)
        
        c = Counter(nums2)
        ans = []
        for n in nums1 :
            if c[n] > 0 :
                ans.append(n)
                c[n] -= 1
        return ans

s = Solution()
print(s.())



