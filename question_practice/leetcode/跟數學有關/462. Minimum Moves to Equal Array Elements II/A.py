# My Runtime: 68 ms, faster than 99.32% of Python3
class Solution:
    def minMoves2(self, nums):
        # 找中位數
        median = int(statistics.median(nums))
        return sum(abs(i-median) for i in nums)

s = Solution()
print(s.minMoves2([1,2,3]))

