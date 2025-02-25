# 1980. Find Unique Binary String
# https://leetcode.com/problems/find-unique-binary-string

from typing import List
from math import inf

# my 0ms
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        len_n = len(nums[0])
        nums = set(nums)
        ans = ""
        def dfs(s) : # at most try 16 paths, since at most 16 items
            nonlocal ans
            # print(s)
            if len(s) == len_n :
                if s not in nums :
                    ans = s[:]
                    return True
                return False
            for next_n in ['0', '1'] :
                s += next_n
                if dfs(s) :
                    return True
                s = s[:-1]
            return False
        dfs("")
        return ans

# given ans (Heuristic)
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        return ''.join('1' if num[i] == '0' else '0' for i, num in enumerate(nums))

s = Solution()
print("ans :",s.findDifferentBinaryString(["01","10"])) # "00" or "11"



