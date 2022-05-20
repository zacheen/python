# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# my Runtime: 727 ms, faster than 57.40% of Python3
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode):
        
        def dfs(now_node, clone_now) :
            if now_node == target :
                return clone_now
            
            if now_node.left :
                ret = dfs(now_node.left, clone_now.left) 
                if ret :
                    return ret
            if now_node.right :
                ret = dfs(now_node.right, clone_now.right) 
                if ret :
                    return ret
            return None
        
        return dfs(original, cloned)

# given ans
# 記得是處理最尾端的點 比較快! (O)
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode):
        
        def dfs(now_node, clone_now) :
            if now_node == None :
                return False
            
            if now_node == target :
                return clone_now
            
            return dfs(now_node.left, clone_now.left) or dfs(now_node.right, clone_now.right)  
        
        return dfs(original, cloned)

s = Solution()
print(s.())



