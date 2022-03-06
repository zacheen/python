class Solution:
    def removeDuplicates(self, nums):
        if not nums: return 0
        i, j = 0, 1
        while j < len(nums):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
            j += 1
        return i + 1

# My
# class Solution:
#     def removeDuplicates(self, nums):
#         his = {}
#         removeIdx = []
        
#         numListLen = len(nums)
#         for idx, val in enumerate(nums) :
#             # print(idx, val)
#             gethis = his.get(val, None)
#             if gethis == None :
#                 his[val] = True
#             elif gethis :
#                 removeIdx.append(idx)  

#         count = len(removeIdx)-1
#         while count >= 0:
#             del nums[removeIdx[count]]
#             count = count -1
            
#         return numListLen-count

s = Solution()
print(s.removeDuplicates([1,2,1]))