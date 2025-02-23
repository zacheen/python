# 863. All Nodes Distance K in Binary Tree
# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree

from typing import List
from math import inf

# my 38ms Beats81.38%
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        li = defaultdict(list)

        queue = [root]
        count_down = inf
        while queue and count_down >= 0:
            new_queue = []
            for node in queue :
                if node.val == target :
                    count_down = k
                if node.left != None :
                    new_queue.append(node.left)
                    li[node.left.val].append(node.val)
                    li[node.val].append(node.left.val)
                if node.right != None :
                    new_queue.append(node.right)
                    li[node.right.val].append(node.val)
                    li[node.val].append(node.right.val)
            queue = new_queue
            count_down -= 1
        # print(li)

        queue = [(target.val,-1)]
        count_down = k
        while queue and count_down > 0:
            new_queue = []
            for now_n, prev_n in queue :
                # print(now_n, li[now_n])
                for nei_n in li[now_n] :
                    if nei_n == prev_n :
                        continue
                    new_queue.append((nei_n, now_n))
            queue = new_queue
            count_down -= 1
            # print("new",queue)
        return [item[0] for item in queue]
                                   
# optimized, but code longer : 36ms Beats89.19%
    # Only mem the links above target
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if k == 0 : 
            return [target.val]
        
        li = defaultdict(list)
        queue = [root]
        count_down = inf
        while queue and count_down > 0:
            new_queue = []
            for node in queue :
                if node.val == target.val :
                    count_down = k-2
                    target = node
                    continue
                if node.left != None :
                    new_queue.append(node.left)
                    li[node.left.val].append(node.val)
                    li[node.val].append(node.left.val)
                if node.right != None :
                    new_queue.append(node.right)
                    li[node.right.val].append(node.val)
                    li[node.val].append(node.right.val)
            queue = new_queue
            count_down -= 1

        # ans below target
        queue = [target]
        count_down = k
        while queue and count_down > 0:
            new_queue = []
            for node in queue :
                if node.left != None :
                    new_queue.append(node.left)
                if node.right != None :
                    new_queue.append(node.right)
            queue = new_queue
            count_down -= 1
        ans = [item.val for item in queue]

        # ans not below target
        queue = [(target.val,-1)]
        count_down = k
        while queue and count_down > 0:
            new_queue = []
            for now_n, prev_n in queue :
                for nei_n in li[now_n] :
                    if nei_n == prev_n :
                        continue
                    new_queue.append((nei_n, now_n))
            queue = new_queue
            count_down -= 1

        return ans + [item[0] for item in queue]




