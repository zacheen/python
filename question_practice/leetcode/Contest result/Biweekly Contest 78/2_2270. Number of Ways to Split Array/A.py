# 2270. Number of Ways to Split Array
# https://leetcode.com/problems/number-of-ways-to-split-array/description

# my 38ms Beats98.11%
class Solution:
    def waysToSplitArray(self, nums):
        total = sum(nums)
        
        now = 0
        ans = 0
        for n in nums[:-1] :
            now += n
            # print(now, total-now)
            if now >= total-now :
                ans += 1
        return ans
        

# given ans
# 判斷 兩倍的now >= total 
# 但 * 應該比較慢

s = Solution()
print(s.waysToSplitArray())



