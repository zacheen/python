# 2261. K Divisible Elements Subarrays
# https://leetcode.com/problems/k-divisible-elements-subarrays/description/

from typing import List
from math import inf

# my Trie version : 89ms Beats99.26%
class Trie:
    def __init__(self):
        self.root = {}
        self.cou = 0

    def insert(self, word):
        now_n = self.root
        for c in word :
            if c not in now_n :
                now_n[c] = {}
                self.cou += 1
            now_n = now_n[c]

class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        trie = Trie()
        r = 0  
        cou = 0
        for l,l_n in enumerate(nums) :
            while r < len(nums) :
                if nums[r]%p == 0 :
                    cou += 1
                    if cou > k :
                        cou -= 1
                        break
                r+=1
            
            # cal ans
            # print(nums[l:r])
            trie.insert(nums[l:r])

            if l_n%p == 0 :
                cou -= 1
        return trie.cou

# my set version is slower : 367ms Beats43.18%
    # also might happend collision
class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        # trie = Trie()
        seen = set()
        r = 0  
        cou = 0
        for l,l_n in enumerate(nums) :
            while r < len(nums) :
                if nums[r]%p == 0 :
                    cou += 1
                    if cou > k :
                        cou -= 1
                        break
                r+=1
            
            # print(nums[l:r])
            # trie.insert(nums[l:r])
            for end_i in range(l+1, r+1):
                seen.add(tuple(nums[l:end_i]))

            if l_n%p == 0 :
                cou -= 1
        return len(seen)

s = Solution()
print("ans :",s.countDistinct(nums = [2,3,3,2,2], k = 2, p = 2)) # 11
# print("ans :",s.countDistinct(nums = [1,2,3,4], k = 4, p = 1)) # 10
# print("ans :",s.countDistinct()) # 



