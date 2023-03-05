# my Beats 95.4%
"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid):
        def this_grid(from_x, from_y, squ_len):
            all_one = squ_len ** 2
            total_sum = sum( sum(grid[y][from_x : from_x + squ_len]) for y in range(from_y, from_y + squ_len) )
            # print(from_x, from_y, squ_len, total_sum)
            if all_one == total_sum :
                return_Node = Node(1, True, None, None, None, None)
            elif 0 == total_sum :
                return_Node = Node(0, True, None, None, None, None)
            else :
                return_Node = Node(0, False, None, None, None, None)
                next_squ_len = squ_len >> 1 # /2
                return_Node.topLeft = this_grid(from_x, from_y, next_squ_len)
                return_Node.topRight = this_grid(from_x+next_squ_len, from_y, next_squ_len)
                return_Node.bottomLeft = this_grid(from_x, from_y+next_squ_len, next_squ_len)
                return_Node.bottomRight = this_grid(from_x+next_squ_len, from_y+next_squ_len, next_squ_len)
            return return_Node

        return this_grid(0,0,len(grid))

s = Solution()
print(s.construct())



