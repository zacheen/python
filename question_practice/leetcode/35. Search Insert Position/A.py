# My Runtime: 52 ms, faster than 83.76% of Python3
class Solution:
    def searchInsert(self, nums, target):
        def binary_search (l,r) :
            print(l,r)
            if l == r :
                if target > nums[-1] :
                    return len(nums)
                else:
                    return l
            
            mid = (l+r)// 2
            
            if nums[mid] > target :
                return binary_search(l,mid)
            elif nums[mid] < target :
                return binary_search(mid+1,r)
            else :
                return mid
            
        return binary_search(0, len(nums)-1)

s = Solution()
# print(s.searchInsert([1,3,5,7],6))
print(s.searchInsert([1],1))