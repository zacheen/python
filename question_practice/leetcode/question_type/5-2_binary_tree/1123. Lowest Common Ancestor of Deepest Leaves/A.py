# 1123. Lowest Common Ancestor of Deepest Leaves
# https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves

from typing import List
from math import inf

# my (dfs) : 0ms
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node) :
            ret_n = node
            ret_dep = 0
            if node.left :
                ret_n, ret_dep = dfs(node.left)
                ret_dep += 1
            if node.right :
                new_n, new_dep = dfs(node.right)
                new_dep += 1
                if new_dep > ret_dep :
                    return new_n, new_dep
                elif new_dep < ret_dep :
                    return ret_n, ret_dep
                else :
                    return node, ret_dep
            return ret_n, ret_dep
        return dfs(root)[0] 

# my (bfs down, bfs up) : 2ms Beats62.96%
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        bfs_l = [root]
        while True :
            new_bfs_l = []
            for node in bfs_l :
                if node.left :
                    new_bfs_l.append(node.left)
                    node.left.anc = node
                if node.right :
                    new_bfs_l.append(node.right)
                    node.right.anc = node
            if not new_bfs_l :
                break
            else :
                bfs_l = new_bfs_l

        # now bfs_l is deepest leaves
        if len(bfs_l) == 1 :
            return bfs_l[0]

        while len(bfs_l) > 1 :
            new_bfs_l = set()
            for node in bfs_l :
                new_bfs_l.add(node.anc)
            bfs_l = new_bfs_l
        return bfs_l.pop()




