# my Beats 86.11%
from collections import deque 
class Solution(object):
    def isCompleteTree(self, root):
        stack = deque([root])

        while stack[0] :
            now_node = stack.popleft()
            stack.append(now_node.left)
            stack.append(now_node.right)

        for node in stack :
            if node :
                return False
        return True

# given ans
# BFS 的想法一樣
# 另一種解法 DFS(感覺很複雜 看起來也不會比較快)

s = Solution()
print(s.isCompleteTree())



