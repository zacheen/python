from typing import List
import functools

# my Beats 75.91%
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        prev_max_candies = max(candies)
        return [cand + extraCandies >= prev_max_candies for cand in candies]

s = Solution()
print(s.kidsWithCandies(candies = [2,3,5,1,3], extraCandies = 3))
print(s.kidsWithCandies(candies = [4,2,1,1,2], extraCandies = 1))



