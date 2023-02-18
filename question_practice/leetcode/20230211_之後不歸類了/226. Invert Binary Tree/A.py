# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# my Beats 74.32%
class Solution(object):
    def do_invert(self, root):
        if root == None :
            return

        self.do_invert(root.left)
        self.do_invert(root.right)
        root.left , root.right = root.right , root.left

    def invertTree(self, root):
        self.do_invert(root)
        return root

# given ans
#same

s = Solution()
print(s.do_invert())



