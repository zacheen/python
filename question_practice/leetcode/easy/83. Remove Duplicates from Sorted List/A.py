# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 無法跑的
# My
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None :
            return None
        
        start = head
        while head.next != None :
            if head.val == head.next.val :
                head.next = head.next.next
            else :
                head = head.next
        return start

# s = Solution()
# print(s.())