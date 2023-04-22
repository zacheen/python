from typing import List
import functools

# my Beats 98.8%
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # 每個點都走過 跟 min_indx 與 max_indx 比較
            # min_indx max_indx 每個點紀錄最前面跟最後面的位置
        min_indx = []
        max_indx = []

        def dfs(root, layer, indx) :
            if root :
                if len(min_indx) <= layer :
                    min_indx.append(indx)
                    max_indx.append(indx)
                else :
                    min_indx[layer] = min(min_indx[layer], indx)
                    max_indx[layer] = max(max_indx[layer], indx)
                dfs(root.left, layer+1, indx*2) 
                dfs(root.right, layer+1, indx*2+1) 
        
        dfs(root,0,0)
        return max( (r-l) for l, r in zip(min_indx, max_indx))+1

# # wrong
# # 有可能我先走到 Max indx 再走到 mix indx
# class Solution:
#     def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
#         # 每個點都走過 跟 min_indx 與 max_indx 比較
#             # min_indx max_indx 每個點紀錄最前面跟最後面的位置
#         # 應該是還可以優化拉，但有點複雜就不做了
#         min_indx = []
#         ans = 0
#         def dfs(root, layer, indx) :
#             nonlocal ans
#             if root :
#                 if len(min_indx) <= layer :
#                     min_indx.append(indx)
#                     ans = max(ans, 1)
#                 else :
#                     min_indx[layer] = min(min_indx[layer], indx)
#                     ans = max(ans, indx - min_indx[layer])
#                 dfs(root.left, layer+1, indx*2) 
#                 dfs(root.right, layer+1, indx*2+1) 
        
#         dfs(root,0,0)
#         return ans
    
# given ans
# BFS 一次只計算一層 就不用紀錄 layer

# s = Solution()
# print(s.())



