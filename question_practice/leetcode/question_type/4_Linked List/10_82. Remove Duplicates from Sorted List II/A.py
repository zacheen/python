# 82. Remove Duplicates from Sorted List II
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/

# my Runtime: 59 ms, faster than 51.24% of Python3
# 不能跑
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def deleteDuplicates(self, head: Optional[ListNode]):
#         start_head = head
#         last_next = None  # 存放上一個存活的數字的位置
#         while head != None :
#             if head.next != None and head.val == head.next.val :
#                 # 重複了
#                 head = head.next
#                 # 繼續找有沒有相同的數字
#                 while head.next != None and head.val == head.next.val :
#                     head = head.next
#                 head = head.next # 這個點是不要保留的 直接接到重覆數字的 next
#                 if last_next == None:
#                     start_head = head
#                 else :
#                     last_next.next = head
#             else :
#                 # 存活
#                 last_next = head
#                 head = head.next
                
#         return start_head

# 移除 != None 好像有稍微快一點
# Runtime: 53 ms, faster than 64.45% of Python3 
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]):
        start_head = head
        last_next = None  # 存放上一個存活的數字的位置
        while head :
            if head.next and head.val == head.next.val :
                # 重複了
                head = head.next
                # 繼續找有沒有相同的數字
                while head.next and head.val == head.next.val :
                    head = head.next
                head = head.next # 這個點是不要保留的 直接接到重覆數字的 next
                if not last_next :
                    start_head = head
                else :
                    last_next.next = head
            else :
                # 存活
                last_next = head
                head = head.next
                
        return start_head

# given ans 
# 判斷是否有重複項目 改成判斷 while 之後 點有沒有改變
# class Solution:
#     def deleteDuplicates(self, head: Optional[ListNode]):
#         dummy = ListNode(0, head)
#         prev = dummy

#         while head:
#             while head.next and head.val == head.next.val:
#                 head = head.next
#             if prev.next == head:
#                 prev = prev.next
#             else:
#                 prev.next = head.next
#             head = head.next

#         return dummy.next


s = Solution()
print(s.deleteDuplicates())
