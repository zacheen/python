# 3287. Find the Maximum Sequence Value of Array
# https://leetcode.com/problems/find-the-maximum-sequence-value-of-array

from typing import List
from math import inf

# my 944ms Beats97.50%
class Solution:
    def maxValue(self, nums: List[int], k: int) -> int:
        # 注意! 並不是挑k個出來之後 再挑k個
        # 而是選 2*k個 再拆成兩半
            # 所以其實可以想成前半段 跟 後半段
        
        # front half
        mem_front = [{0}] + [set() for _ in range(k)] # mem_front[i] : 挑了i個項目之後，所有可能組合
        mem_i_poss = []
        for i, num in enumerate(nums[:-k], 1):
            for fut_i in range(min(k, i),0,-1):
                mem_front[fut_i] |= set( s|num for s in mem_front[fut_i-1] )
            if i >= k :
                mem_i_poss.append(mem_front[-1].copy())

        ans = 0
        mem_front = [{0}] + [set() for _ in range(k)]
        seen_poss_b = set() # optimize, since each "mem_i_poss.pop()" poss_f would be lesser and lesser
        for i, num in enumerate(nums[:k-1:-1], 1):
            for fut_i in range(min(k, i),0,-1):
                mem_front[fut_i] |= set( s|num for s in mem_front[fut_i-1] )
            if i >= k :
                for poss_f in mem_i_poss.pop() :
                    for poss_b in mem_front[-1] - seen_poss_b :
                        ans = max(ans, poss_f^poss_b)
                seen_poss_b |= mem_front[-1]
        return ans
            
        
        
        
        
        

s = Solution()
print("ans :",s.maxValue(nums = [2,6,7], k = 1)) # 5
print("ans :",s.maxValue(nums = [4,2,5,6,7], k = 2)) # 2
print("ans :",s.maxValue(nums = [4,2,5,6,16], k = 2)) # 
# print("ans :",s.maxValue()) # 



