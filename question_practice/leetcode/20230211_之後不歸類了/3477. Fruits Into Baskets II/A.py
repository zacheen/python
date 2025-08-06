# 3477. Fruits Into Baskets II
# https://leetcode.com/problems/fruits-into-baskets-ii
    # same as, but smaller testcase
    # 3479. Fruits Into Baskets III
    # https://leetcode.com/problems/fruits-into-baskets-iii

from typing import List
from math import inf

# my 9ms Beats96.22%
class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        for f in fruits :
            for i, cap in enumerate(baskets) :
                if cap >= f :
                    baskets.pop(i)
                    break
        return len(baskets)

s = Solution()
print("ans :",s.numOfUnplacedFruits(fruits = [4,2,5], baskets = [3,5,4])) # 1
print("ans :",s.numOfUnplacedFruits(fruits = [4,2,5,5], baskets = [3,5,4,5])) # 1
print("ans :",s.numOfUnplacedFruits(fruits = [3,6,1], baskets = [6,4,7])) # 0
# print("ans :",s.numOfUnplacedFruits()) # 



