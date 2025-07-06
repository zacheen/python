# 1865. Finding Pairs With a Certain Sum
# https://leetcode.com/problems/finding-pairs-with-a-certain-sum

from typing import List
from math import inf
from collections import Counter

# my 
class FindSumPairs:
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.cnt1 = Counter(nums1)
        self.cnt2 = Counter(nums2)
        self.nums2 = nums2

    def add(self, index: int, val: int) -> None:
        old_val = self.nums2[index]
        new_val = old_val + val
        self.cnt2[old_val] -= 1
        self.cnt2[new_val] += 1
        self.nums2[index] = new_val

    def count(self, tot: int) -> int:
        # 因為 nums1.len 只有 1000，所以當然是 for 這個
        ret = 0
        for n1, c1 in self.cnt1.items():
            ret += self.cnt2[tot-n1] * c1
        return ret

