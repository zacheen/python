# 不能跑的
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# My Runtime: 66 ms, faster than 71.02% of Python3 
# class Solution:
#     def hasCycle(self, head: Optional[ListNode]):
#         mem = {}
#         while head != None :
#             mem[head] = True
#             ret = mem.get(head.next, None)
#             if ret == None :
#                 head = head.next 
#             else :
#                 return True
                
#         return False

# given ans Runtime: 56 ms, faster than 90.55% of Python3
# 邏輯是 如果真的有迴圈， fast 會在回圈內以"每次一格"的速度追上 slow
# 因為 "每次一格" 所以一定會相遇
class Solution:
    def hasCycle(self, head):
        fast, slow = head, head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
            if fast == slow:
                return True
        return False
    
# practice again 20230309
class Solution(object):
    def hasCycle(self, head):
        quick = head
        slow = head
        while True :
            if quick :
                quick = quick.next
            else :
                return False
            if quick :
                quick = quick.next
            else :
                return False

            slow = slow.next
            
            if quick == slow :
                return True
            
s = Solution()
print(s.hasCycle())

