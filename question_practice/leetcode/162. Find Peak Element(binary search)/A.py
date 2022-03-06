class Solution:
    # given ans (binary search)
    def findPeakElement(self, nums):
        def search (nums, l, r):
            if l == r :
                return l
            mid = (l+r)//2
            if nums[mid] > nums[mid+1] :   
                return search(nums, l, mid)
            else :
                return search(nums, mid+1, r)

        return search(nums, 0, len(nums)-1)
        # My 方法1 太慢
        # for i in range(len(nums)-1) :
        #     if nums[i] > nums[i+1] :
        #         return i
            
        # return len(nums)-1

s = Solution()
print(s.findPeakElement([1,10,3,4,5]))