# 525. Contiguous Array
# https://leetcode.com/problems/contiguous-array/description/

from typing import List

# my : 79ms Beats95.02%
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        cnt0 = 0
        cnt1 = 0
        diff_mem = {}
        diff_mem[0] = -1
        max_len = 0
        for i, n in enumerate(nums) :
            if n & 1 :
                cnt1 += 1
            else :
                cnt0 += 1
            
            now_diff = cnt0 - cnt1
            # print(i, now_diff, diff_mem)
            if now_diff in diff_mem :
                new_len = i-diff_mem[now_diff]
                if new_len > max_len :
                    max_len = new_len
            else :
                diff_mem[now_diff] = i

        return max_len

s = Solution()
print(s.findMaxLength([0,1]))
print(s.findMaxLength([0,1,0]))
print(s.findMaxLength([0,1,1,1,1,1,0,0,0]))



