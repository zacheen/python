# 這個是特有格式 所以不能跑
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# My 靠腰 我怎麼使用偷吃步
class Solution:
    def sortList(self, head):
        
        ll = []
        
        while head != None :
            ll.append(head.val)
            head = head.next
            
        ll.sort()
        print(ll)
        
        lastNode = None
        startNode = None
        for eachNum in ll :
            newNode = ListNode(eachNum)
            if lastNode == None :
                startNode = newNode
                lastNode = newNode
            else :
                lastNode.next = newNode
                lastNode = newNode
                
        return startNode
# s = Solution()
# print(s.())