# my Beats 94.44%
class Solution(object):
    def missingNumber(self, nums):
        usual_num_len = len(nums) # +1 # 不應該加一 因為某一個項目是0
        usual_sum = ((usual_num_len)*(usual_num_len+1))/2
        now_sum = sum(nums)
        return usual_sum-now_sum

# given ans # Beats 99.69%
class Solution:
    def missingNumber(self, nums):
        ans = len(nums)
        for i, num in enumerate(nums):
            ans ^= i ^ num
        return ans
s = Solution()
print(s.missingNumber([0,1]))


