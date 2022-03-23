# https://walkccc.me/LeetCode/problems/0453/


class Solution:
    def minMoves(self, nums):
        mini = min(nums)
        return sum(num - mini for num in nums)

s = Solution()
print(s.minMoves([3,4,4]))

