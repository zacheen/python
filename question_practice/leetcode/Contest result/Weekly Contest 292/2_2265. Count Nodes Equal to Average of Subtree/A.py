# my 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def averageOfSubtree(self, root):
#         def recur(root) :
#             if root.left == None and root.right == None :
#                 return root.val, 1, 1  # total, fit_count, sub_count
            
#             total = root.val
#             fit_count = 0
#             sub_count = 1
#             if root.left :
#                 t_total, t_fit_count, t_sub_count = recur(root.left)
#                 total += t_total
#                 fit_count += t_fit_count
#                 sub_count += t_sub_count
                
#             if root.right :
#                 t_total, t_fit_count, t_sub_count = recur(root.right)
#                 total += t_total
#                 fit_count += t_fit_count
#                 sub_count += t_sub_count
                
#             # print( (total//sub_count) , root.val)
#             if (total//sub_count) == root.val :
#                 fit_count += 1
                
#             return total, fit_count, sub_count
        
#         return recur(root)[1]

# given ans
# 好看的寫法 (O)
class Solution:
    def averageOfSubtree(self, root):
        z = 0
        def dfs(root):
            nonlocal z
            if root is None:
                return 0, 0
            ls, lc = dfs(root.left)
            rs, rc = dfs(root.right)
            s = ls + rs + root.val
            c = lc + rc + 1
            if s // c == root.val:
                z += 1
            return s, c
        dfs(root)
        return z



