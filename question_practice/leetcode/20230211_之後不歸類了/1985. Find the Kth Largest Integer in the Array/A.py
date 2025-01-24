class Solution:
    def kthLargestNumber(self, nums, k):
        # [int(x) for i in nums]
        nums.sort(reverse = True, key = int)
        print(nums)
        return nums[k-1]
        
s = Solution()
print(s.kthLargestNumber(["2","21","12","1"], 3))