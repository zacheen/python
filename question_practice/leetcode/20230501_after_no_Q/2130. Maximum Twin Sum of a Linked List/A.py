# 2130. Maximum Twin Sum of a Linked List
# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/

from typing import List
import functools

# # my v1 Beats 47.12%
# class Solution:
#     def pairSum(self, head: Optional[ListNode]) -> int:
#         mem_list = []

#         fast = head
#         slow = head
#         while fast :
#             mem_list.append(slow.val)
#             slow = slow.next
#             fast = fast.next.next

#         max_ans = 0
#         while slow :
#             max_ans = max(max_ans, mem_list.pop() + slow.val)
#             slow = slow.next

#         return max_ans

# my v2 Beats 68.22%
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        mem_list = []

        fast = head
        slow = head
        while fast :
            mem_list.append(slow.val)
            slow = slow.next
            fast = fast.next.next

        max_ans = 0
        # 其實只要取值就好 不需要再修改 list
        for twin_item in reversed(mem_list) :
            max_ans = max(max_ans, twin_item + slow.val)
            slow = slow.next

        return max_ans

# given ans Beats 84.89%
# 竟然比我的還要快
    # 明明感覺做了很多判斷
    # 看來 List 的 append 所花的時間比 四次給值(reverse)的時間長
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        def reverseList(head: ListNode) -> ListNode:
            prev = None
            while head:
                # next = head.next
                # head.next = prev
                # prev = head
                # head = next
                # 我優化成
                prev, head.next, head = head, prev, head.next
                # head, head.next, prev = head.next, prev, head # 這種方式是不行的
                    # 所以看來給值還是有順序性 而且是從前面開始給
            return prev

        ans = 0
        slow = head
        fast = head

        # Let slow point to the start of the second half
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Tail points to the end with reversed second half
        tail = reverseList(slow)

        while tail:
            ans = max(ans, head.val + tail.val)
            head = head.next
            tail = tail.next

        return ans
  
s = Solution()
print(s.pairSum())



