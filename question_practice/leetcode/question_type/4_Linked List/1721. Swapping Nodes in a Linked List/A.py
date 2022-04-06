# my Runtime: 1068 ms, faster than 93.54% of Python3
# class Solution:
#     def swapNodes(self, head: Optional[ListNode], k: int):
#         # 找 倒數第k點 19. Remove Nth Node From End of List
#         dummy = ListNode(0, head)
        
#         fast = dummy
#         for i in range(k-1) :
#             fast = fast.next
            
#         before_k = fast
#         fast = fast.next
            
#         before_neg_k = dummy
#         while fast.next != None :
#             fast = fast.next
#             before_neg_k = before_neg_k.next
            
#         # print(before_k.val, before_neg_k.val)
#         # 找到之k與-k的前一點
#         # 原本是想要交換點 結果有錯
#         # 但之後想到 交換值就好了
#         before_k.next.val = before_neg_k.next.val

#         return dummy.next

# given ans
# 找到 第k個 跟 第-k個 然後交換值
class Solution:
    def swapNodes(self, head: ListNode, k: int):
        first = head
        for i in range(k - 1):
            first = first.next
        tmp = first
        second = head
        while first.next:
            first = first.next
            second = second.next
        tmp.val, second.val = second.val, tmp.val
        return head

s = Solution()
print(s.())



