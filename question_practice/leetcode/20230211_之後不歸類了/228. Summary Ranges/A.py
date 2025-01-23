class Solution:
    def summaryRanges(self, nums):
        ans = []
        if len(nums) == 0 :
            return []
        
        left = nums[0]
        mem = nums[0]
        # need_reset = False
        count = 1
        while count < len(nums) :
        # for count in range(1,len(nums)) :
            if nums[count] != mem+1 :
                if mem == left :
                    ans.append(str(left))
                else :
                    ans.append(str(left)+"->"+str(mem))
                # reset
                left = nums[count]
            
            mem = nums[count]
            count = count + 1
                
        if mem == left :
            ans.append(str(left))
        else :
            ans.append(str(left)+"->"+str(mem))
        
        return ans

s = Solution()
print(s.summaryRanges([0,2,3,4,6,8,9]))