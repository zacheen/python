class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

CONDITION = True

# add filter node
dummy_head = ListNode()
now_end = dummy_head
while head :
    if CONDITION :
        now_end.next = head
        now_end = head # now_end = now_end.next
    head = head.next
now_end.next = None
return dummy_head.next