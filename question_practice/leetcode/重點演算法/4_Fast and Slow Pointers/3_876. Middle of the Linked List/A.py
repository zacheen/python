# My Runtime: 24 ms, faster than 98.82% of Python3
class Solution:
    def middleNode(self, head):
        fast = head
        slow = head
        while fast and fast.next :
            fast = fast.next.next
            slow = slow.next
        return slow

s = Solution()
print(s.())

