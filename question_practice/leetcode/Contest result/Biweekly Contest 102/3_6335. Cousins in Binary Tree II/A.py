from typing import List
import functools

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
# my 
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        mem_val = []
        mem_node = [root]
        
        root.val = 0
        while(mem_node) :
            now_mem_node = []
            now_mem_sum = 0
            for node in mem_node :
                inside_val = []
                inside_mem_node = []
                if node.left :
                    now_mem_sum += node.left.val
                    inside_mem_node.append(node.left)
                if node.right :
                    now_mem_sum += node.right.val
                    inside_mem_node.append(node.right)
                now_mem_node.append(inside_mem_node)
            
            next_mem_node = []
            for nodes in now_mem_node :
                inside_sum = sum(n.val for n in nodes)
                after_val = now_mem_sum - inside_sum
                for node in nodes :
                    node.val = after_val
                    next_mem_node.append(node)
            mem_node = next_mem_node
        return root

# given ans

# s = Solution()
# print(s.())



