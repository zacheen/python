# 104. Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/

from typing import List
from math import inf

# my 
class Solution:
    def maxDepth(self, root) -> int:
        if root == None :
            return 0
        
        each_level = [root]
        now_depth = 1
        while each_level :
            new_each_level = []
            for now_node in each_level :
                if (now_node.left == None) and (now_node.right == None) :
                    return now_depth
                if now_node.left :
                    new_each_level.append(now_node.left)
                if now_node.right :
                    new_each_level.append(now_node.right)
            each_level = new_each_level
            now_depth += 1

