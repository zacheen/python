# My 錯誤type
# class Solution:
#     def addTwoNumbers(self, l1, l2):

#         l1_len = len(l1)
#         l2_len = len(l2)
#         sumList = []
#         addone = 0
#         for i in range(max(l1_len,l2_len)) :
            
#             if i < l1_len :
#                 if i < l2_len :
#                     # 都還有
#                     this_sum = l1[i]+l2[i]+addone
#                 else :
#                     # l2 沒了
#                     this_sum = l1[i]+addone
#             elif i < l2_len :
#                 # l1 沒了
#                 this_sum = l2[i]+addone

#             if this_sum >= 10 :
#                 addone = 1
#                 this_sum = this_sum - 10
#             else :
#                 addone = 0
#             sumList.append(this_sum)
        
#         if addone == 1 :
#             sumList.append(1)

#         return sumList

# My 網站type 但這裡不能跑
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         addone = 0
#         lastNode = 0
#         firstNode = 0
#         while True :
#             print(l1.val, l2.val)
#             this_sum = l1.val+l2.val+addone

#             if this_sum >= 10 :
#                 addone = 1
#                 this_sum = this_sum - 10
#             else :
#                 addone = 0
            
#             newListNode = ListNode(this_sum)
#             if lastNode == 0 :
#                 firstNode = newListNode
#                 lastNode = firstNode
#             else :
#                 lastNode.next = newListNode
#                 lastNode = newListNode
            
#             if l1.next == None :
#                 l1.val = 0
#                 if l2.next == None :
#                     if addone == 1 :
#                         newListNode = ListNode(1)
#                         lastNode.next = newListNode
#                     return firstNode
#                 else :
#                     l2 = l2.next
#                     continue
#             else :
#                 l1 = l1.next
                
#             if l2.next == None :
#                 l2.val = 0
#             else :
#                 l2 = l2.next

# My(優化版本) 網站type 但這裡不能跑
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        addone = 0
        lastNode = 0
        firstNode = 0
        
        while not (l1 == None and l2 == None) :

            if l1 != None :
                x = l1.val
                l1 = l1.next
            else :
                x = 0
                
            if l2 != None :
                y = l2.val
                l2 = l2.next
            else :
                y = 0
                
            this_sum = x+y+addone

            if this_sum >= 10 :
                addone = 1
                this_sum = this_sum - 10
            else :
                addone = 0
            
            newListNode = ListNode(this_sum)
            if lastNode == 0 :
                firstNode = newListNode
                lastNode = firstNode
            else :
                lastNode.next = newListNode
                lastNode = newListNode
            
        if addone == 1 :
            newListNode = ListNode(1)
            lastNode.next = newListNode
        return firstNode


s = Solution()
print(s.addTwoNumbers(l1 = [2,4,3], l2 = [5,6,4]))
print(s.addTwoNumbers(l1 = [0], l2 = [0]))
print(s.addTwoNumbers(l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]))
