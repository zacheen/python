# 2415. Reverse Odd Levels of Binary Tree
# https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/description

from typing import List
import functools

# my 11ms Beats94.14%
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root):
        rev_flag = False
        stack = [root]
        while stack :
            if rev_flag :
                val_list = [p.val for p in stack]
                val_list.reverse()
                for p,v in zip(stack, val_list) :
                    p.val = v
            next_stack = []
            for p in stack :
                if p.left != None :
                    next_stack.append(p.left)
                if p.right != None :
                    next_stack.append(p.right)
            stack = next_stack
            rev_flag = not rev_flag
        return root

# given ans
# since it is "perfect binary tree"
class Solution:
    def reverseOddLevels(self, root: TreeNode | None) -> TreeNode | None:
        def dfs(left: TreeNode | None, right: TreeNode | None, isOddLevel: bool) -> None:
            if not left:
                return
            if isOddLevel:
                left.val, right.val = right.val, left.val
            dfs(left.left, right.right, not isOddLevel)
            dfs(left.right, right.left, not isOddLevel)

        dfs(root.left, root.right, True)
        return root

s = Solution()
print("ans :",s.reverseOddLevels())



