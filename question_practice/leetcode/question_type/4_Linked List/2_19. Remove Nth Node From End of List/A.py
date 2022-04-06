# my Runtime: 41 ms, faster than 67.65% of Python3
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int):
        dummy = ListNode(0, head)
        
        fast = dummy
        for i in range(n) : 
            fast = fast.next
            
        slow = dummy
        while fast.next != None :
            fast = fast.next
            slow = slow.next
        
        # 刪除點
        slow.next = slow.next.next
        
        return dummy.next

# 跟 given ans 一樣 只是優化 if X != None : 成 if X :

s = Solution()
print(s.())

