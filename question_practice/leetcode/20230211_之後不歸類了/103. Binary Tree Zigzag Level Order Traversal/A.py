# my Beats 85.19%
class Solution(object):
    def zigzagLevelOrder(self, root):
        next_level_stack = [root]
        return_ans = []
        flag_L_to_R = True
        while True :
            new_next_level_stack = []
            return_ans_inside = []
            for now_p in next_level_stack :
                if now_p != None :
                    return_ans_inside.append(now_p.val)
                    new_next_level_stack.append(now_p.right)
                    new_next_level_stack.append(now_p.left)
            if return_ans_inside :
                if flag_L_to_R :
                    return_ans_inside.reverse()
                return_ans.append(return_ans_inside)
            else :
                break
            flag_L_to_R = not flag_L_to_R
            next_level_stack = new_next_level_stack
        return return_ans


# # 各有特色 但我的實作上邏輯比較簡單
# # given ans : Deque
# # Beats 56.52%
# class Solution(object):
#     def zigzagLevelOrder(self, root):
#         if not root:
#             return []

#         ans = []
#         q = collections.deque([root])
#         isLeftToRight = True

#         while q:
#             currLevel = []
#             for _ in range(len(q)):
#                 if isLeftToRight:
#                     node = q.popleft()
#                     currLevel.append(node.val)
#                     if node.left:
#                             q.append(node.left)
#                     if node.right:
#                             q.append(node.right)
#                 else:
#                     node = q.pop()
#                     currLevel.append(node.val)
#                     if node.right:
#                             q.appendleft(node.right)
#                     if node.left:
#                             q.appendleft(node.left)
#             ans.append(currLevel)
#             isLeftToRight = not isLeftToRight

#         return ans

# # given ans : Queue
# # Beats 20.11%
# class Solution(object):
#     def zigzagLevelOrder(self, root):
#         if not root:
#             return []

#         ans = []
#         q = collections.deque([root])
#         isLeftToRight = True

#         while q:
#             size = len(q)
#             currLevel = [0] * size
#             for i in range(size):
#                 node = q.popleft()
#                 index = i if isLeftToRight else size - i - 1
#                 currLevel[index] = node.val
#                 if node.left:
#                     q.append(node.left)
#                 if node.right:
#                     q.append(node.right)
#             ans.append(currLevel)
#             isLeftToRight = not isLeftToRight

#         return ans

s = Solution()
print(s.zigzagLevelOrder())



