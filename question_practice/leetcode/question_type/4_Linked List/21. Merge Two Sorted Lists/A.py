# my 
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]):
        # 把 list2 插入 list1 中
        if list1 == None :
            return list2
        if list2 == None :
            return list1
        
        if list2.val < list1.val :
            head, list2 = list2, list2.next
            head.next = list1
        else :
            head = list1
        now_list1 = head
        
        while list2 :
            if now_list1.next == None :
                now_list1.next = list2
                break
            # print(now_list1.val , list2.val)
            if now_list1.next.val > list2.val :
                now_list1.next, list2.next, list2 = list2, now_list1.next, list2.next
            now_list1 = now_list1.next    
        return head

# given ans
# 把問題簡單化
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]):
        if not list1 or not list2:
            return list1 if list1 else list2
        if list1.val > list2.val:
            list1, list2 = list2, list1
        list1.next = self.mergeTwoLists(list1.next, list2)
        return list1

s = Solution()
print(s.mergeTwoLists())



