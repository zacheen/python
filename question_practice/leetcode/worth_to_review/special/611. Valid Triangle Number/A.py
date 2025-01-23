# 611. Valid Triangle Number
# https://leetcode.com/problems/valid-triangle-number/

# my practice again : 2282ms Beats12.27%
# using sliding window is still faster
from bisect import bisect_right
class Solution:
    def triangleNumber(self, nums):
        nums.sort()
        ans_cou = 0
        for r, r_n in enumerate(nums) :
            for l, l_n in enumerate(nums[:r]) :
                ans_cou += max(0, l - bisect_right(nums, r_n-l_n))
                # using hi is slower...
        return ans_cou

# given ans : 483ms Beats98.16%
# 我有再優化一下
class Solution:
    def triangleNumber(self, nums):
        ans = 0
        nums.sort()

        # k is the largest edge
        for k, largest_edge in enumerate(nums):
            # 使用 sliding widows
            i = 0
            j = k - 1
            while i < j:
                if nums[i] + nums[j] > largest_edge:
                    # 現在 的邊長 是 k 跟 j，i總共有幾種解答 
                    # 每次 j 不一樣的時候就增加一次解答
                    ans += j - i 
                    j -= 1
                else:
                    # 找尋適合的 i
                    # (這裡用 binary search 應該不會比較快)
                    i += 1
        return ans

s = Solution()
print(s.triangleNumber([2,2,3,4]))
# print(s.triangleNumber([4,2,3,4]))



