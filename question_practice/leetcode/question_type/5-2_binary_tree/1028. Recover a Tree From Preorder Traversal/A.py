# 1028. Recover a Tree From Preorder Traversal
# 

from typing import List
from math import inf

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# my 11ms Beats96.47%
class Solution:
    def recoverFromPreorder(self, traversal: str):
        root = TreeNode()
        d_cou = 0
        stack = [root]
        last_is_num = True
        num_s = []
        for c in "s"+traversal+"-":
            if c == "-" :
                if num_s and num_s[0] == "s" :
                    stack[0].val = int("".join(num_s[1:]))
                    num_s = []
                elif last_is_num :
                    while len(stack) > d_cou :
                        stack.pop()
                    new_node = TreeNode(int("".join(num_s)))
                    num_s = []
                    if stack[-1].left == None :
                        stack[-1].left = new_node
                    else :
                        stack[-1].right = new_node
                    stack.append(new_node)
                    d_cou = 0
                d_cou += 1
                last_is_num = False
            else :
                num_s.append(c)
                last_is_num = True
        return root

# given ans


s = Solution()
print("ans :",s.recoverFromPreorder("1-2--3--4-5--6--7")) # 



