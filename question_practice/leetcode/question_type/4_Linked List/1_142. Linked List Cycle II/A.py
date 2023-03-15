# 不能跑
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# my Runtime: 75 ms, faster than 47.47% of Python3
class Solution:
    def detectCycle(self, head):
        mem = {}
        count = 0
        while head != None :
            mem[head] = count
            count += 1
            ret = mem.get(head.next, None)
            if ret == None :
                head = head.next 
            else :
                return head.next
                
        return None

# given ans 
# 先找出有沒有 cycle (參考141. Linked List Cycle)
# 迴圈跑一次 找出 cycle 的長度
# 因為有cycle的長度 所以fast先往前移cycle的長度 
# fast 跟 slow 再一起同時往前移 一定會在 答案的點重疊
# https://www.youtube.com/watch?v=2z4EnLA46z4&t=26s
class Solution(object):
    def detectCycle(self, head):
        slow = head
        fast = head

        # 在這裡直接確認下一個點存不存在
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow

        return None

# practice again 20230309
class Solution(object):
    def detectCycle(self, head):
        quick = head
        slow = head
        while quick :
            quick = quick.next
            if quick :
                quick = quick.next
            else :
                return None

            slow = slow.next

            if quick == slow :
                slow = head
                while quick != slow :
                    quick = quick.next
                    slow = slow.next
                return slow

        return None

s = Solution()
print(s.detectCycle())

