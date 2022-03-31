# My Runtime: 32 ms, faster than 89.83% of Python3
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int):
        dummy = ListNode(None, head)
        l = dummy
        # 先找到 left 
        # l 的位置是 left 的前一個
        for i in range(left-1) :
            l = l.next
            
        # 在找到right
        # r 的位置是 right 的後一個
        r = l
        for i in range(right-left+2) :
            r = r.next
        # print("r:",r.val)
            
        # 中間 reverse    
        prev = r
        curr = l.next

        for i in range(right-left+1) :
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            
        l.next = prev
        
        return dummy.next

# given ans
# 還蠻神奇的想法 竟然用 Recusive 實作
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int):
        if left == 1:
            return self.reverseN(head, right)

        head.next = self.reverseBetween(head.next, left - 1, right - 1)
        return head

    def reverseN(self, head: Optional[ListNode], n: int):
        if n == 1:
            return head

        newHead = self.reverseN(head.next, n - 1)
        headNext = head.next
        head.next = headNext.next
        headNext.next = head
        return newHead

s = Solution()
print(s.())

