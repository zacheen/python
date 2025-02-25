# my practice again
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None : return None
        
        def dfs(node, right_s):
            if node.right != None :
                node.val += dfs(node.right, right_s)
            else :
                node.val += right_s
            if node.left != None :
                return dfs(node.left, node.val)
            else :
                return node.val
        dfs(root, 0)
        return root 

# my Runtime: 82 ms, faster than 89.47% of Python3
class Solution:
    def convertBST(self, root):
        if root == None :
            return root
           
        def recur(now_node, parent_total):
            if now_node.right != None :
                now_node.val += recur(now_node.right, parent_total)
            ret_total = now_node.val
            now_node.val += parent_total
            if now_node.left != None :
                ret_total += recur(now_node.left, now_node.val)
                
            return ret_total

        recur(root,0)
        return root

# given ans
# 用一個變數紀錄 到目前為止總和是多少
class Solution:
    def convertBST(self, root):
        prefix = 0

        def reversedInorder(root):
            nonlocal prefix
            if not root:
                return

            reversedInorder(root.right)
            prefix += root.val
            root.val = prefix
            reversedInorder(root.left)

        reversedInorder(root)
        return root

s = Solution()
print(s.convertBST())



