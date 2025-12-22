# 138. Copy List with Random Pointer
# https://leetcode.com/problems/copy-list-with-random-pointer

from typing import List
from math import inf

# my 
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        id2node = {}
        id_cnt = 0

        new_head = Node(-1)
        now_node = new_head
        
        ori_node = head
        while ori_node != None :
            now_node.next = Node(ori_node.val)
            now_node = now_node.next
            now_node.id = id_cnt
            id2node[id_cnt] = now_node
            ori_node.id = id_cnt
            ori_node = ori_node.next
            id_cnt += 1

        now_node = new_head.next
        ori_node = head
        while ori_node != None :
            if ori_node.random != None :
                # print("change random", ori_node.random.id)
                ptr_id = ori_node.random.id
                now_node.random = id2node[ptr_id]
            now_node = now_node.next
            ori_node = ori_node.next
    
        return new_head.next

