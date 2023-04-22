from typing import List
import functools

# # my Beats 93.22%
# class Solution:
#     def findPrefixScore(self, nums: List[int]) -> List[int]:
#         ans = [0]
#         previous_max = nums[0]
#         for n in nums :
#             this_ans = n
#             previous_max = max(previous_max, n)
#             this_ans += previous_max
#             this_ans += ans[-1]
#             ans.append(this_ans)
#         return ans[1:]
    
class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        ans = [0]
        previous_max = nums[0]
        for n in nums :
            previous_max = max(previous_max, n)
            ans.append(n + previous_max + ans[-1])
        return ans[1:]

# given ans
# 其實就是把我的 this_ans 合併了
class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        ans = [2 * nums[0]]
        mx = nums[0]
        
        for num in nums[1:]:
            mx = max(mx, num)
            ans.append(ans[-1] + mx + num)
        
        return ans
    
s = Solution()
print(s.findPrefixScore([2,3,7,5,10]))
print(s.findPrefixScore([1,1,2,4,8,16]))



