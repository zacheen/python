class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

# my Beats 70.39%
class Solution:
    def cloneGraph(self, node):
        if node == None :
            return None
        
        new_nodes = {}
        
        to_do_stack = [node]
        new_nodes[node.val] = Node(node.val, [])
        return_node = new_nodes[node.val]

        i = 0
        while to_do_stack :
            this_node = to_do_stack.pop()
            new_this_node = new_nodes[this_node.val]
            for nei_node in this_node.neighbors :
                if nei_node.val not in new_nodes.keys() :
                    # print("append", nei_node.val)
                    new_nodes[nei_node.val] = Node(nei_node.val, [])
                    to_do_stack.append(nei_node)
                new_this_node.neighbors.append(new_nodes[nei_node.val])
            # print("to_do_stack",to_do_stack)
        
        return return_node

# given ans
# 還有 DFS

s = Solution()
print(s.cloneGraph())



