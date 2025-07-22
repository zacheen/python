# 3618. Split Array by Prime Indices
# https://leetcode.com/problems/split-array-by-prime-indices/description/

from typing import List
from math import inf

# my 52ms
MAX = 100001
prime = [True]*MAX
prime[0] = False
prime[1] = False
for i in range(2, int(MAX**(1/2)+1)):
    if not prime[i]:
        continue
    for j in range(i*i, MAX, i):
        prime[j] = False

class Solution:
    def splitArray(self, nums: List[int]) -> int:
        diff = 0
        for i, n in enumerate(nums):
            if prime[i] :
                diff += n
            else :
                diff -= n
        return abs(diff)

s = Solution()
print("ans :",s.splitArray([2,3,4])) # 1
print("ans :",s.splitArray([-1,5,7,0])) # 3

