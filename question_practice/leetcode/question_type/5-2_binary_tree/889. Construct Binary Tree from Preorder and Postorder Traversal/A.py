# 889. Construct Binary Tree from Preorder and Postorder Traversal
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal

from typing import List
from math import inf

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# my 0ms Beats100.00%
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]):
        stack_t = []
        post_i = 0
        for p_i, pre in enumerate(preorder) :
            new_node = TreeNode(pre)
            if p_i == 0 :
                stack_t = [new_node]
                continue
            if stack_t[-1].left == None :
                stack_t[-1].left = new_node
            else :
                stack_t[-1].right = new_node
            stack_t.append(new_node)

            while len(stack_t) > 1 and postorder[post_i] == stack_t[-1].val :
                stack_t.pop()
                post_i += 1
        return stack_t[0]

# given ans


s = Solution()
print("ans :",s.constructFromPrePost(preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1])) # 



