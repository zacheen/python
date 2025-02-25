# 315. Count of Smaller Numbers After Self
# https://leetcode.com/problems/count-of-smaller-numbers-after-self/description

from typing import List
import functools

# my (segTree) 1399ms Beats45.05%
from collections import deque
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        class SegTree:
            def __init__(self, nums):
                self.n = len(nums)
                self.tree = [0] * 2 * self.n

            def update(self, index):
                index += self.n
                self.tree[index] += 1
                while index > 1:
                    # update node
                    self.tree[index>>1] = self.tree[index] + self.tree[index^1]
                    index >>= 1

            def query(self, right):
                # include
                left = self.n
                right += self.n-1
                res = 0
                while left <= right:
                    if left & 1 :
                        # combine result
                        res += self.tree[left]
                        left += 1
                    if not (right & 1) :
                        # combine result
                        res += self.tree[right]
                        right -= 1
                    left >>= 1
                    right>>= 1
                return res 
        
        dense_n = list(set(nums))
        dense_n.sort()
        n_indx = { n:i for i,n in enumerate(dense_n) }
        segTree = SegTree(dense_n)
        
        ans_list = deque()
        for n in nums[::-1] :
            n = n_indx[n]
            ans_list.appendleft(segTree.query(n))
            segTree.update(n)
        return list(ans_list)
    
s = Solution()
print("ans :",s.countSmaller(nums = [5,2,6,1])) # [2,1,1,0]
print("ans :",s.countSmaller(nums = [-1])) # [0]
print("ans :",s.countSmaller(nums = [-1,-1])) # [0,0]



