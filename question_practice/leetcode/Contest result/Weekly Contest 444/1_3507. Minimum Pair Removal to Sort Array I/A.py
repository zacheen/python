# 3507. Minimum Pair Removal to Sort Array I
# https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i

from typing import List
from math import inf

# my 11ms Beats84.21%
class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        def dfs(now_i, prev_n, now_s):
            if now_i == len(nums) :
                if now_s >= prev_n :
                    return 0, [now_s]
                else :
                    return inf, [now_s]

            # merge here
            ret, p = dfs(now_i+1, prev_n, now_s+nums[now_i])
            ret += 1 # merge cost
            
            # seperate here
            if now_s >= prev_n :
                ret2, p2 = dfs(now_i+1, now_s, nums[now_i])
                if ret2 < ret :
                    ret, p = ret2, p2
                    p.append(prev_n)

            return ret, p
        return dfs(1, -inf, nums[0])

s = Solution()
# print("ans :",s.minimumPairRemoval([-1])) # 
print("ans :",s.minimumPairRemoval([2,2,-1,3,-2,2,1,1,1,0,-1])) # 



