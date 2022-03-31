# My Runtime: 1109 ms, faster than 43.20% of Python3
class Solution:
    def isPalindrome(self, head: Optional[ListNode]):
        stack = []
        fast = head
        slow = head
        while fast and fast.next :
            stack.append(slow.val)
            fast = fast.next.next
            slow = slow.next
            
        # print(stack)
        if fast :
            slow = slow.next
        
        while slow :
            if stack.pop() != slow.val :
                return False
            slow = slow.next
        return True

# given ans 
# 後面比較是否相同實作的方法不一樣
# 這裡是直接 reverse 中間點之後的 link List 
# 再各自從頭比較
# 好處是不會再增加空間
class Solution:
    def isPalindrome(self, head):
        def reverseList(head):
            prev = None
            curr = head

            while curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next

            return prev

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        if fast:
            slow = slow.next
        slow = reverseList(slow)

        while slow:
            if slow.val != head.val:
                return False
            slow = slow.next
            head = head.next

        return True

s = Solution()
print(s.())

