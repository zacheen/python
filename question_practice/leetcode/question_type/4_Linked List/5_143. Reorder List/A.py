# my Time Limit Exceeded
class Solution:
    def reorderList(self, head: Optional[ListNode]):
        """
        Do not return anything, modify head in-place instead.
        """
        def reverseList(head):
            prev = None
            curr = head

            while curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next

            return prev
        
        save_head = head
        cur = head.next
        pre = head
        while cur :
            rev = reverseList(cur)
            pre.next = rev
            pre = pre.next
            cur = pre.next

# my 看觀念自己實作
# Runtime: 121 ms, faster than 55.59% of Python3
class Solution:
    def reorderList(self, head: Optional[ListNode]):
        """
        Do not return anything, modify head in-place instead.
        """
        # corner case
        if not head or not head.next or not head.next.next :
            return head
        
        def reverseList(head):
            prev = None
            curr = head

            while curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next

            return prev
        
        fast = head
        slow = head
        prev_slow = None
        while fast and fast.next :
            fast = fast.next.next
            prev_slow = slow
            slow = slow.next
        
        # 截斷
        prev_slow.next = None
        back_rev = reverseList(slow)
        
        save_head = head
        while True :
            if head.next == None :
                head.next = back_rev
                break

            nexthead, nextrev = head.next, back_rev.next
            head.next, back_rev.next = back_rev,head.next
            head, back_rev = nexthead, nextrev

# given ans
# 差在 這裡的 合併(def merge) 做的比較優雅
# 我是一次建立兩個連結
# 他是一次建立一個連結 建立完後 l1 與 l2 的腳色互換
class Solution:
    def reorderList(self, head: ListNode):
        def findMid(head: ListNode):
            prev = None
            slow = head
            fast = head

            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            prev.next = None

            return slow

        def reverse(head: ListNode):
            prev = None
            curr = head

            while curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next

            return prev

        def merge(l1: ListNode, l2: ListNode):
            # l1 是 current  要把 l2 的第一個點接到後面
            while l2:
                next = l1.next
                l1.next = l2
                l1 = l2
                l2 = next

        if not head or not head.next:
            return

    mid = findMid(head)
    reversed = reverse(mid)
    merge(head, reversed)

s = Solution()
print(s.())

