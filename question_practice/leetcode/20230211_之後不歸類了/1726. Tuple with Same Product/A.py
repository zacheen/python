# 1726. Tuple with Same Product
# https://leetcode.com/problems/tuple-with-same-product/description

from typing import List
from math import inf
from collections import defaultdict, Counter

# my 
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        mem = defaultdict(int)
        ans = 0
        for i,n1 in enumerate(nums) :
            for n2 in nums[:i] :
                mul = n1*n2
                ans += mem[mul]
                mem[mul] += 1
        return ans*8

# given ans
from math import comb
from itertools import combinations
from operator import mul
from itertools import starmap, cycle
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        return 8*sum(map(comb, Counter(starmap(mul, combinations(nums, 2))).values(), cycle([2])))


s = Solution()
print("ans :",s.tupleSameProduct(nums = [2,3,4,6])) # 8
print("ans :",s.tupleSameProduct(nums = [1,2,4,5,10])) # 16



