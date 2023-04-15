from typing import List
import functools

# my 
class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        ans = [0]
        previous_max = nums[0]
        for n in nums :
            this_ans = n
            previous_max = max(previous_max, n)
            this_ans += previous_max
            this_ans += ans[-1]
            ans.append(this_ans)
        return ans[1:]

# given ans

s = Solution()
print(s.findPrefixScore([2,3,7,5,10]))
print(s.findPrefixScore([1,1,2,4,8,16]))



