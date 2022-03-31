# My Runtime: 56 ms, faster than 89.68% of Python3
class Solution:
    def removeDuplicates(self, nums):
        
        ans = 0
        now_num = None
        count = 0
        for i in range(len(nums)-1, -1, -1) :
            if now_num != nums[i] :
                ans = ans + count
                count = 1
                now_num = nums[i]
            else :
                if count >= 2 :
                    del(nums[i])
                    # nums.append("_")
                count = 2
        
        ans = ans + count
        # print(ans)
        return ans

s = Solution()
print(s.removeDuplicates([0,0,1,1,1,1,2,3,3]))

