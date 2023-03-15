# my Beats 77.4%
from collections import deque
class Solution(object):
    def isSymmetric(self, root):
        left_stack = deque([root.left])
        right_stack = deque([root.right])

        while left_stack :
            now_left  = left_stack.popleft()
            now_right = right_stack.popleft()
            if now_left == None :
                if now_right == None : 
                    # print("both None")
                    continue
                else :
                    return False
            else :
                if now_right == None :
                    return False

            # print(now_left.val, now_right.val)
            if now_left.val != now_right.val :
                return False

            left_stack.append(now_left.left)
            right_stack.append(now_right.right)
            
            left_stack.append(now_left.right)
            right_stack.append(now_right.left)
        
        return True

# 不使用 deque (其實就是 recursive 的概念)
# Beats 62.67% (應該是 test case 的問題)
class Solution(object):
    def isSymmetric(self, root):
        left_stack = [root.left]
        right_stack = [root.right]

        while left_stack :
            now_left  = left_stack.pop()
            now_right = right_stack.pop()
            if now_left == None :
                if now_right == None : 
                    # print("both None")
                    continue
                else :
                    return False
            else :
                if now_right == None :
                    return False

            # print(now_left.val, now_right.val)
            if now_left.val != now_right.val :
                return False

            left_stack.append(now_left.left)
            right_stack.append(now_right.right)
            
            left_stack.append(now_left.right)
            right_stack.append(now_right.left)
        
        return True

# given ans
class Solution:
    def isSymmetric(self, root):
        def judgeSymmetric(p, q):
            if not p or not q:
                return p == q

            return p.val == q.val and \
                judgeSymmetric(p.left, q.right) and \
                judgeSymmetric(p.right, q.left)

        return judgeSymmetric(root, root)
  
s = Solution()
print(s.isSymmetric())



