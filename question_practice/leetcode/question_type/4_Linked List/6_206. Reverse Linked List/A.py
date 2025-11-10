# 206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/description/

from typing import List
from math import inf

# direct change the linked list pointers
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
            # prev, curr, curr.next = curr, curr.next, prev 
                # order matters
                # assign from left to right
                # at the second curr already assigned to curr.next
                # thus curr.next assigns to the new curr

            # next_node = curr.next
            # curr.next = prev
            # prev = curr
            # curr = next_node
        return prev

# recursive solution
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        root = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return root




