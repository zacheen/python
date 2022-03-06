# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# My Runtime: 44 ms, faster than 87.84% of Python3
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None :
            return False
        
        def sum (total, node) :
            total_now = total + node.val
            if node.left != None :
                ret = sum(total_now, node.left)
                if ret :
                    return True
            if node.right != None :
                ret = sum(total_now, node.right)
                if ret :
                    return True
            elif node.left == None :
                if total_now == targetSum :
                    return True
                else :
                    return False
                
        return sum(0, root)
        
# s = Solution()
# print(s.())