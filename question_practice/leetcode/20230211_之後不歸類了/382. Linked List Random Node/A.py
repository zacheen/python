# my Beats 75.81%
import random
class Solution(object):

    def __init__(self, head):
        self.mem = []
        while(head) :
            self.mem.append(head.val)
            head = head.next
        # random.shuffle(self.mem)
        self.get_indx = 0
        

    def getRandom(self):
        return self.mem[random.randint(0,len(self.mem)-1)]

# given ans # Beats 22.58%
class Solution(object):
    def __init__(self, head):
        self.mem = head

    def getRandom(self):
        ans = -1
        i = 0
        curr = self.mem
        while(curr != None):
            if (random.randint(0,i) == 0):
                ans = curr.val
            curr = curr.next
            i+=1
        return ans

s = Solution()
# print(s.())



