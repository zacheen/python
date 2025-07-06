# 3489. Zero Array Transformation IV
# https://leetcode.com/problems/zero-array-transformation-iv

from typing import List
from math import inf

# my using template knapsack_01_reach : 73ms Beats66.11%
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        finish_i = set(i for i, n in enumerate(nums) if n == 0)
        if len(finish_i) == len(nums) :
            return 0
        
        can_comb_set = [{0} for _ in range(len(nums))]  # 裡面紀錄目前可以的組合
        for ans, (l, r, val) in enumerate(queries):
            for i in range(l, r+1) :
                if i in finish_i : continue
                can_comb_set[i] |= set( new_s for s in can_comb_set[i] if (new_s := s+val) <= nums[i] )
                if nums[i] in can_comb_set[i] :
                    finish_i.add(i)
                    if len(finish_i) == len(nums) :
                        return ans+1
        return -1
    
# inspire by given ans, opt : 一條一條做 做完看所需query最大值
    # 22ms Beats76.75%
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        max_q = -1
        for i, num in enumerate(nums) :
            if num == 0 :
                continue
            can_comb_set = {0} # 裡面紀錄目前可以的組合
            for ans, (l, r, val) in enumerate(queries):
                if l <= i <= r :
                    can_comb_set |= set( new_s for s in can_comb_set if (new_s := s+val) <= num )
                    if num in can_comb_set :
                        max_q = max(max_q, ans)
                        break
            else :
                return -1
        return max_q+1

s = Solution()
print("ans :",s.minZeroArray(nums = [2,0,2], queries = [[0,2,1],[0,2,1],[1,1,3]])) # 2
print("ans :",s.minZeroArray(nums = [4,3,2,1], queries = [[1,3,2],[0,2,1]])) # -1
print("ans :",s.minZeroArray(nums = [1,2,3,2,1], queries = [[0,1,1],[1,2,1],[2,3,2],[3,4,1],[4,4,1]])) # 4
print("ans :",s.minZeroArray(nums = [0], queries = [[0,0,1]])) # 0



