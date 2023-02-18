# my 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# # 錯誤
# class Solution(object):
#     def maxDepth(self, root):
#         # 我一開始以為是 list 的 tree
#         n = len(root) + 1
#         count = 0
#         while n != 1 :
#             n //= 2
#             count+=1
#         return count

# 方法1 Beats 75.79%
class Solution(object):
    def return_depth(self, root, now_detph):
        left_longest_detph = now_detph
        right_longest_detph = now_detph
        if root.left != None :
            left_longest_detph = self.return_depth(root.left, now_detph + 1) 
        if root.right != None :
            right_longest_detph = self.return_depth(root.right, now_detph + 1)
        return max(left_longest_detph, right_longest_detph)
    
    def maxDepth(self, root):
        if root == None :
            return 0

        return self.return_depth(root, 1)


# 方法2 Beats 62.90% (不知道為什麼比較慢 照道理應該是一樣快)
class Solution(object):
    def return_depth(self, root):
        if root == None :
            return 0
        return max(self.return_depth(root.right), self.return_depth(root.left))+1
    
    def maxDepth(self, root):
        return self.return_depth(root)
    
# 方法3 再簡化 
# Beats 40.47% (但不知道為什麼又更慢了)
class Solution(object):  
    def maxDepth(self, root):
        if root == None :
            return 0
        return max(self.maxDepth(root.right), self.maxDepth(root.left))+1
# given ans

s = Solution()
print(s.())



