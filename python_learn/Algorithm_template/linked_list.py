class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next 

def create_linkList(l):
    start = ListNode()
    dummy = start
    for i in l:
        start.next = ListNode(i, None)
        start = start.next
    return dummy.next

# # 最基本的範例 #############################################
def basic_print(head):
    # 現在指到的點 : head
    # head前一個點 : prev
    # 記錄一開始的點 : dummy.next
    dummy = ListNode(0, head)
    prev = dummy

    ret = []
    while head:
        if True:  # 條件
            # 符合條件要做的事
            ret.append(head.val)
            prev = head
            head = head.next
            # 1. 刪除
            # prev.next = head.next
            # head = prev.next # 或是 head = head.next
        else :
            # 移到下一個點
            prev = head
            head = head.next
    return ret

# ll = create_linkList([1,2,3,4,5])
# print(basic_print(ll))

# # 反轉 link list #############################################
def reverseList(head):
    prev = None
    curr = head

    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    return prev

# ll = create_linkList([1,2,3,4,5,6])
# ret = reverseList(ll)
# print(basic_print(ret))

# # 優化到極致的刪除點的方法  #############################################  
def delete(head, val):
    dummy = ListNode()
    prev = dummy

    while head:
        if head.val != val : # 判斷... :
            # 如果沒事 就接起來  有事就跳過
            # prev 就接到 現在這個點(head)
            prev.next = head
            # 修改 prev
            prev = prev.next
        # 移到下一個點
        head = head.next

    prev.next = None # 不懂為什麼要這個

    return dummy.next

# ll = create_linkList([1,2,6,3,4,5,6,1])
# ret = delete(ll, 1)
# print(basic_print(ret))







