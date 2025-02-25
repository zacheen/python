# 1261. Find Elements in a Contaminated Binary Tree
# https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree
    # 這題教 如何用 index 找到對應位置

from typing import List
from math import inf

# my 2ms Beats94.39%
class FindElements:
    def __init__(self, root):
        self.tree = root

    def find(self, target: int) -> bool:
        now_n = self.tree
        for c in f'{target+1:b}'[1:]:
            if now_n == None : 
                return False
            if c == "0" :
                now_n = now_n.left
            else :
                now_n = now_n.right
        return now_n != None

from collections import deque

# my version 2
class FindElements:
    def __init__(self, root):
        self.mem = set()
        root.val = 0
        queue = deque([root])
        while queue :
            now_n = queue.popleft()
            self.mem.add(now_n.val)
            if now_n.left != None :
                now_n.left.val = now_n.val*2 + 1
                queue.append(now_n.left)
            if now_n.right != None :
                now_n.right.val = now_n.val*2 + 2
                queue.append(now_n.right)

    def find(self, target: int) -> bool:
        return target in self.mem
