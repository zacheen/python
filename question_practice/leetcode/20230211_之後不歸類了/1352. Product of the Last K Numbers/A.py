# 1352. Product of the Last K Numbers
# https://leetcode.com/problems/product-of-the-last-k-numbers/description
    # The test cases are generated so that, at any time, the product of any contiguous sequence of numbers will fit into a single 32-bit integer without overflowing.

from typing import List
from math import inf

# my 15ms Beats98.93%
class ProductOfNumbers:
    def __init__(self):
        self.stack = []
        self.now_pro = 1

    def add(self, num: int) -> None:
        if num == 0:
            self.now_pro = 1
            self.stack = []
        else:
            self.stack.append(self.now_pro)
            self.now_pro *= num

    def getProduct(self, k: int) -> int:
        if len(self.stack) < k :
            return 0
        return self.now_pro // self.stack[-k]
