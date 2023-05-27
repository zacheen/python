# 24. Swap Nodes in Pairs
# https://leetcode.com/problems/swap-nodes-in-pairs/description/

from typing import List
import functools

# my Beats 67.6%
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mem_head = head

        while head and head.next :
            last_node = head
            head = head.next
            last_node.val, head.val = head.val, last_node.val

            head = head.next

        return mem_head

# given ans
# 直接交換 node 的順序

s = Solution()
print(s.swapPairs())



