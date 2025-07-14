# 1290. Convert Binary Number in a Linked List to Integer
# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer

from typing import List
from math import inf

# my : 0ms
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        ans = 0
        while head :
            ans = (ans<<1) + head.val
            head = head.next
        return ans
