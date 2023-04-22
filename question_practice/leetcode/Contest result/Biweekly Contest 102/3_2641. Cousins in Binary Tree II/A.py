from typing import List
import functools

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
# my Beats 76.16%
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        root.val = 0
        mem_node = [root]
        while(mem_node) :
            now_mem_node = []
            now_mem_sum = 0
            for node in mem_node :
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
# 他把 child 的 parents 存起來，到時候就去找 child_sum[parents] 就可以找到總和
# 然後有優化不用判斷 left right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = [(root, None)]
        while queue:
            next_queue = []
            child_sum = defaultdict(int)
            p = {}
            curr = 0
            
            for node, parent in queue:
                child_sum[parent] += node.val
                p[node] = parent
                curr += node.val
                if node.left:
                    next_queue.append((node.left, node))
                if node.right:
                    next_queue.append((node.right, node))
            
            for node in p:
                node.val = curr - child_sum[p[node]]
            
            queue = next_queue
        
        return root
    
# s = Solution()
# print(s.())



