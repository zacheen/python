# my using template
from bisect import bisect_left
class Solution:
    def maximumCandies(self, candies, k: int) -> int:
        def mid_too_big(mid):
            if mid == 0 : return False
            return sum(n//mid for n in candies) < k
        return bisect_left(range(max(candies)+1), True, key=mid_too_big)-1

s = Solution()
print("ans:",s.maximumCandies(candies = [5,8,6], k = 3)) # 5
print("ans:",s.maximumCandies(candies = [2,5], k = 11)) # 0
print("ans:",s.maximumCandies(candies = [4,7,5], k = 16)) # 1
print("ans:",s.maximumCandies([4,7,6],3)) # 5


